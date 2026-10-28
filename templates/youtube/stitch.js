/* Cross-stitch any short word or number, the way the After Harvest stitch icons are made (art/figma/stitch-*.png,
   art/scarecrow-*.svg: one X per cell, the top stitch lighter than the one under it).
   <div data-stitch="$100K" data-cell="14" data-color="#B06A4A"></div>
   data-px: the size the word is drawn at before it becomes stitches (18 = about 13 rows); data-weight: Hanken weight. */
(function () {
  function rand(seed) { let s = seed % 2147483647; if (s <= 0) s += 2147483646; return () => (s = s * 16807 % 2147483647) / 2147483647; }
  function mix(hex, f) {
    const n = parseInt(hex.slice(1), 16), t = f > 0 ? 255 : 0, p = Math.abs(f);
    const c = [n >> 16, (n >> 8) & 255, n & 255].map(v => Math.round(v + (t - v) * p));
    return `rgb(${c[0]},${c[1]},${c[2]})`;
  }
  function stitch(el) {
    const text = el.dataset.stitch, cell = +(el.dataset.cell || 14), color = el.dataset.color || "#B06A4A";
    const px = +(el.dataset.px || 18), font = `${el.dataset.weight || 800} ${px}px "Body"`;
    const c = document.createElement("canvas"), ctx = c.getContext("2d");
    ctx.font = font;
    const w = Math.ceil(ctx.measureText(text).width) + 6, h = Math.ceil(px * 1.3) + 6;
    c.width = w; c.height = h; ctx.font = font; ctx.textBaseline = "top"; ctx.fillStyle = "#000"; ctx.fillText(text, 3, 3);
    const d = ctx.getImageData(0, 0, w, h).data, cells = [];
    let x0 = 1e9, y0 = 1e9, x1 = 0, y1 = 0;
    for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) if (d[(y * w + x) * 4 + 3] > 110) {
      cells.push([x, y]); x0 = Math.min(x0, x); y0 = Math.min(y0, y); x1 = Math.max(x1, x); y1 = Math.max(y1, y);
    }
    const R = rand(text.length * 131 + cell * 7), sw = cell * 0.3, k = cell * 0.17;
    const under = mix(color, -0.22), over = color, shine = mix(color, 0.38);
    let p = "";
    for (const [x, y] of cells) {
      const X = (x - x0) * cell, Y = (y - y0) * cell, j = () => ((R() - 0.5) * cell * 0.09).toFixed(1);
      const a = [X + k, Y + k, X + cell - k, Y + cell - k], b = [X + cell - k, Y + k, X + k, Y + cell - k];
      p += `<path d="M${a[0] + +j()} ${a[1] + +j()}L${a[2] + +j()} ${a[3] + +j()}" stroke="${under}" stroke-width="${sw}"/>`;
      p += `<path d="M${b[0] + +j()} ${b[1] + +j()}L${b[2] + +j()} ${b[3] + +j()}" stroke="${over}" stroke-width="${sw}"/>`;
      p += `<path d="M${b[0] - sw * 0.1} ${b[1] + sw * 0.18}L${b[2] + sw * 0.2} ${b[3] - sw * 0.1}" stroke="${shine}" stroke-width="${(sw * 0.26).toFixed(1)}" opacity=".75"/>`;
    }
    const W = (x1 - x0 + 1) * cell, H = (y1 - y0 + 1) * cell;
    el.innerHTML = `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" style="display:block;overflow:visible;filter:drop-shadow(0 1.5px 1.2px rgba(38,33,25,.28))"><g stroke-linecap="round" fill="none">${p}</g></svg>`;
  }
  document.fonts.ready.then(() => document.querySelectorAll("[data-stitch]").forEach(stitch));
})();
