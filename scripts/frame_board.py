"""Storyboard sheets -> one board per video of its DISTINCT frames, numbered, for picking layouts.

    python3 scripts/frame_board.py <video folder> [...] [--out DIR] [--cols 6] [--diff 14]

A frame is kept when it differs from the last kept frame (mean pixel difference above --diff, 0-255),
so a slide held for a minute shows once. Writes <out>/<id>-board.jpg and <id>-frames/<n>_<m-ss>.png
(the kept frames, so a pick can be cropped out by number). 0 tokens.
"""
import glob, json, os, sys
from PIL import Image, ImageChops, ImageDraw, ImageStat


def frames(folder):
    meta = json.load(open(os.path.join(folder, "meta.json")))
    sheets = sorted(glob.glob(os.path.join(folder, "sheets", "S*.jpg")))
    n = len(sheets)
    out = []
    for si, path in enumerate(sheets):
        im = Image.open(path).convert("RGB")
        w, h = im.size
        tw, th = 320, 180
        cols, rows = max(1, w // tw), max(1, h // th)
        per = cols * rows
        step = (meta["duration"] or 0) / max(1, n * per)
        for k in range(per):
            t = (si * per + k) * step
            if meta["duration"] and t > meta["duration"]:
                break
            tile = im.crop(((k % cols) * tw, (k // cols) * th, (k % cols + 1) * tw, (k // cols + 1) * th))
            if ImageStat.Stat(tile.convert("L")).stddev[0] < 3:   # blank tail of the last sheet
                continue
            out.append((t, tile))
    return meta, out


def distinct(tiles, diff):
    kept, last = [], None
    for t, tile in tiles:
        small = tile.resize((80, 45)).convert("L")
        if last is None or ImageStat.Stat(ImageChops.difference(small, last)).mean[0] > diff:
            kept.append((t, tile))
            last = small
    return kept


def board(folder, out, cols, diff):
    meta, tiles = frames(folder)
    kept = distinct(tiles, diff)
    vid = meta["id"]
    fdir = os.path.join(out, f"{vid}-frames")
    os.makedirs(fdir, exist_ok=True)
    tw, th, pad = 320, 180, 22
    rows = (len(kept) + cols - 1) // cols
    b = Image.new("RGB", (cols * tw, rows * (th + pad) + 40), "white")
    d = ImageDraw.Draw(b)
    d.text((8, 12), f"{meta['title']}  |  {meta.get('view_count')} views  |  {len(kept)} distinct frames", fill="black")
    for i, (t, tile) in enumerate(kept):
        stamp = f"{int(t) // 60}-{int(t) % 60:02d}"
        tile.save(os.path.join(fdir, f"{i + 1:03d}_{stamp}.png"))
        x, y = (i % cols) * tw, 40 + (i // cols) * (th + pad)
        b.paste(tile, (x, y))
        d.text((x + 4, y + th + 4), f"#{i + 1}  {stamp.replace('-', ':')}", fill="black")
    path = os.path.join(out, f"{vid}-board.jpg")
    b.save(path, quality=80)
    print(f"{vid}: {len(tiles)} frames -> {len(kept)} distinct, {path}")


if __name__ == "__main__":
    args = sys.argv[1:]
    opts = {"--out": "boards", "--cols": "6", "--diff": "14"}
    for k in list(opts):
        if k in args:
            i = args.index(k)
            opts[k] = args[i + 1]
            del args[i:i + 2]
    os.makedirs(opts["--out"], exist_ok=True)
    for f in args:
        board(f, opts["--out"], int(opts["--cols"]), float(opts["--diff"]))
