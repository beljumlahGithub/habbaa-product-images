// usage in an amazon.sa tab: (0,eval)(await (await fetch(RAW+'b12/extract.js')).text()); await X12(['ASIN',...]) -> renders JSON into <pre id=dd>
window.X12 = async (L) => {
  const D = {};
  const one = async a => {
    const h = await (await fetch('/dp/' + a + '?language=en_AE&th=1&psc=1')).text();
    const d = new DOMParser().parseFromString(h, 'text/html');
    const T = s => ((d.querySelector(s) || {}).textContent || '').replace(/\s+/g, ' ').trim();
    const bl = [...d.querySelectorAll('#feature-bullets li span.a-list-item')].map(e => e.textContent.replace(/\s+/g, ' ').trim()).filter(Boolean);
    const tb = [...d.querySelectorAll('#productDetails_techSpec_section_1 tr,#productDetails_detailBullets_sections1 tr,#productOverview_feature_div tr,#detailBullets_feature_div li')]
      .map(e => e.textContent.replace(/\s+/g, ' ').trim()).filter(x => !/Customer Reviews|Best Sellers|ASIN|Date First|Manufacturer/.test(x));
    let im = [...h.matchAll(/"(?:hiRes|large)":"https:\/\/m\.media-amazon\.com\/images\/I\/([A-Za-z0-9+%-]+)\./g)].map(m => m[1]);
    const lm = d.querySelector('#landingImage');
    if (lm) { const m = (lm.getAttribute('data-old-hires') || lm.src || '').match(/images\/I\/([A-Za-z0-9+%-]+)\./); if (m) im.unshift(m[1]); }
    D[a] = { t: T('#productTitle'), bl, de: T('#productDescription').slice(0, 1500), tb: tb.join(' | ').slice(0, 900), im: [...new Set(im)].slice(0, 7) };
  };
  for (let i = 0; i < L.length; i += 10) await Promise.all(L.slice(i, i + 10).map(a => one(a).catch(e => D[a] = { err: String(e) })));
  window.__X12 = D;
  document.body.innerHTML = '<pre id="dd" style="white-space:pre-wrap"></pre>';
  document.getElementById('dd').textContent = JSON.stringify(D);
  return JSON.stringify(D).length;
};
// grid of photos for visual check: await G12(['ASIN',...], 3)  (first n images each)
window.G12 = async (L, n) => {
  const D = window.__X12 || {};
  document.body.innerHTML = '';
  const g = document.createElement('div');
  g.style.cssText = 'display:grid;grid-template-columns:repeat(4,370px);gap:4px;background:#fff';
  L.forEach((a, i) => {
    const c = document.createElement('div');
    c.style.cssText = 'font:12px Arial;text-align:center';
    c.innerHTML = ((D[a] || {}).im || []).slice(0, n || 3).map(m => '<img src="https://m.media-amazon.com/images/I/' + m + '._SL400_.jpg" style="width:120px;height:120px;object-fit:contain">').join('') + '<br>' + (i + 1) + ' ' + a;
    g.appendChild(c);
  });
  document.body.appendChild(g);
  await new Promise(r => setTimeout(r, 4000));
  return 'ok';
};
