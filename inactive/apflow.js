window.__apFlow = window.__apFlow || {};
(() => {
  const F = window.__apFlow;
  const sl = ms => new Promise(r => setTimeout(r, ms));
  const react = (w, el) => { let p = el; for (let i = 0; i < 8 && p; i++, p = p.parentElement) { const k = Object.keys(p).find(k => k.startsWith('__reactEventHandlers') || k.startsWith('__reactProps')); if (k && p[k].onClick) { p[k].onClick({ preventDefault() {}, stopPropagation() {}, target: p, currentTarget: p, nativeEvent: new w.MouseEvent('click'), persist() {} }); return true } } return false };
  F.react = react;
  F.open = async (lang) => {
    const w = window.__f2; w.location.href = '/enhanced-content/content-manager/workflow/ebc-premium/content/new/edit?mons_sel_locale=' + (lang || 'ar_AE');
    for (let i = 0; i < 40; i++) { await sl(1000); try { if (w.document.readyState == 'complete' && w.document.body && /تفاصيل المحتوى|Content details/.test(w.document.body.innerText)) break } catch (e) {} }
    await sl(2500); w.eval(localStorage.__HBH); w.eval(localStorage.__HB2); try { w.eval(localStorage.__WKJS) } catch (e) {}
    return !!w.hb2Name();
  };
  F.addModule = async () => {
    const w = window.__f2;
    const b = w.hbAll('button,kat-button,a,[role=button]').filter(e => e.offsetWidth > 0 && (e.textContent || '').trim() === 'إضافة وحدة').pop(); if (!b) return 'noaddbtn'; b.click(); await sl(1500);
    const s = w.hbAll('input').filter(e => e.offsetWidth > 0 && e.placeholder === 'بحث').pop(); if (!s) return 'nosearch'; w.hbType(s, 'صورة كاملة'); s.dispatchEvent(new w.Event('input', { bubbles: true })); await sl(1500);
    const h = w.hbAll('h6').filter(e => e.textContent.trim() === 'صورة كاملة لنظام Premium' && e.offsetWidth > 0)[0]; if (!h) return 'nomodule';
    const before = w.hbAll('*').filter(e => e.children.length === 0 && /الضغط لإضافة صورة/.test(e.textContent) && e.offsetWidth > 0).length;
    react(w, h); await sl(2000);
    const after = w.hbAll('*').filter(e => e.children.length === 0 && /الضغط لإضافة صورة/.test(e.textContent) && e.offsetWidth > 0).length;
    return after > before ? 'ok' : 'noadd ' + before + '>' + after;
  };
  F.build = async (name, mods) => {
    const w = window.__f2; const log = [];
    w.hbType(w.hb2Name(), name); await sl(500);
    for (const [d, m, alt] of mods) {
      const a = await F.addModule(); log.push('m:' + a); if (a !== 'ok') return log.join(' ');
      const r = await window.__apImg(w, d, m, alt); log.push('i:' + r); if (r !== 'ok') return log.join(' ');
    }
    return log.join(' ');
  };
  F.apply = async (asins) => {
    const w = window.__f2;
    const j = await (await fetch('/aplus/api/ListContentMetadata?filteredContentTypes=')).json(); const cov = new Set(); j.items.forEach(x => (x.asins || []).forEach(a => cov.add(a)));
    const free = asins.filter(a => !cov.has(a)); if (!free.length) return 'nofree';
    const nx = w.hbAll('*').filter(e => e.offsetWidth > 0 && e.children.length <= 2 && e.textContent.trim() === 'التالي: تطبيق أرقام ASIN').pop(); if (!nx) return 'nonext';
    if (!react(w, nx)) nx.click(); await sl(8000);
    const e = w.hbErrors(); if (e.length) return 'ERR ' + JSON.stringify(e).slice(0, 300);
    await w.hbClickText('التحميل المجمع'); await sl(1200);
    const inp = w.hbAll('input').filter(e => e.type === 'file')[0]; if (!inp) return 'nofile';
    const f = new w.File([free.join('\n') + '\n'], 'asins.csv', { type: 'text/csv' }); const dt = new w.DataTransfer(); dt.items.add(f); inp.files = dt.files; inp.dispatchEvent(new w.Event('change', { bubbles: true })); await sl(8000);
    const t = w.document.body.innerText; return 'free ' + free.length + '/' + asins.length + ' | ' + ((t.match(/عدد ASIN المطبق عليها \((\d+)\)/) || [])[1] || '?') + ' errs ' + ((t.match(/خطأ \(/g) || []).length);
  };
  F.review = async () => {
    const w = window.__f2;
    const nx = w.hbAll('*').filter(e => e.offsetWidth > 0 && e.children.length <= 2 && e.textContent.trim() === 'التالي: مراجعة وإرسال').pop(); if (!nx) return 'nonext';
    if (!react(w, nx)) nx.click(); await sl(9000);
    const b = w.hbAll('*').filter(e => e.children.length === 0 && e.textContent.trim() === 'إرسال للموافقة' && e.offsetWidth > 0)[0]; if (!b) return 'nobtn ' + JSON.stringify(w.hbErrors()).slice(0, 200);
    react(w, b); await sl(2500);
    // confirm dialog
    const c = w.hbAll('button,kat-button').filter(e => e.offsetWidth > 0 && /^(إرسال|تأكيد|إرسال للموافقة)$/.test((e.textContent || e.getAttribute('label') || '').trim()));
    const t0 = w.document.body.innerText;
    return 'submitclicked confirms=' + c.length + ' ' + (/بنجاح|successfully/.test(t0) ? 'SUCCESS' : '');
  };
  F.replace = async (idx, d, m, alt) => {
    const w = window.__f2;
    const kbs = w.hbAll('kat-button').filter(e => e.offsetWidth > 0 && /^(تعديل)$/.test((e.textContent || e.getAttribute('label') || '').trim()));
    const kb = kbs[idx]; if (!kb) return 'noedit ' + kbs.length; kb.scrollIntoView({ block: 'center' }); await sl(400);
    (kb.shadowRoot && kb.shadowRoot.querySelector('button') || kb).click(); let As = [];
    for (let i = 0; i < 12 && As.length < 2; i++) { await sl(800); As = [...w.document.querySelectorAll('a')].filter(a => /سحب الصورة/.test(a.textContent) && a.offsetWidth > 0) } if (As.length < 2) return 'nodialog';
    let dlg = As[0]; for (let i = 0; i < 12 && dlg && !/إضافة صورة/.test(dlg.innerText || ''); i++) dlg = dlg.parentElement;
    if (!dlg) return 'nodlg';
    const xs = [...dlg.querySelectorAll('*')].filter(e => e.offsetWidth > 0 && e.offsetWidth < 40 && /^(×|x|X|✕)$/.test((e.textContent || '').trim()) && dlg.contains(e));
    // only the small x on image previews (not the dialog close): those sit inside the image boxes, near the drop links
    const imgX = xs.filter(x => { const r = x.getBoundingClientRect(); return As.some(a => { const q = a.getBoundingClientRect(); return Math.abs(r.top - q.top) < 260 && r.top > q.top - 260 && Math.abs(r.left - q.left) < 900 }) });
    imgX.slice(0, 2).forEach(x => x.click()); await sl(1500);
    const As2 = [...w.document.querySelectorAll('a')].filter(a => /سحب الصورة/.test(a.textContent) && a.offsetWidth > 0);
    const dz = As2.find(a => a.offsetWidth > 500) || As2[0], mz = As2.find(a => a.offsetWidth < 400) || As2[1];
    const drop = (el, b, nm) => { const f = new w.File([b], nm, { type: 'image/jpeg' }); const dt = new w.DataTransfer(); dt.items.add(f); for (const t of ['dragenter', 'dragover', 'drop']) el.dispatchEvent(new w.DragEvent(t, { bubbles: true, cancelable: true, dataTransfer: dt })) };
    drop(dz, d, 'd' + Date.now() + '.jpg'); await sl(700); drop(mz, m, 'm' + Date.now() + '.jpg'); await sl(6500);
    const add = w.hbAll('button,kat-button').filter(x => x.textContent.trim() === 'إضافة' && x.offsetWidth > 0); if (!add.length) return 'noadd ' + imgX.length; add[0].click(); await sl(2500);
    return [...w.document.querySelectorAll('a')].filter(a => /سحب الصورة/.test(a.textContent) && a.offsetWidth > 0).length ? 'dialog still open' : 'ok x' + imgX.length;
  };
  F.confirm = async () => {
    const w = window.__f2; const c = w.hbAll('button,kat-button').filter(e => e.offsetWidth > 0 && /^(إرسال|تأكيد|إرسال للموافقة)$/.test((e.textContent || e.getAttribute('label') || '').trim())).pop();
    if (!c) return 'noconfirm'; if (!react(w, c)) (c.shadowRoot && c.shadowRoot.querySelector('button') || c).click(); await sl(7000);
    return /بنجاح|successfully/.test(w.document.body.innerText) ? 'SUCCESS' : 'unknown';
  };
})();
'apflow ok';
