// Hand marks for every slide: circles, underlines, arrows, boxes drawn with rough.js so they wobble like
// an iPad pen, not like vector shapes. A slide lists its marks in data-ink (JSON), in 1920x1080 coordinates:
//   [{"k":"ellipse","x":960,"y":540,"w":400,"h":120,"c":"rust"}, {"k":"arrow","d":[[x1,y1],[x2,y2],[x3,y3]]}, ...]
// k: ellipse | line | arrow (a curve through the points, with a head) | box | scribble (cross-out) | under (underline)
// Also: Olivera has no punctuation, so apostrophes and quotes in .display get a tighter fallback glyph.
(function () {
  const COLORS = { rust: "#B06A4A", olive: "#6F7452", ink: "#262119", wheat: "#C89B4B", paper: "#FBFAF6" };
  const NS = "http://www.w3.org/2000/svg";

  function head(rc, svg, p, q, o) {
    const a = Math.atan2(q[1] - p[1], q[0] - p[0]), L = 26 * (o.size || 1);
    for (const s of [-1, 1]) {
      const b = a + Math.PI + s * 0.5;
      svg.appendChild(rc.line(q[0], q[1], q[0] + L * Math.cos(b), q[1] + L * Math.sin(b), o));
    }
  }

  function draw(slide) {
    const marks = JSON.parse(slide.dataset.ink || "[]");
    if (!marks.length) return;
    const svg = document.createElementNS(NS, "svg");
    svg.setAttribute("class", "ink");
    svg.setAttribute("viewBox", "0 0 1920 1080");
    slide.appendChild(svg);
    const rc = rough.svg(svg);
    marks.forEach((m, i) => {
      const o = { stroke: COLORS[m.c] || m.c || COLORS.rust, strokeWidth: m.sw || 4.2, roughness: m.r ?? 1.4,
                  bowing: m.b ?? 1.2, seed: m.seed || 7 + i, disableMultiStroke: m.single || false };
      if (m.k === "ellipse") svg.appendChild(rc.ellipse(m.x, m.y, m.w, m.h, o));
      if (m.k === "box") svg.appendChild(rc.rectangle(m.x, m.y, m.w, m.h, { ...o, strokeLineDash: m.dash || undefined }));
      if (m.k === "line") svg.appendChild(rc.line(m.d[0][0], m.d[0][1], m.d[1][0], m.d[1][1], o));
      if (m.k === "under") svg.appendChild(rc.curve([[m.x, m.y], [m.x + m.w * 0.5, m.y + 6], [m.x + m.w, m.y - 3]], o));
      if (m.k === "arrow") {
        svg.appendChild(rc.curve(m.d, { ...o, disableMultiStroke: true }));
        head(rc, svg, m.d[m.d.length - 2], m.d[m.d.length - 1], { ...o, disableMultiStroke: true });
      }
      if (m.k === "scribble") {
        const pts = []; const n = m.n || 7;
        for (let j = 0; j <= n; j++) pts.push([m.x + (m.w * j) / n, m.y + (j % 2 ? m.h : 0)]);
        svg.appendChild(rc.curve(pts, { ...o, roughness: 1.8 }));
      }
    });
  }

  function punctuation(el) {
    el.querySelectorAll(".display, .ol, .sc").forEach((d) => {
      const walk = (node) => {
        if (node.nodeType === 3 && /[’'“”"?!,.:]/.test(node.nodeValue)) {
          const frag = document.createDocumentFragment();
          node.nodeValue.split(/([’'“”"?!,.:])/).forEach((part) => {
            if (!part) return;
            if (/^[’'“”"?!,.:]$/.test(part)) {
              const s = document.createElement("span");
              s.className = part === "’" || part === "'" ? "ap" : "pn";
              s.textContent = part === "'" ? "’" : part;
              frag.appendChild(s);
            } else frag.appendChild(document.createTextNode(part));
          });
          node.replaceWith(frag);
        } else if (node.nodeType === 1) [...node.childNodes].forEach(walk);
      };
      [...d.childNodes].forEach(walk);
    });
  }

  window.addEventListener("load", () => {
    document.querySelectorAll(".slide").forEach((s) => { punctuation(s); draw(s); });
    document.body.dataset.inked = "1";
  });
})();
