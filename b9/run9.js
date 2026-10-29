// Batch 9 runner: loads each listing editor in an iframe, rewrites text (HB.rewrite) and optionally uploads images, then submits.
(() => {
  const R = window.R9 = window.R9 || {};
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  R.log = R.log || {};
  R.save = () => { try { localStorage.__r9 = JSON.stringify(R.log) } catch (e) {} };
  try { Object.assign(R.log, JSON.parse(localStorage.__r9 || '{}')) } catch (e) {}
  R.frame = () => {
    let f = document.getElementById('__r9f');
    if (f) f.remove();
    f = document.createElement('iframe'); f.id = '__r9f';
    f.style.cssText = 'position:fixed;left:0;top:0;width:1400px;height:900px;z-index:99999;background:#fff';
    document.body.appendChild(f); return f;
  };
  R.open = async (sku, asin) => {
    const f = R.frame();
    f.src = '/interactive/listing/workflow/edit/description?sku=' + encodeURIComponent(sku) + '&asin=' + asin;
    await new Promise(r => { f.onload = r; setTimeout(r, 40000) });
    const w = f.contentWindow;
    for (let i = 0; i < 40; i++) { await sleep(500); try { if (w.document.querySelector('kat-button,button')) break } catch (e) {} }
    await sleep(4000);
    w.eval(R.hbsrc);
    w.HB.C = { [asin]: R.C[asin] };
    return w;
  };
  R.findBtn = (H) => H.find(e => e.tagName === 'KAT-BUTTON' && /^\s*Submit( Edits)?\s*$/.test(e.textContent) );
  R.submit = async (w) => {
    const H = w.HB; H.hook(); H.res = null;
    let btn = null;
    for (let i = 0; i < 40; i++) { btn = R.findBtn(H); if (btn && !btn.hasAttribute('disabled')) break; await sleep(500) }
    if (!btn) return 'nobtn';
    if (btn.hasAttribute('disabled')) {
      const ta = H.find(e => e.tagName === 'TEXTAREA');
      if (ta) { ta.focus(); ta.value = ta.value + ' '; ta.dispatchEvent(new w.Event('input', { bubbles: true, composed: true })); ta.dispatchEvent(new w.Event('change', { bubbles: true, composed: true })) }
      await sleep(1500); btn = R.findBtn(H);
      if (!btn || btn.hasAttribute('disabled')) return 'disabled';
    }
    (btn.shadowRoot && btn.shadowRoot.querySelector('button') || btn).click();
    for (let i = 0; i < 60 && !H.res; i++) await sleep(500);
    const r = H.res;
    return r ? (/"status":"SUCCESS"/.test(r) ? 'SUCCESS:' + (H.LG || '') : 'ERR:' + r.slice(0, 400)) : 'noresp';
  };
  R.one = async (asin, sku, imgUrls) => {
    try {
      const w = await R.open(sku, asin);
      let up = '';
      if (imgUrls && imgUrls.length) {
        const H = w.HB;
        const n0 = H.imgCount();
        const need = Math.max(0, 7 - n0);
        const list = imgUrls.slice(0, need);
        let inp = null;
        for (let i = 0; i < 40 && !inp; i++) { await sleep(500); inp = H.find(e => e.tagName === 'INPUT' && e.type === 'file' && e.multiple && /image/.test(e.accept)) }
        let ok = 0;
        if (inp && list.length) {
          for (const u of list) {
            const b = await fetch(u).then(r => r.blob());
            const f = new w.File([b], asin + '-' + Date.now() + '.jpg', { type: 'image/jpeg', lastModified: Date.now() });
            const before = H.newImgs();
            const dt = new w.DataTransfer(); dt.items.add(f); inp.files = dt.files;
            inp.dispatchEvent(new w.Event('change', { bubbles: true, composed: true }));
            for (let i = 0; i < 40 && H.newImgs() <= before; i++) await sleep(500);
            if (H.newImgs() > before) ok++;
            await sleep(1200);
          }
          await sleep(2500);
        }
        up = ' img0=' + n0 + ' up=' + ok + '/' + list.length + (inp ? '' : ' noinput');
      }
      const r = await R.submit(w);
      R.log[asin] = r + up; R.save();
      return R.log[asin];
    } catch (e) { R.log[asin] = 'EXC:' + e; R.save(); return R.log[asin] }
  };
  R.run = async (jobs) => {
    R.busy = 1;
    for (const j of jobs) {
      if (R.stop) break;
      if (R.log[j.a] && /^SUCCESS/.test(R.log[j.a]) && !j.force) continue;
      R.cur = j.a; await R.one(j.a, j.sku, j.imgs);
    }
    R.busy = 0; R.cur = null;
  };
})();
'run9 loaded';
