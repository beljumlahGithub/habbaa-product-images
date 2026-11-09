window.__AP = window.__AP || {};
(() => {
  const P = window.__AP;
  const BAD = /مص|كس|لعن|بز|ثدي|علق|هور|جن|نيك|لسبو|فوهة|شفر|مخزن|جماع|زنا|زنى|زب|طيز|قحب|شرموط|عاهر|خول|لوط|سكس|نهد|قبض/;
  P.bad = (s) => { const t = String(s).replace(/[ً-ْ]/g, '').replace(/\s+/g, ''); const m = t.match(BAD); return m ? m[0] : '' };
  P.CATS = [
    { k: 'bags', re: /(كيس|اكياس|أكياس)\s*(ورق|ورقي|ورقية)|paper bag/i, h: 'أكياس ورقية للتغليف', s: 'للهدايا والمحلات والمناسبات', f: ['مقاسات وألوان متنوعة', 'للهدايا والمشتريات اليومية', 'شكل مرتب وأنيق عند التقديم', 'العدد والمقاس في عنوان كل منتج'] },
    { k: 'boxes', re: /(علب|علبة|علية|بوكس|صندوق|صناديق)\s*(ورق|ورقية|كرتون|كرتونية)|kraft|paper box/i, h: 'علب ورقية للتقديم والتغليف', s: 'للمطاعم والحلويات والهدايا', f: ['أشكال ومقاسات متنوعة', 'تقديم مرتب للطعام والحلويات', 'للمحلات والمناسبات والمنزل', 'العدد والمقاس في عنوان كل منتج'] },
    { k: 'foil', re: /قصدير|ألمنيوم|المنيوم|الومنيوم|foil/i, h: 'أواني وأوراق ألمنيوم', s: 'للطبخ والتقديم وحفظ الطعام', f: ['أشكال ومقاسات متعددة', 'للتقديم والتخزين في المطبخ', 'لا تستخدم داخل المايكرويف', 'العدد والمقاس في عنوان كل منتج'] },
    { k: 'cont', re: /(علب|علبة|علية|وعاء|اوعية|أوعية|برطمان)\s*(طعام|بلاستيك|حفظ)|food container/i, h: 'علب حفظ وتقديم الطعام', s: 'للتخزين والتقديم اليومي', f: ['أحجام متعددة حسب المنتج', 'لحفظ الأطعمة وتنظيم المطبخ', 'للمنازل والمطاعم والرحلات', 'العدد والسعة في عنوان كل منتج'] },
    { k: 'cups', re: /(اكواب|أكواب|كوب|كاسات)\s*(ورق|ورقية|بلاستيك|كرتون)|paper cup|plastic cup/i, h: 'أكواب للضيافة والتقديم', s: 'للمشروبات حسب نوع كل كوب', f: ['مقاسات وألوان متنوعة', 'للضيافة والمكاتب والمناسبات', 'سهلة الحمل والتقديم', 'العدد والسعة في عنوان كل منتج'] },
    { k: 'cutl', re: /(ملاعق|ملعقة|شوك|شوكة|سكاكين|صحون|صحن|صينية|صواني|أطباق|اطباق)\s*/i, h: 'أدوات مائدة للحفلات والرحلات', s: 'للضيافة والتقديم بسهولة', f: ['قطع خفيفة وسهلة الاستخدام', 'للحفلات والرحلات والضيافة', 'أشكال وألوان متنوعة', 'العدد والمقاس في عنوان كل منتج'] },
    { k: 'cello', re: /سلوفان|كيس بلاستيك|اكياس بلاستيك|أكياس بلاستيك|كيس شفاف|اكياس شفافة|أكياس شفافة/i, h: 'أكياس شفافة للتغليف', s: 'للحلويات والهدايا والتوزيعات', f: ['تظهر محتوى الكيس بوضوح', 'للتوزيعات والهدايا الصغيرة', 'مقاسات متعددة حسب المنتج', 'العدد والمقاس في عنوان كل منتج'] },
    { k: 'party', re: /بالون|بلالين|حفلات|حفلة|شمعة|شموع|زينة|توزيعات|party|balloon|candle/i, h: 'مستلزمات الحفلات والمناسبات', s: 'لتجهيز الاحتفالات في البيت', f: ['ألوان وأشكال متنوعة', 'للحفلات والمناسبات المنزلية', 'سهلة التجهيز والترتيب', 'التفاصيل في عنوان كل منتج'] },
    { k: 'bath', re: /ليفة|استحمام|حمام|فرشاة اسنان|فرشاة أسنان|مشط|شعر|bath/i, h: 'مستلزمات الحمام والاستخدام الشخصي', s: 'للاستخدام اليومي في المنزل', f: ['تصاميم وألوان متنوعة', 'للاستخدام الشخصي اليومي', 'سهلة الحمل والحفظ', 'التفاصيل في عنوان كل منتج'] },
    { k: 'clean', re: /منفضة|تنظيف|ممسحة|مكنسة|مساحة|اسفنج|إسفنج|clean|brush/i, h: 'أدوات تنظيف المنزل', s: 'لبيت مرتب ونظيف كل يوم', f: ['أدوات عملية للاستخدام اليومي', 'للمطبخ والحمام وأرجاء المنزل', 'سهلة الاستخدام والحفظ', 'التفاصيل في عنوان كل منتج'] },
    { k: 'gen', re: /./, h: 'منتجات هبة للمنزل', s: 'احتياجات يومية في مكان واحد', f: ['تشكيلة منتجات متنوعة', 'للمنزل والمكتب والمناسبات', 'تصاميم عملية للاستخدام اليومي', 'التفاصيل في عنوان كل منتج'] },
  ];
  P.cat = (t) => P.CATS.find(c => c.re.test(t)).k;
  const font = (w, px) => `${w} ${px}px Tajawal, Arial, sans-serif`;
  const C = { bg: '#F7F5F1', ink: '#1E2126', sub: '#62666E', acc: '#B08D57', teal: '#1F6F6B', white: '#FFFFFF' };
  P.logo = null;
  P.init = async () => {
    if (!P.logo) { const b = await (await fetch('https://raw.githubusercontent.com/beljumlahGithub/habbaa-product-images/main/inactive/logo_black.png')).blob(); P.logo = await createImageBitmap(b) }
  };
  const cv = (w, h, bg) => { const c = document.createElement('canvas'); c.width = w; c.height = h; const x = c.getContext('2d'); x.fillStyle = bg; x.fillRect(0, 0, w, h); return [c, x] };
  const rr = (x, a, b, w, h, r, fill) => { x.beginPath(); x.roundRect(a, b, w, h, r); x.fillStyle = fill; x.fill() };
  const place = (x, bm, bx, by, bw, bh) => window.__G.place(x, bm, bx, by, bw, bh);
  const rt = (x, s, X, y, px, w, col) => { x.direction = 'rtl'; x.textAlign = 'right'; x.font = font(w, px); x.fillStyle = col; x.fillText(s, X, y) };
  const ct = (x, s, X, y, px, w, col) => { x.direction = 'rtl'; x.textAlign = 'center'; x.font = font(w, px); x.fillStyle = col; x.fillText(s, X, y) };
  const blob = (c) => new Promise(z => c.toBlob(z, 'image/jpeg', 0.9));
  const logo = (x, X, Y, h) => { const r = h / P.logo.height; x.drawImage(P.logo, X - P.logo.width * r, Y, P.logo.width * r, h) };
  // hero: products left, text right
  P.hero = async (cat, ims) => {
    const [d, x] = cv(1464, 600, C.bg); rr(x, 0, 0, 1464, 600, 0, C.bg);
    rr(x, 30, 30, 700, 540, 30, C.white); const n = Math.min(3, ims.length);
    if (n == 1) place(x, ims[0], 60, 60, 640, 480); else for (let i = 0; i < n; i++) place(x, ims[i], 50 + i * (660 / n), 80, 660 / n - 20, 440);
    logo(x, 1410, 50, 80); let fs = 54; x.font = font(800, fs); while (x.measureText(cat.h).width > 640 && fs > 34) { fs -= 2; x.font = font(800, fs) } rt(x, cat.h, 1410, 250, fs, 800, C.ink); rt(x, cat.s, 1410, 320, 32, 400, C.sub); x.fillStyle = C.acc; x.fillRect(1410 - 140, 350, 140, 6);
    rt(x, 'منتجات مختارة بعناية من هبة', 1410, 430, 28, 400, C.teal);
    const [m, y] = cv(600, 450, C.bg); rr(y, 20, 150, 560, 280, 24, C.white);
    if (n == 1) place(y, ims[0], 40, 165, 520, 250); else for (let i = 0; i < n; i++) place(y, ims[i], 30 + i * (540 / n), 170, 540 / n - 10, 240);
    logo(y, 570, 15, 44); let ms = 30; y.font = font(800, ms); while (y.measureText(cat.h).width > 540 && ms > 18) { ms -= 1; y.font = font(800, ms) } rt(y, cat.h, 570, 105, ms, 800, C.ink); rt(y, cat.s, 570, 138, 20, 400, C.sub);
    return [await blob(d), await blob(m)];
  };
  // uses: 4 tiles with product photos + short names
  P.tiles = async (cat, items) => {
    const [d, x] = cv(1464, 600, C.bg); rt(x, 'من تشكيلة ' + cat.h, 1410, 75, 36, 800, C.ink);
    const T = items.slice(0, 4); const tw = (1464 - 60 - 30 * (T.length - 1)) / T.length;
    T.forEach((it, i) => { const X = 1464 - 30 - (i + 1) * tw - i * 30; rr(x, X, 110, tw, 460, 26, C.white); place(x, it.bm, X + 20, 130, tw - 40, 330); x.save(); x.beginPath(); x.rect(X + 10, 470, tw - 20, 90); x.clip(); ct(x, it.name, X + tw / 2, 520, 26, 700, C.ink); x.restore() });
    const [m, y] = cv(600, 450, C.bg); rt(y, 'من تشكيلة ' + cat.h, 575, 45, 22, 800, C.ink);
    const M = T.slice(0, 4); M.forEach((it, i) => { const col = i % 2, row = Math.floor(i / 2); const X = 600 - 15 - (col + 1) * 280 - col * 10; const Y = 70 + row * 190; rr(y, X, Y, 280, 180, 18, C.white); place(y, it.bm, X + 10, Y + 8, 260, 128); y.save(); y.beginPath(); y.rect(X + 5, Y + 140, 270, 36); y.clip(); ct(y, it.name, X + 140, Y + 166, 17, 700, C.ink); y.restore() });
    return [await blob(d), await blob(m)];
  };
  // features: product right card + 4 bullets
  P.feats = async (cat, im) => {
    const [d, x] = cv(1464, 600, C.bg); rr(x, 30, 30, 520, 540, 30, C.white); place(x, im, 60, 60, 460, 480);
    rt(x, 'لماذا تختار هبة؟', 1410, 95, 44, 800, C.ink); x.fillStyle = C.acc; x.fillRect(1410 - 120, 120, 120, 6);
    cat.f.forEach((t, i) => { const Y = 170 + i * 100; rr(x, 610, Y, 800, 80, 20, C.white); x.beginPath(); x.arc(1370, Y + 40, 18, 0, Math.PI * 2); x.fillStyle = C.acc; x.fill(); rt(x, t, 1335, Y + 51, 32, 700, C.ink) });
    const [m, y] = cv(600, 450, C.bg); rt(y, 'لماذا تختار هبة؟', 575, 45, 26, 800, C.ink);
    cat.f.forEach((t, i) => { const Y = 70 + i * 92; rr(y, 15, Y, 570, 78, 16, C.white); y.beginPath(); y.arc(555, Y + 39, 11, 0, Math.PI * 2); y.fillStyle = C.acc; y.fill(); rt(y, t, 533, Y + 48, 22, 700, C.ink) });
    return [await blob(d), await blob(m)];
  };
  P.short = (t) => { let s = window.__G.short(t); s = s.replace(/بوكس ورقي(?!ة)/g, 'علبة ورقية').replace(/بوكس/g, 'علبة').replace(/اكسسوارات|إكسسوارات/g, 'مستلزمات').replace(/المقبض|مقبض/g, 'المسكة'); s = s.replace(/بوكس ورقي\b/g, 'علبة ورقية'); let ws = s.split(' ').slice(0, 4); while (ws.length > 2 && /^(لون|مع|من|مقاسات|مقاس|ذات|و|ب|في|عدد|حجم)$/.test(ws[ws.length - 1])) ws.pop(); s = ws.join(' '); while (P.bad(s) && s.includes(' ')) s = s.split(' ').slice(0, -1).join(' '); return P.bad(s) ? '' : s };
  P.checkCat = (cat) => [cat.h, cat.s, ...cat.f, 'منتجات مختارة بعناية من هبة', 'من تشكيلة ' + cat.h, 'لماذا تختار هبة؟'].map(P.bad).filter(Boolean);
})();
'aplus ok';
