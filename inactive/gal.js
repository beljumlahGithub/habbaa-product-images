window.__G = window.__G || {};
(() => {
  const S = 2000, BG = '#F7F5F1', INK = '#1E2126', SUB = '#62666E', ACC = '#B08D57', PANEL = '#FFFFFF';
  const G = window.__G;
  G.short = (t) => {
    t = String(t || '').replace(/^\s*(HABBAA|هبة)\s*/i, '').replace(/^\s*(HABBAA|هبة)\s*/i, '');
    t = t.split(/[,،–\-|(]/)[0].trim();
    if (t.length > 48) t = t.slice(0, 48).replace(/\s+\S*$/, '');
    return t;
  };
  G.cleanB = (b) => String(b || '').replace(/^(المنتج|Product)\s*:\s*/, '').replace(/\s+/g, ' ').trim();
  const wrap = (x, s, maxw) => {
    const out = []; let cur = '';
    for (const w of s.split(' ')) { const t = (cur + ' ' + w).trim(); if (x.measureText(t).width > maxw && cur) { out.push(cur); cur = w } else cur = t }
    if (cur) out.push(cur); return out;
  };
  const rr = (x, a, b, w, h, r, fill, stroke) => { x.beginPath(); x.roundRect(a, b, w, h, r); if (fill) { x.fillStyle = fill; x.fill() } if (stroke) { x.strokeStyle = stroke; x.lineWidth = 4; x.stroke() } };
  const font = (w, px) => `${w} ${px}px Tajawal, Arial, sans-serif`;
  G.loadImg = async (url) => { const b = await (await fetch(url)).blob(); return await createImageBitmap(b) };
  // contain image into box with white trimming
  G.place = (x, bm, bx, by, bw, bh) => {
    const c = document.createElement('canvas'); c.width = bm.width; c.height = bm.height; const cx = c.getContext('2d'); cx.fillStyle = '#fff'; cx.fillRect(0, 0, c.width, c.height); cx.drawImage(bm, 0, 0);
    const d = cx.getImageData(0, 0, c.width, c.height).data; let x0 = c.width, y0 = c.height, x1 = 0, y1 = 0;
    for (let y = 0; y < c.height; y += 3) for (let i = 0; i < c.width; i += 3) { const k = (y * c.width + i) * 4; if (Math.min(d[k], d[k + 1], d[k + 2]) < 236) { if (i < x0) x0 = i; if (i > x1) x1 = i; if (y < y0) y0 = y; if (y > y1) y1 = y } }
    if (x1 <= x0 || y1 <= y0) { x0 = 0; y0 = 0; x1 = c.width - 1; y1 = c.height - 1 }
    const cw = x1 - x0 + 1, ch = y1 - y0 + 1; const r = Math.min(bw / cw, bh / ch); const w = cw * r, h = ch * r;
    x.imageSmoothingQuality = 'high'; x.drawImage(c, x0, y0, cw, ch, bx + (bw - w) / 2, by + (bh - h) / 2, w, h);
  };
  const header = (x, rtl, head, sub) => {
    x.direction = rtl ? 'rtl' : 'ltr'; x.textAlign = rtl ? 'right' : 'left'; const X = rtl ? S - 80 : 80;
    x.fillStyle = ACC; x.font = font(700, 34); x.fillText('HABBAA', X, 95);
    x.fillStyle = INK; x.font = font(800, 92); x.fillText(head, X, 200);
    x.fillStyle = SUB; x.font = font(400, 46); x.fillText(sub, X, 270);
    x.fillStyle = ACC; x.fillRect(rtl ? S - 80 - 160 : 80, 300, 160, 8);
  };
  const canvas = () => { const c = document.createElement('canvas'); c.width = S; c.height = S; const x = c.getContext('2d'); x.fillStyle = BG; x.fillRect(0, 0, S, S); return [c, x] };
  const toBlob = (c) => new Promise(z => c.toBlob(z, 'image/jpeg', 0.92));
  G.features = async (bm, rtl, sub, bullets) => {
    const [c, x] = canvas(); header(x, rtl, rtl ? 'المميزات الرئيسية' : 'Key Features', sub);
    rr(x, 70, 340, S - 140, 760, 44, PANEL); G.place(x, bm, 130, 380, S - 260, 680);
    const B = bullets.slice(0, 4); const tw = (S - 140 - 40) / 2, th = 400;
    B.forEach((b, i) => {
      const col = i % 2, row = Math.floor(i / 2);
      const bx = rtl ? (S - 70 - tw - col * (tw + 40)) : (70 + col * (tw + 40)); const by = 1140 + row * (th + 30);
      rr(x, bx, by, tw, th, 36, PANEL);
      const cxp = rtl ? bx + tw - 70 : bx + 70; x.beginPath(); x.arc(cxp, by + 70, 34, 0, Math.PI * 2); x.fillStyle = ACC; x.fill();
      x.fillStyle = '#fff'; x.font = font(800, 40); x.textAlign = 'center'; x.direction = 'ltr'; x.fillText(String(i + 1), cxp, by + 84);
      x.direction = rtl ? 'rtl' : 'ltr'; x.textAlign = rtl ? 'right' : 'left'; x.fillStyle = INK; x.font = font(700, 40);
      const lines = wrap(x, b, tw - 90); const X = rtl ? bx + tw - 45 : bx + 45; let y = by + 165;
      lines.slice(0, 5).forEach((l, k) => { x.fillText(k == 4 && lines.length > 5 ? l.replace(/\s*\S+$/, '…') : l, X, y); y += 54 });
    });
    return toBlob(c);
  };
  G.glance = async (bm, rtl, sub, boxLine) => {
    const [c, x] = canvas(); header(x, rtl, rtl ? 'لمحة سريعة' : 'At a Glance', sub);
    rr(x, 70, 340, S - 140, 1240, 44, PANEL); G.place(x, bm, 120, 380, S - 240, 1160);
    if (boxLine) {
      rr(x, 70, 1640, S - 140, 260, 44, null, ACC); x.direction = rtl ? 'rtl' : 'ltr'; x.textAlign = 'center';
      x.fillStyle = ACC; x.font = font(700, 40); x.fillText(rtl ? 'محتويات العبوة' : 'In the box', S / 2, 1730);
      x.fillStyle = INK; x.font = font(800, 58); x.fillText(boxLine, S / 2, 1830);
    }
    return toBlob(c);
  };
  G.details = async (bm, rtl, sub, rows) => {
    const [c, x] = canvas(); header(x, rtl, rtl ? 'التفاصيل' : 'Details', sub);
    rr(x, 70, 340, S - 140, 820, 44, PANEL); G.place(x, bm, 130, 380, S - 260, 740);
    let y = 1210;
    rows.slice(0, 4).forEach(r => {
      x.font = font(700, 40); x.direction = rtl ? 'rtl' : 'ltr'; x.textAlign = rtl ? 'right' : 'left';
      const lines = wrap(x, r, S - 140 - 140).slice(0, 3); const h = 50 + lines.length * 54;
      if (y + h > S - 50) return;
      rr(x, 70, y, S - 140, h, 28, PANEL);
      const dx = rtl ? S - 70 - 50 : 70 + 50; x.beginPath(); x.arc(dx, y + 52, 12, 0, Math.PI * 2); x.fillStyle = ACC; x.fill();
      x.fillStyle = INK; let ly = y + 66; lines.forEach(l => { x.fillText(l, rtl ? S - 70 - 85 : 70 + 85, ly); ly += 54 }); y += h + 22;
    });
    return toBlob(c);
  };
  G.count = (t) => { try { return window.__ucCount ? __ucCount(t) : 0 } catch (e) { return 0 } };
  G.boxLine = (t, rtl) => {
    const m = String(t).match(/(\d+)\s*(حبة|حبات|قطعة|قطع|كيس|أكياس|عبوة|كوب|أكواب|ورقة|شمعة|بالون|بالونة|Pieces|Pcs|Pack|Count|Sheets|Rolls?|Cups?)/i) || String(t).match(/\((\d+)\)\s*$/);
    if (!m) return '';
    const n = m[1]; if (+n < 2 || +n > 5000) return '';
    return rtl ? ('عبوة من ' + n + (m[2] ? ' ' + m[2] : ' قطع')) : ('Pack of ' + n);
  };
  G.make = async (imgUrl, title, bullets, lang) => {
    const rtl = /^ar/.test(lang); const bm = await G.loadImg(imgUrl); const sub = G.short(title); const B = bullets.map(G.cleanB).filter(Boolean);
    if (B.length < 3) throw 'fewbullets';
    const f = await G.features(bm, rtl, sub, B.slice(0, 4));
    const g = await G.glance(bm, rtl, sub, G.boxLine(title, rtl));
    const d = await G.details(bm, rtl, sub, B.slice(Math.min(2, B.length - 3)).slice(0, 4));
    return [f, g, d];
  };
})();
'gal ok';
