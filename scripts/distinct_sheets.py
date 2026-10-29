"""Storyboard sheets -> only the frames worth reading, repacked as new sheets (SOP: sops/video-teardown.md, step 3).

    python3 scripts/distinct_sheets.py "<video folder>" [...] [--min-change 0.002] [--camera-every 60] [--scene-every 30]

Plain "keep what changed" fails on these videos: on camera the speaker moves all the time, so every talking-head
frame differs, while a page held on screen looks identical. So each frame is first called a camera shot (a big face
fills it, found with OpenCV's YuNet model in assets/models/) or content (a page, a pad, a sheet, a slide):
  - camera shots: one kept per run, then one more every --camera-every seconds while the run lasts;
  - content: split into scenes at every big change (a new page, slide or cut: more than 5% of the pixels); in a
    scene, the first frame, a frame every --scene-every seconds that changed by more than --min-change of its
    pixels, and the finished state are kept. Any small face and the body under it are left out of the comparison
    (a PiP, a speaker beside a slide), so a newly written word counts and a held page does not.
Writes <folder>/distinct/D00.jpg ... (3x3 frames of 320x180, each stamped with its time) and <folder>/distinct.md
(each kept frame, its kind, and every word said until the next kept frame), and prints how many frames it kept.
A camera shot is a face at least 10% of the frame high, outside the bottom corners (see is_camera).
The teardown agents read these instead of every sheet. 0 tokens, a few seconds.
"""
import json, os, re, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YUNET = os.path.join(ROOT, "assets", "models", "face_detection_yunet_2023mar.onnx")
TW, TH = 320, 180


def clock(sec):
    sec = int(sec)
    h, m, s = sec // 3600, sec % 3600 // 60, sec % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def seconds(stamp):
    parts = [int(p) for p in stamp.split(":")]
    return sum(p * 60 ** i for i, p in enumerate(reversed(parts)))


def frames(folder):
    """(time, image) for every frame, in order, with times from study.md (the last sheet is often partial)."""
    study = open(os.path.join(folder, "study.md")).read()
    out = []
    for block in re.split(r"^## sheets/", study, flags=re.M)[1:]:
        sheet = block.split(".jpg", 1)[0]
        im = Image.open(os.path.join(folder, "sheets", sheet + ".jpg")).convert("RGB")
        cols = max(1, im.width // TW)
        for r, c, t in re.findall(r"^- row (\d+) col (\d+) \[([\d:]+)\]", block, re.M):
            r, c = int(r) - 1, int(c) - 1
            crop = im.crop((c * TW, r * TH, (c + 1) * TW, (r + 1) * TH))
            if np.asarray(crop.convert("L")).std() < 4:   # an empty cell at the end of the last sheet
                continue
            out.append((seconds(t), crop, f"{sheet} r{r + 1}c{c + 1}"))
    return out


def detector():
    try:
        import cv2
    except ImportError:
        sys.exit("opencv is not installed: pip install opencv-python-headless")
    if not os.path.exists(YUNET):
        sys.exit(f"missing {YUNET}")
    return cv2, cv2.FaceDetectorYN.create(YUNET, "", (TW * 2, TH * 2), 0.6, 0.3, 50)


def faces(cv2, det, img):
    """Faces as (x, y, w, h) in 320x180 frame pixels."""
    bgr = cv2.cvtColor(np.asarray(img.resize((TW * 2, TH * 2))), cv2.COLOR_RGB2BGR)
    _, found = det.detect(bgr)
    return [tuple(float(v) / 2 for v in f[:4]) for f in (found if found is not None else [])]


def is_camera(boxes):
    """A camera shot: a face at least 10% of the frame height, outside the bottom corners where a picture-in-picture
    sits. Measured on all five videos (2026-10-29): on-camera faces are 10-30% high and never in a bottom corner; the
    PiP face is 4-10% and always in one; Jason's slide video shows him at 6-10% beside the slide."""
    for x, y, w, h in boxes:
        cx, cy = (x + w / 2) / TW, (y + h / 2) / TH
        corner = cy > 0.62 and (cx > 0.74 or cx < 0.26)
        if h / TH >= 0.10 and not corner:
            return True
    return False


def mask_for(boxes):
    """Pixels to compare: everything except each small face and the body under it (a PiP or a speaker beside a
    slide moves all the time; that is not new content)."""
    m = np.ones((TH, TW), bool)
    for x, y, w, h in boxes:
        x0, x1 = int(max(0, x - 1.6 * w)), int(min(TW, x + 2.6 * w))
        y0, y1 = int(max(0, y - 0.8 * h)), TH
        m[y0:y1, x0:x1] = False
    return m


def changed(a, b, mask):
    """Share of the compared pixels that changed between two content frames."""
    d = np.abs(np.asarray(a.convert("L"), int) - np.asarray(b.convert("L"), int)) > 28
    return float(d[mask].mean()) if mask.any() else 0.0


def words(folder):
    path = os.path.join(folder, "transcript.json")
    return json.load(open(path)) if os.path.exists(path) else []


BIG = 0.05  # a change on more than 5% of the pixels starts a new scene (a new page, a cut, a new slide)


def run(folder, min_change, camera_every, scene_every):
    cv2, det = detector()
    all_frames = frames(folder)
    kept, cam_since, scene = [], None, []

    def close_scene():
        """A scene is a run of content frames with no big change (a page being written on, a sheet being walked
        through): keep its first frame, a frame each --scene-every seconds that changed, and its finished state."""
        if not scene:
            return
        picked, last = [scene[0]], scene[0]
        for f in scene[1:]:
            if changed(f[1], last[1], mask_for(f[3] + last[3])) > min_change and f[0] - last[0] >= scene_every:
                picked.append(f)
                last = f
        end = scene[-1]
        if end is not last and changed(end[1], last[1], mask_for(end[3] + last[3])) > min_change:
            picked.append(end)
        kept.extend((t, img, where, "content") for t, img, where, _ in picked)
        scene.clear()

    for t, img, where in all_frames:
        boxes = faces(cv2, det, img)
        if is_camera(boxes):
            close_scene()
            if cam_since is None or t - cam_since >= camera_every:
                kept.append((t, img, where, "camera"))
                cam_since = t
            continue
        cam_since = None
        if scene and changed(img, scene[-1][1], mask_for(boxes + scene[-1][3])) > BIG:
            close_scene()
        scene.append((t, img, where, boxes))
    close_scene()

    out_dir = os.path.join(folder, "distinct")
    os.makedirs(out_dir, exist_ok=True)
    for f in os.listdir(out_dir):
        os.remove(os.path.join(out_dir, f))
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 15)
    except OSError:
        font = ImageFont.load_default()
    lines = json.load(open(os.path.join(folder, "meta.json")))
    md = [f"# Distinct frames: {lines.get('title')}", "",
          f"{len(kept)} of {len(all_frames)} storyboard frames kept by scripts/distinct_sheets.py (camera shots: one per "
          f"run, then one every {camera_every} s; content: each new page or slide, then every {scene_every} s while it is "
          f"built up, and its finished state). "
          "Sheets distinct/DNN.jpg hold 9 frames each, read left to right, top to bottom; each frame is stamped with its "
          "time. Under each frame: its kind, where it came from, and the words said until the next kept frame.", ""]
    caps = words(folder)
    for i in range(0, len(kept), 9):
        sheet = Image.new("RGB", (TW * 3, TH * 3), (0, 0, 0))
        name = f"D{i // 9:02d}"
        md.append(f"## distinct/{name}.jpg  [{clock(kept[i][0])} - {clock(kept[min(i + 8, len(kept) - 1)][0])}]")
        md.append("")
        for k, (t, img, where, kind) in enumerate(kept[i:i + 9]):
            r, c = divmod(k, 3)
            tile = img.copy()
            d = ImageDraw.Draw(tile)
            label = clock(t)
            w = d.textlength(label, font=font)
            d.rectangle((0, 0, w + 10, 21), fill=(255, 255, 255))
            d.text((5, 2), label, fill=(0, 0, 0), font=font)
            sheet.paste(tile, (c * TW, r * TH))
            nxt = kept[i + k + 1][0] if i + k + 1 < len(kept) else 10 ** 9
            said = " ".join(x["text"] for x in caps if t <= x["t"] < nxt)
            md.append(f"- row {r + 1} col {c + 1} [{clock(t)}] {kind} ({where}): {said}")
        sheet.save(os.path.join(out_dir, name + ".jpg"), quality=88)
        md.append("")
    open(os.path.join(folder, "distinct.md"), "w").write("\n".join(md))
    n_sheets = (len(kept) + 8) // 9
    cams = sum(1 for k in kept if k[3] == "camera")
    print(f"OK {os.path.relpath(folder, ROOT)}: kept {len(kept)} of {len(all_frames)} frames "
          f"({len(kept) / max(1, len(all_frames)):.0%}; {cams} camera, {len(kept) - cams} content) -> {n_sheets} sheets in distinct/")
    return n_sheets


def main():
    args = sys.argv[1:]
    opts = {"--min-change": 0.002, "--camera-every": 60, "--scene-every": 30}
    folders = []
    i = 0
    while i < len(args):
        if args[i] in opts:
            opts[args[i]] = float(args[i + 1])
            i += 2
        else:
            folders.append(args[i])
            i += 1
    if not folders:
        sys.exit(__doc__)
    for f in folders:
        run(os.path.abspath(f), opts["--min-change"], opts["--camera-every"], opts["--scene-every"])


if __name__ == "__main__":
    main()
