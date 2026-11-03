// Batch 13 patch for run10.js: unit_count type fix + double-click retry on noresp
(() => {
  const R = window.R10;
  const sleep = ms => new Promise(r => setTimeout(r, ms));
  R.fixUnit = async (w) => {
    const H = w.HB;
    const dd = H.find(e => e.tagName === 'KAT-DROPDOWN' && /unit_count-0-type-value/.test(e.getAttribute('name') || ''));
    if (!dd) return 'nodd';
    const opts = dd.options || [];
    if (!opts.length) return 'noopts';
    dd.value = opts[0].value;
    dd.dispatchEvent(new w.Event('change', { bubbles: true, composed: true }));
    dd.dispatchEvent(new w.CustomEvent('change', { bubbles: true, composed: true, detail: { value: opts[0].value } }));
    await sleep(1500);
    return 'set:' + opts[0].value;
  };
  if (!R.submit0) R.submit0 = R.submit;
  R.submit = async (w) => {
    let r = await R.submit0(w);
    if (r === 'noresp' || /99022|unit_count/.test(r)) {
      const f = await R.fixUnit(w);
      r = await R.submit0(w);
      if (r === 'noresp') r = await R.submit0(w);
      r = r + ' fix=' + f;
    }
    return r;
  };
})();
'r13 patch loaded';
