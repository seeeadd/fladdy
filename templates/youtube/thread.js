/* Needlework marks: After Harvest's hand instead of a pen (Sean 2026-10-29: tape is generic; the brand already
   strikes "AD" through with a red thread, art/figma/stitch-icons-watch-video-ad-money.png). Drawn here so they are
   ours, sharp at any size, and need no stock photo.

   A slide lists its marks in data-thread (JSON), in 1920x1080 coordinates:
     {"k":"run",    "d":[[x,y],...]}            running stitch along a smooth curve through the points
     {"k":"lay",    "d":[[x,y],...]}            one laid thread (no gaps), twisted, with "knot" and/or "needle" ends
     {"k":"arrow",  "d":[[x,y],...]}            running stitch ending in a stitched V
     {"k":"loop",   "x","y","w","h"}            running stitch round an ellipse (centre x,y)
     {"k":"strike", "d":[[x1,y1],[x2,y2]]}      one long straight stitch (the brand's "AD")
     {"k":"tack",   "x","y","s"}                one cross-stitch, to tack a corner down
     {"k":"pin",    "x","y","a","c"}            a pearl-head pin pushed through at x,y, angle a (degrees)
   Common keys: c (colour name or hex), tw (thread width, default 5), len / gap (stitch and gap length),
   knot (true: a knot at the start), needle (true: a needle at the end), seed.
   data-thread also works on any element, in that element's own pixels, so the marks turn with it.
   Decorators, drawn inside the element so they turn with it:
     data-sew="colour"   a running stitch round its inside edge: a print sewn onto the page
                         (data-sew-inset, default 12; data-sew-w, -len, -gap)
     data-tack="colour"  a woven label sewn down at both ends
     data-hem="colour"   a running-stitch hem along the bottom of a band of cloth (data-hem-inset)
     data-hoop           the camera in an embroidery hoop (see hoop() below) */
(function () {
  const COLORS = { rust: "#A85A3C", red: "#B5372B", olive: "#6F7452", sage: "#8A9068", ink: "#2E2820",
                   wheat: "#C89B4B", gold: "#D2A33A", cream: "#F3EEDF", plum: "#7A4A5C", lilac: "#9C8FB5" };
  const NS = "http://www.w3.org/2000/svg";
  const col = (c) => COLORS[c] || c || COLORS.rust;
  function rand(seed) { let s = Math.floor(seed) % 2147483647; if (s <= 0) s += 2147483646;
    return () => (s = s * 16807 % 2147483647) / 2147483647; }
  function mix(hex, f) {
    const n = parseInt(hex.slice(1), 16), t = f > 0 ? 255 : 0, p = Math.abs(f);
    const c = [n >> 16, (n >> 8) & 255, n & 255].map((v) => Math.round(v + (t - v) * p));
    return `rgb(${c[0]},${c[1]},${c[2]})`;
  }
  const el = (tag, attrs) => { const e = document.createElementNS(NS, tag); for (const k in attrs) e.setAttribute(k, attrs[k]); return e; };

  // a smooth curve through the points (Catmull-Rom), sampled every ~2 px, with its running length
  function sample(pts, closed) {
    const P = closed ? [pts[pts.length - 1], ...pts, pts[0], pts[1]] : [pts[0], ...pts, pts[pts.length - 1]];
    const out = [];
    for (let i = 1; i < P.length - 2; i++) {
      const [p0, p1, p2, p3] = [P[i - 1], P[i], P[i + 1], P[i + 2]];
      const n = Math.max(2, Math.ceil(Math.hypot(p2[0] - p1[0], p2[1] - p1[1]) / 2));
      for (let j = 0; j < n; j++) {
        const t = j / n, t2 = t * t, t3 = t2 * t;
        const f = (a, b, c, d) => 0.5 * (2 * b + (-a + c) * t + (2 * a - 5 * b + 4 * c - d) * t2 + (-a + 3 * b - 3 * c + d) * t3);
        out.push([f(p0[0], p1[0], p2[0], p3[0]), f(p0[1], p1[1], p2[1], p3[1])]);
      }
    }
    out.push(closed ? out[0] : pts[pts.length - 1]);
    let L = 0; const acc = [0];
    for (let i = 1; i < out.length; i++) { L += Math.hypot(out[i][0] - out[i - 1][0], out[i][1] - out[i - 1][1]); acc.push(L); }
    return { pts: out, acc, L };
  }
  function at(s, d) { // point and angle at distance d along a sampled curve
    let i = 1; while (i < s.acc.length - 1 && s.acc[i] < d) i++;
    const a = s.pts[i - 1], b = s.pts[i], seg = s.acc[i] - s.acc[i - 1] || 1, t = (d - s.acc[i - 1]) / seg;
    return [a[0] + (b[0] - a[0]) * t, a[1] + (b[1] - a[1]) * t, Math.atan2(b[1] - a[1], b[0] - a[0])];
  }
  function between(s, d0, d1) { // the sampled points from d0 to d1
    const out = [at(s, d0)];
    for (let i = 0; i < s.pts.length; i++) if (s.acc[i] > d0 && s.acc[i] < d1) out.push([...s.pts[i], 0]);
    out.push(at(s, d1));
    return out.map((p) => [p[0], p[1]]);
  }

  // one length of thread drawn along a polyline: holes, shadow, the strand, its twist
  function strand(g, line, color, w, R, holes) {
    const d = "M" + line.map((p) => p[0].toFixed(1) + " " + p[1].toFixed(1)).join("L");
    if (holes) for (const p of [line[0], line[line.length - 1]]) {
      g.appendChild(el("circle", { cx: p[0] + 0.6, cy: p[1] + 0.9, r: (w * 0.5).toFixed(1), fill: "rgba(38,33,25,.42)" }));
    }
    g.appendChild(el("path", { d, transform: "translate(1.4 2.4)", stroke: "rgba(38,33,25,.30)", "stroke-width": w + 0.8,
                               fill: "none", "stroke-linecap": "round", "stroke-linejoin": "round", filter: "url(#thr-soft)" }));
    g.appendChild(el("path", { d, stroke: mix(color, -0.28), "stroke-width": w, fill: "none", "stroke-linecap": "round", "stroke-linejoin": "round" }));
    g.appendChild(el("path", { d, stroke: color, "stroke-width": w * 0.68, fill: "none", "stroke-linecap": "round", "stroke-linejoin": "round" }));
    // the twist: short light strokes across the strand at about 55 degrees, one per ply
    let tw = ""; const step = w * 0.95;
    let L = 0; const acc = [0];
    for (let i = 1; i < line.length; i++) { L += Math.hypot(line[i][0] - line[i - 1][0], line[i][1] - line[i - 1][1]); acc.push(L); }
    for (let s = step * 0.6; s < L - step * 0.4; s += step * (0.9 + R() * 0.2)) {
      let i = 1; while (i < acc.length - 1 && acc[i] < s) i++;
      const a = line[i - 1], b = line[i], t = (s - acc[i - 1]) / ((acc[i] - acc[i - 1]) || 1);
      const x = a[0] + (b[0] - a[0]) * t, y = a[1] + (b[1] - a[1]) * t, ang = Math.atan2(b[1] - a[1], b[0] - a[0]) + 0.95;
      const h = w * 0.36;
      tw += `M${(x - Math.cos(ang) * h).toFixed(1)} ${(y - Math.sin(ang) * h).toFixed(1)}L${(x + Math.cos(ang) * h).toFixed(1)} ${(y + Math.sin(ang) * h).toFixed(1)}`;
    }
    g.appendChild(el("path", { d: tw, stroke: mix(color, 0.42), "stroke-width": (w * 0.26).toFixed(2), "stroke-linecap": "round", opacity: 0.85 }));
  }

  function running(g, s, m, R) {
    const w = m.tw || 5, len = m.len || w * 4.4, gap = m.gap || w * 2.4, color = col(m.c);
    let d = m.offset || gap * 0.5;
    while (d < s.L - 2) {
      const L1 = Math.min(s.L, d + len * (0.86 + R() * 0.28));
      if (L1 - d > w * 1.2) {
        const line = between(s, d, L1).map((p) => [p[0] + (R() - 0.5) * 0.8, p[1] + (R() - 0.5) * 0.8]);
        strand(g, line, color, w, R, true);
      }
      d = L1 + gap * (0.85 + R() * 0.3);
    }
  }

  function knot(g, p, color, w) {
    g.appendChild(el("circle", { cx: p[0] + 1.2, cy: p[1] + 2, r: w * 1.15, fill: "rgba(38,33,25,.3)", filter: "url(#thr-soft)" }));
    g.appendChild(el("circle", { cx: p[0], cy: p[1], r: w * 1.1, fill: mix(color, -0.25) }));
    for (let k = 0; k < 3; k++) {
      const a = k * 2.1;
      g.appendChild(el("path", { d: `M${p[0] + Math.cos(a) * w * 0.7} ${p[1] + Math.sin(a) * w * 0.7}A${w * 0.75} ${w * 0.75} 0 0 1 ${p[0] + Math.cos(a + 1.9) * w * 0.7} ${p[1] + Math.sin(a + 1.9) * w * 0.7}`,
        stroke: mix(color, 0.35), "stroke-width": w * 0.3, fill: "none", "stroke-linecap": "round" }));
    }
  }

  function needle(g, p, ang, w) { // a needle lying along ang, its eye at p (the thread runs through the eye)
    const L = 120, c = Math.cos(ang), s = Math.sin(ang), tip = [p[0] + c * L, p[1] + s * L], back = [p[0] - c * 12, p[1] - s * 12];
    const gr = "thr-steel";
    g.appendChild(el("path", { d: `M${back[0] + 2} ${back[1] + 4}L${tip[0] + 2} ${tip[1] + 4}`, stroke: "rgba(38,33,25,.28)", "stroke-width": 5, "stroke-linecap": "round", filter: "url(#thr-soft)" }));
    const n = [-s, c], hw = 2.6;
    const body = `M${back[0] + n[0] * hw} ${back[1] + n[1] * hw}L${tip[0] - c * 30 + n[0] * hw * 0.8} ${tip[1] - s * 30 + n[1] * hw * 0.8}L${tip[0]} ${tip[1]}L${tip[0] - c * 30 - n[0] * hw * 0.8} ${tip[1] - s * 30 - n[1] * hw * 0.8}L${back[0] - n[0] * hw} ${back[1] - n[1] * hw}Z`;
    g.appendChild(el("path", { d: body, fill: `url(#${gr})` }));
    g.appendChild(el("path", { d: `M${p[0] - c * 7} ${p[1] - s * 7}L${p[0] + c * 9} ${p[1] + s * 9}`, stroke: "#4a4740", "stroke-width": 1.6, "stroke-linecap": "round" }));
    g.appendChild(el("path", { d: `M${back[0] + n[0] * 1.1} ${back[1] + n[1] * 1.1}L${tip[0] - c * 34 + n[0] * 1.1} ${tip[1] - s * 34 + n[1] * 1.1}`, stroke: "rgba(255,255,255,.75)", "stroke-width": 0.9 }));
  }

  function pin(g, m) {
    const ang = ((m.a ?? 35) * Math.PI) / 180, c = Math.cos(ang), s = Math.sin(ang), p = [m.x, m.y], color = col(m.c || "rust");
    const r = m.r || 12, vis = m.vis || 26, hid = m.hid || 34, tipL = m.tip ?? 18;
    const head = [p[0] - c * vis, p[1] - s * vis], out1 = [p[0] + c * hid, p[1] + s * hid], tip = [out1[0] + c * tipL, out1[1] + s * tipL];
    const id = "thr-pin" + Math.round(m.x) + "-" + Math.round(m.y);
    const defs = g.ownerSVGElement.querySelector("defs");
    const rg = el("radialGradient", { id, cx: "35%", cy: "30%", r: "70%" });
    [[0, mix(color, 0.7)], [0.28, mix(color, 0.12)], [0.75, color], [1, mix(color, -0.45)]].forEach(([o, sc]) => rg.appendChild(el("stop", { offset: o, "stop-color": sc })));
    defs.appendChild(rg);
    // tip: 0 for a pin pushed into the board behind (no tip comes back out)
    for (const q of tipL > 0 ? [p, out1] : [p]) g.appendChild(el("circle", { cx: q[0] + 0.5, cy: q[1] + 0.8, r: 2.2, fill: "rgba(38,33,25,.45)" }));
    if (tipL > 0) {
      g.appendChild(el("path", { d: `M${out1[0] + 1.5} ${out1[1] + 3}L${tip[0] + 1.5} ${tip[1] + 3}`, stroke: "rgba(38,33,25,.25)", "stroke-width": 2.4, "stroke-linecap": "round", filter: "url(#thr-soft)" }));
      g.appendChild(el("path", { d: `M${out1[0]} ${out1[1]}L${tip[0]} ${tip[1]}`, stroke: "#9a9b9d", "stroke-width": 2, "stroke-linecap": "round" }));
    }
    g.appendChild(el("path", { d: `M${head[0] + 2} ${head[1] + 5}L${p[0] + 2} ${p[1] + 5}`, stroke: "rgba(38,33,25,.3)", "stroke-width": 2.8, "stroke-linecap": "round", filter: "url(#thr-soft)" }));
    g.appendChild(el("path", { d: `M${head[0]} ${head[1]}L${p[0]} ${p[1]}`, stroke: "#8e9093", "stroke-width": 2.4, "stroke-linecap": "round" }));
    g.appendChild(el("path", { d: `M${head[0]} ${head[1] - 0.8}L${p[0]} ${p[1] - 0.8}`, stroke: "#e8e9eb", "stroke-width": 0.8 }));
    g.appendChild(el("ellipse", { cx: head[0] + 3, cy: head[1] + 7, rx: r * 1.05, ry: r * 0.8, fill: "rgba(38,33,25,.32)", filter: "url(#thr-soft2)" }));
    g.appendChild(el("circle", { cx: head[0], cy: head[1], r, fill: `url(#${id})` }));
  }

  function draw(svg, marks) {
    const defs = el("defs", {});
    defs.innerHTML = `<filter id="thr-soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="1.1"/></filter>
      <filter id="thr-soft2" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="3"/></filter>
      <linearGradient id="thr-steel" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4f4f5"/><stop offset=".45" stop-color="#b9bbbe"/><stop offset="1" stop-color="#6f7174"/></linearGradient>`;
    svg.appendChild(defs);
    marks.forEach((m, i) => {
      const R = rand((m.seed || 11) * 97 + i * 13), g = el("g", {}), w = m.tw || 5, color = col(m.c);
      svg.appendChild(g);
      if (m.k === "pin") return pin(g, m);
      if (m.k === "tack") {
        const s = m.s || 16, x = m.x, y = m.y;
        strand(g, [[x - s / 2, y + s / 2], [x + s / 2, y - s / 2]], mix(color, -0.1), w, R, true);
        strand(g, [[x - s / 2, y - s / 2], [x + s / 2, y + s / 2]], color, w, R, true);
        return;
      }
      if (m.k === "strike") return strand(g, m.d, color, w, R, true);
      let s;
      if (m.k === "loop") {
        const pts = [], n = 10, rot = ((m.rot || -4) * Math.PI) / 180;
        for (let j = 0; j < n; j++) {
          const t = (j / n) * Math.PI * 2, j1 = 1 + (R() - 0.5) * 0.05;
          const x = (m.w / 2) * Math.cos(t) * j1, y = (m.h / 2) * Math.sin(t) * j1;
          pts.push([m.x + x * Math.cos(rot) - y * Math.sin(rot), m.y + x * Math.sin(rot) + y * Math.cos(rot)]);
        }
        s = sample(pts, true);
      } else s = sample(m.d, false);
      if (m.k === "lay") strand(g, s.pts, color, w, R, false);
      else running(g, s, m, R);
      if (m.k === "arrow") {
        const [x, y, a] = at(s, s.L), L = (m.head || 30);
        for (const k of [-1, 1]) {
          const b = a + Math.PI + k * 0.55;
          strand(g, [[x + Math.cos(b) * L, y + Math.sin(b) * L], [x, y]], color, w, R, true);
        }
      }
      if (m.knot) knot(g, s.pts[0], color, w);
      if (m.needle) { const [x, y, a] = at(s, s.L); needle(g, [x, y], a, w); }
    });
  }

  // marks in a slide's 1920x1080 space, or in any element's own box (they turn with it): data-thread on either
  function marksOn(node) {
    const marks = JSON.parse(node.dataset.thread || "[]");
    if (!marks.length) return;
    const isSlide = node.classList.contains("slide"), W = isSlide ? 1920 : node.offsetWidth, H = isSlide ? 1080 : node.offsetHeight;
    const svg = el("svg", { class: "thread", viewBox: `0 0 ${W} ${H}`, width: W, height: H,
      style: `position:absolute;left:0;top:0;z-index:${isSlide ? 46 : 5};pointer-events:none;overflow:visible` });
    node.appendChild(svg);
    draw(svg, marks);
  }

  function overlay(node) { // an svg over an element's own box, with the soft-shadow filter, for the decorators below
    const W = node.offsetWidth, H = node.offsetHeight;
    const svg = el("svg", { viewBox: `0 0 ${W} ${H}`, width: W, height: H,
      style: "position:absolute;left:0;top:0;pointer-events:none;overflow:visible;z-index:5" });
    node.appendChild(svg);
    svg.appendChild(el("defs", {})).innerHTML = `<filter id="thr-soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="1.1"/></filter>`;
    const g = el("g", {}); svg.appendChild(g);
    return [g, W, H];
  }

  // a woven label sewn down at both ends: data-tack="colour"
  function tack(node) {
    const [g, W, H] = overlay(node), R = rand(W * 3 + H), color = col(node.dataset.tack), w = +(node.dataset.tackW || 3.4);
    for (const x of [W * 0.06 + 4, W * 0.94 - 4]) for (const dx of [-3.5, 3.5])
      strand(g, [[x + dx + (R() - 0.5) * 2, H * 0.2], [x + dx + (R() - 0.5) * 2, H * 0.8]], color, w, R, true);
  }

  // a hem: running stitch along the bottom edge of a band of cloth, data-hem="colour" (data-hem-inset, default 26)
  function hem(node) {
    const [g, W, H] = overlay(node), k = +(node.dataset.hemInset || 26), R = rand(W + k);
    running(g, sample([[-10, H - k], [W * 0.5, H - k - 3], [W + 10, H - k + 1]], false),
            { c: node.dataset.hem, tw: +(node.dataset.hemW || 5), len: 30, gap: 16 }, R);
  }

  function sew(node) { // running stitch round the inside of a print, turning with it
    const W = node.offsetWidth, H = node.offsetHeight, k = +(node.dataset.sewInset || 12);
    const svg = el("svg", { class: "sewn", viewBox: `0 0 ${W} ${H}`, width: W, height: H,
      style: "position:absolute;left:0;top:0;pointer-events:none;overflow:visible;z-index:2" });
    node.appendChild(svg);
    const m = { k: "run", c: node.dataset.sew, tw: +(node.dataset.sewW || 4), len: +(node.dataset.sewLen || 17), gap: +(node.dataset.sewGap || 10), seed: W + H };
    const pts = [[k, k], [W - k, k], [W - k, H - k], [k, H - k], [k, k]];
    const defs = el("defs", {}); svg.appendChild(defs);
    defs.innerHTML = `<filter id="thr-soft" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="1.1"/></filter>`;
    const g = el("g", {}); svg.appendChild(g);
    const R = rand(m.seed);
    for (let i = 0; i < 4; i++) running(g, sample([pts[i], pts[i + 1]], false), { ...m, offset: 3 }, R);
  }

  /* The camera in an embroidery hoop: <div class="cam round" data-hoop> (data-hoop-t: ring width, default 4.2% of
     the diameter). A wooden ring with its grain running round it, the inner ring beside it, the brass clasp and
     screw at the top. Drawn as a sibling of the camera so the camera's round clip does not cut it. */
  function hoop(cam) {
    const D = cam.offsetWidth, T = +(cam.dataset.hoopT || Math.max(16, D * 0.042)), pad = T * 3;
    const S = D + pad * 2, c = S / 2, r = D / 2 + T * 0.32, R = rand(D);
    const svg = el("svg", { class: "hoop", width: S, height: S, viewBox: `0 0 ${S} ${S}`,
      style: `position:absolute;left:${cam.offsetLeft - pad}px;top:${cam.offsetTop - pad}px;z-index:${(+getComputedStyle(cam).zIndex || 40) + 1};pointer-events:none;overflow:visible` });
    cam.parentNode.insertBefore(svg, cam.nextSibling);
    const id = "hp" + Math.round(cam.offsetLeft) + "x" + Math.round(cam.offsetTop);
    svg.innerHTML = `<defs>
      <linearGradient id="${id}w" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#EBCB9E"/><stop offset=".5" stop-color="#D7AE7C"/><stop offset="1" stop-color="#B98A57"/></linearGradient>
      <linearGradient id="${id}b" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FBE7A6"/><stop offset=".35" stop-color="#D9B158"/><stop offset=".7" stop-color="#A9822F"/><stop offset="1" stop-color="#6E531C"/></linearGradient>
      <linearGradient id="${id}s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFF3C8"/><stop offset=".5" stop-color="#C9A04A"/><stop offset="1" stop-color="#7A5C1E"/></linearGradient>
      <filter id="${id}f" x="-10%" y="-10%" width="120%" height="120%"><feGaussianBlur stdDeviation="${(T * 0.45).toFixed(1)}"/></filter>
      <filter id="${id}g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="1.2"/></filter></defs>`;
    const g = el("g", {}); svg.appendChild(g);
    const ring = (rr, w, stroke, extra = {}) => g.appendChild(el("circle", { cx: c, cy: c, r: rr, fill: "none", stroke, "stroke-width": w, ...extra }));
    // shadow on the page, then the inner ring peeking inside the outer one
    ring(r + T * 0.2, T * 1.15, "rgba(38,33,25,.30)", { transform: `translate(${T * 0.25} ${T * 0.55})`, filter: `url(#${id}f)` });
    ring(r - T * 0.62, T * 0.42, `url(#${id}w)`);
    ring(r - T * 0.4, 1.4, "rgba(70,45,20,.55)");
    // the outer ring, split at the top for the clasp
    const gapA = 0.075, a0 = -Math.PI / 2 + gapA, a1 = -Math.PI / 2 - gapA + Math.PI * 2;
    const arc = (rr) => `M${c + rr * Math.cos(a0)} ${c + rr * Math.sin(a0)}A${rr} ${rr} 0 1 1 ${c + rr * Math.cos(a1)} ${c + rr * Math.sin(a1)}`;
    g.appendChild(el("path", { d: arc(r), fill: "none", stroke: `url(#${id}w)`, "stroke-width": T, "stroke-linecap": "butt" }));
    // grain: thin dashed arcs running round the ring
    for (let k = 0; k < 9; k++) {
      const rr = r - T * 0.42 + (T * 0.84 * (k + 0.5)) / 9, dash = [];
      for (let j = 0; j < 14; j++) dash.push((20 + R() * 160).toFixed(0), (4 + R() * 40).toFixed(0));
      g.appendChild(el("path", { d: arc(rr), fill: "none", stroke: k % 3 ? "rgba(140,92,48,.20)" : "rgba(120,78,38,.32)",
        "stroke-width": (0.6 + R() * 1.1).toFixed(2), "stroke-dasharray": dash.join(" "), "stroke-dashoffset": (R() * 300).toFixed(0) }));
    }
    g.appendChild(el("path", { d: arc(r + T * 0.5 - 0.8), fill: "none", stroke: "rgba(90,58,26,.55)", "stroke-width": 1.4 }));
    g.appendChild(el("path", { d: arc(r - T * 0.5 + 0.8), fill: "none", stroke: "rgba(90,58,26,.45)", "stroke-width": 1.2 }));
    g.appendChild(el("path", { d: arc(r + T * 0.3), fill: "none", stroke: "rgba(255,248,232,.55)", "stroke-width": T * 0.12,
      "stroke-dasharray": `${(Math.PI * r * 0.7).toFixed(0)} ${(Math.PI * r * 2).toFixed(0)}`, "stroke-dashoffset": `${(Math.PI * r * 1.15).toFixed(0)}` }));
    // the clasp: two brass ears either side of the split, a screw through them, a knurled nut on the right
    const top = c - r, ew = T * 0.95, eh = T * 1.55, gx = r * Math.sin(gapA);
    for (const sx of [-1, 1]) {
      const x = c + sx * (gx + ew * 0.5) - ew / 2;
      g.appendChild(el("rect", { x: x + 1.5, y: top - eh * 0.62 + 3, width: ew, height: eh, rx: T * 0.18, fill: "rgba(38,33,25,.28)", filter: `url(#${id}g)` }));
      g.appendChild(el("rect", { x, y: top - eh * 0.62, width: ew, height: eh, rx: T * 0.18, fill: `url(#${id}b)` }));
      g.appendChild(el("rect", { x: x + ew * 0.18, y: top - eh * 0.57, width: ew * 0.22, height: eh * 0.9, rx: ew * 0.1, fill: "rgba(255,250,220,.45)" }));
    }
    const sy = top - eh * 0.2, sl = gx + ew * 2.6, sh = T * 0.42;
    g.appendChild(el("rect", { x: c - sl, y: sy - sh / 2, width: sl * 2, height: sh, rx: sh / 2, fill: `url(#${id}s)` }));
    let thr = ""; for (let x = c - sl + 3; x < c + sl - 2; x += sh * 0.42) thr += `M${x} ${sy - sh / 2 + 0.6}l${sh * 0.3} ${sh - 1.2}`;
    g.appendChild(el("path", { d: thr, stroke: "rgba(90,66,20,.55)", "stroke-width": 0.9 }));
    const nx = c + sl - T * 0.1, nh = T * 1.05, nw = T * 0.75;
    g.appendChild(el("rect", { x: nx, y: sy - nh / 2, width: nw, height: nh, rx: T * 0.14, fill: `url(#${id}b)` }));
    let kn = ""; for (let y = sy - nh / 2 + 2; y < sy + nh / 2 - 1; y += 2.6) kn += `M${nx + 1.5} ${y}h${nw - 3}`;
    g.appendChild(el("path", { d: kn, stroke: "rgba(80,58,18,.45)", "stroke-width": 0.9 }));
  }

  window.addEventListener("load", () => {
    document.querySelectorAll("[data-hoop]").forEach(hoop);
    document.querySelectorAll("[data-sew]").forEach(sew);
    document.querySelectorAll("[data-tack]").forEach(tack);
    document.querySelectorAll("[data-hem]").forEach(hem);
    document.querySelectorAll("[data-thread]").forEach(marksOn);
    document.body.dataset.threaded = "1";
  });
})();
