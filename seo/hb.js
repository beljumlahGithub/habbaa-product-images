// HABBAA Seller Central listing editor helpers. Load: eval(await (await fetch(RAW+'seo/hb.js')).text())
(() => {
  const M = '338811';
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  const find = pred => { let el = null; const walk = root => { for (const e of root.querySelectorAll('*')) { if (pred(e)) { el = e; return } if (e.shadowRoot) { walk(e.shadowRoot); if (el) return } } }; walk(document); return el };
  const findAll = pred => { const out = []; const walk = root => { for (const e of root.querySelectorAll('*')) { if (pred(e)) out.push(e); if (e.shadowRoot) walk(e.shadowRoot) } }; walk(document); return out };
  const HB = window.HB = window.HB || {};
  HB.sleep = sleep; HB.find = find; HB.findAll = findAll;
  HB.asin = () => new URLSearchParams(location.search).get('asin');

  HB.rewrite = (body) => {
    const C = HB.C; const asin = HB.asin(); const c = C && C[asin];
    const kv = new URLSearchParams(body);
    if (!c || HB.textOff) { HB.lastBody = kv.toString(); return kv.toString() }
    for (const k of [...kv.keys()]) if (/^(item_name|bullet_point|product_description|generic_keyword)#\d+\./.test(k)) kv.delete(k);
    const LG = kv.get('listingLanguageCode') || 'ar_AE'; const x = LG.startsWith('en') ? c.en : c.ar; HB.LG = LG;
    const add = (k, i, v) => { kv.set(k + '#' + i + '.value', v); kv.set(k + '#' + i + '.language_tag', LG); kv.set(k + '#' + i + '.marketplace_id', M) };
    add('item_name', 1, x.t); add('product_description', 1, x.d); add('generic_keyword', 1, x.k);
    x.b.forEach((b, i) => add('bullet_point', 1 + i, b));
    ['item_name', 'product_description', 'generic_keyword'].forEach(k => add(k, 2, ''));
    for (let i = 6; i <= 10; i++) add('bullet_point', i, '');
    HB.lastBody = kv.toString(); return kv.toString();
  };

  HB.hook = () => {
    if (window.__hbHooked) return; window.__hbHooked = 1;
    const os = XMLHttpRequest.prototype.send, oo = XMLHttpRequest.prototype.open;
    XMLHttpRequest.prototype.open = function (m, u) { this.__u = u; return oo.apply(this, arguments) };
    XMLHttpRequest.prototype.send = function (b) {
      if (/abis\/ajax\/edit$/.test(String(this.__u).split('?')[0]) && typeof b === 'string') { b = HB.rewrite(b); this.addEventListener('load', () => { HB.res = this.responseText }) }
      return os.call(this, b)
    };
    const of = window.fetch;
    window.fetch = async function (u, o) {
      const url = typeof u === 'string' ? u : u.url;
      if (/abis\/ajax\/edit$/.test(url.split('?')[0]) && o && typeof o.body === 'string') { o.body = HB.rewrite(o.body); const r = await of.call(this, u, o); r.clone().text().then(t => HB.res = t); return r }
      return of.apply(this, arguments)
    };
  };

  HB.submit = async () => {
    HB.hook(); HB.res = null;
    let btn = null;
    for (let i = 0; i < 60; i++) { await sleep(500); btn = find(e => e.tagName === 'KAT-BUTTON' && /Submit Edits/.test(e.textContent) && !e.hasAttribute('disabled')); if (btn) break }
    if (!btn) return 'nobtn';
    (btn.shadowRoot && btn.shadowRoot.querySelector('button') || btn).click();
    for (let i = 0; i < 60 && !HB.res; i++) await sleep(500);
    return HB.res ? (/"status":"SUCCESS"/.test(HB.res) ? 'SUCCESS' : HB.res.slice(0, 300)) : 'noresp';
  };

  HB.newImgs = () => findAll(e => e.tagName === 'IMG' && /^Image|Main/.test(e.alt || '') && !/media-amazon/.test(e.src) && /cloudfront|DescriptionImages|blob:/.test(e.src)).length;
  HB.imgCount = () => findAll(e => e.tagName === 'IMG' && /^Image|Main/.test(e.alt || '')).length;

  // urls: list of image URLs to append (one by one)
  HB.upload = async (urls) => {
    HB.hook();
    let inp = null;
    for (let i = 0; i < 40 && !inp; i++) { await sleep(500); inp = find(e => e.tagName === 'INPUT' && e.type === 'file' && e.multiple && /image/.test(e.accept)) }
    if (!inp) return 'noinput';
    await sleep(1500);
    const asin = HB.asin(); let ok = 0;
    for (const u of urls) {
      if (HB.imgCount() >= 9) break;
      const b = await fetch(u).then(r => r.blob());
      const f = new File([b], asin + '-' + Date.now() + '.jpg', { type: 'image/jpeg', lastModified: Date.now() });
      const before = HB.newImgs();
      const dt = new DataTransfer(); dt.items.add(f); inp.files = dt.files;
      inp.dispatchEvent(new Event('change', { bubbles: true, composed: true }));
      for (let i = 0; i < 40 && HB.newImgs() <= before; i++) await sleep(500);
      if (HB.newImgs() > before) ok++;
      await sleep(1500);
    }
    await sleep(3000);
    const r = await HB.submit();
    const keys = [...new URLSearchParams(HB.lastBody || '').keys()].filter(k => /ProductImage/.test(k));
    return 'up=' + ok + '/' + urls.length + ' keys=' + keys.join(',') + ' ' + r;
  };
})();
'hb loaded';
