import os, sys, json, re
sys.path.insert(0, '/home/claude/aplus4')
os.environ.setdefault('HB_FONTS', '/home/claude/habbaa-product-images/pipeline/fonts')
import aplus_lib as L
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, '/home/claude/b11')
import gen11 as gen9

B = '/home/claude/b11'; O = f'{B}/aplus'; os.makedirs(O, exist_ok=True)
DW, DH, MW, MH = L.DW, L.DH, L.MW, L.MH
life = lambda a, k=0: f'{B}/life/{a}_{k}.jpg'
BAN = ['شفر', 'عيدالميلاد', 'ميلاد', 'كريسماس', 'مص', 'كس', 'لعن', 'بز', 'ثدي', 'علق', 'هور', 'جن', 'نيك', 'لسبو', 'فوهة']

def check(s):
    z = re.sub(r'[ً-ْ\s]', '', s)
    bad = [b for b in BAN if b in z]
    if bad: raise SystemExit(f'BANNED {bad} in: {s}')

def hero(img, head, sub, out):
    im = Image.open(img).convert('RGB')
    c = Image.new('RGB', (DW, DH), L.BG)
    pw = 700
    c.paste(L.cover(im, pw, DH), (0, 0))
    # soft fade from photo to panel
    g = Image.new('L', (120, DH)); gd = ImageDraw.Draw(g)
    for x in range(120): gd.line([(x, 0), (x, DH)], fill=int(255 * x / 119))
    c.paste(Image.new('RGB', (120, DH), L.BG), (pw - 120, 0), g)
    d = ImageDraw.Draw(c); xr = DW - 90; maxw = DW - pw - 160
    L.rtext(d, xr, 120, 'HABBAA', L.font('ExtraBold', 30), L.ACC)
    y = 175
    for line in head:
        L.rtext(d, xr, y, line, L.fit(d, line, 'ExtraBold', 70, maxw), L.INK); y += 90
    y += 25
    for line in sub:
        L.rtext(d, xr, y, line, L.fit(d, line, 'Medium', 32, maxw), L.SUB); y += 48
    d.rectangle((xr - 90, y + 30, xr, y + 36), fill=L.ACC)
    c.save(out + '-desktop.jpg', quality=92)
    m = Image.new('RGB', (MW, MH), L.BG); m.paste(L.cover(im, MW, 290), (0, 0)); d = ImageDraw.Draw(m)
    t = ' '.join(head); L.rtext(d, MW - 32, 308, t, L.fit(d, t, 'ExtraBold', 40, MW - 64), L.INK)
    y = 368
    for line in sub:
        L.rtext(d, MW - 32, y, line, L.fit(d, line, 'Medium', 22, MW - 64), L.SUB); y += 34
    m.save(out + '-mobile.jpg', quality=92)

def rng(items, title, out):
    """items: 4 (asin, label); product photos from the listing main image, first = rightmost"""
    c = Image.new('RGB', (DW, DH), (244, 241, 236)); d = ImageDraw.Draw(c)
    L.ctext(d, DW // 2, 40, title, L.fit(d, title, 'ExtraBold', 46, DW - 200), L.INK)
    tw_, th, gap, top = 330, 380, 24, 120
    x0 = (DW - (4 * tw_ + 3 * gap)) // 2
    for i, (a, lab) in enumerate(items[::-1]):
        x = x0 + i * (tw_ + gap)
        d.rounded_rectangle((x, top, x + tw_, top + th), 18, fill=(255, 255, 255))
        p = gen9.product(a); p.thumbnail((tw_ - 50, th - 50), Image.LANCZOS)
        c.paste(p, (x + (tw_ - p.width) // 2, top + (th - p.height) // 2))
        L.ctext(d, x + tw_ // 2, top + th + 26, lab, L.fit(d, lab, 'Bold', 28, tw_ - 10), L.INK)
    c.save(out + '-desktop.jpg', quality=92)
    m = Image.new('RGB', (MW, MH), (244, 241, 236)); d = ImageDraw.Draw(m)
    L.ctext(d, MW // 2, 16, title, L.fit(d, title, 'ExtraBold', 30, MW - 40), L.INK)
    tw2, th2, top = 270, 160, 62; xs = [MW - 20 - tw2, MW - 20 - 2 * tw2 - 20]
    for i, (a, lab) in enumerate(items):
        r, cc = divmod(i, 2); x, y = xs[cc], top + r * (th2 + 30)
        d.rounded_rectangle((x, y, x + tw2, y + th2), 12, fill=(255, 255, 255))
        p = gen9.product(a); p.thumbnail((tw2 - 20, th2 - 16), Image.LANCZOS)
        m.paste(p, (x + (tw2 - p.width) // 2, y + (th2 - p.height) // 2))
        L.ctext(d, x + tw2 // 2, y + th2 + 4, lab, L.fit(d, lab, 'Bold', 19, tw2 - 6), L.INK)
    m.save(out + '-mobile.jpg', quality=92)

FAM = {
 'kitchen4': dict(
   asins=['B0FL17Q2S2','B0DB5Z4S1W','B0DB61C6DF','B0DB61KTJL','B0FL2XPV55','B0F7LBCZTZ','B0FQ685GLD','B0CHF59HZP'],
   hero=(life('B0FL17Q2S2'), ['مطبخك أرتب', 'وأكلك محفوظ'],
         ['علب حفظ وأكياس سحاب وأدوات تحضير عملية', 'لترتيب الثلاجة والمطبخ كل يوم']),
   uses=('لكل يوم في المطبخ', [(life('B0FL17Q2S2'), 'حفظ الأكل'), (life('B0DB61C6DF'), 'التخزين والترتيب'),
                              (life('B0H1MYPTZD'), 'سقي النباتات'), (life('B0CH34GPTG'), 'ترتيب الدولاب')]),
   rng=('تشكيلة HABBAA للبيت والمطبخ', [('B0FL17Q2S2', 'علب حفظ دائرية'), ('B0DB61C6DF', 'أكياس سحاب شفافة'),
                                      ('B0FQ685GLD', 'فوطة مطبخ قطن'), ('B0H1MYPTZD', 'بخاخ رذاذ ناعم')]),
   alt=['علب حفظ طعام HABBAA على رخام المطبخ', 'استخدامات منتجات HABBAA في المطبخ والبيت',
        'تشكيلة HABBAA من أدوات المطبخ والبيت']),
 'home4': dict(
   asins=['B0H1MYPTZD','B0H1N3M31R','B0H1MT9XV2','B0GRRGYSPV','B0G8MBR8XV','B0G8MCW7YL','B0FLWL2F57','B0FDQYM38G','B0CJ33KGF3','B0CH34GPTG','B0CHYYCGS4','B0D9NZHYSN','B0F7RCYWLZ','B0F7RDF5ZY','B0F7R9N64Y'],
   hero=(life('B0F7RDF5ZY'), ['تفاصيل ترتب', 'بيتك ويومك'],
         ['أدوات عملية للبيت والصيانة والترتيب', 'ومجسمات بالخط العربي لزوايا البيت والمكتب']),
   uses=('في كل زاوية', [(life('B0F7R9N64Y'), 'المجلس'), (life('B0CH34GPTG'), 'الدولاب'),
                        (life('B0G8MBR8XV'), 'الصيانة والدهان'), (life('B0CJ33KGF3'), 'حماية الجدار')]),
   rng=('تشكيلة HABBAA للبيت', [('B0F7RDF5ZY', 'مجسم اسم الله الفتاح'), ('B0CH34GPTG', 'علاقات ملابس خشب'),
                              ('B0G8MBR8XV', 'سكاكين معجون ستانلس'), ('B0CHYYCGS4', 'مظلات شفافة')]),
   alt=['مجسم اسم الله الفتاح من HABBAA في المجلس', 'استخدامات منتجات HABBAA في البيت',
        'تشكيلة HABBAA من أدوات البيت']),
 'play4': dict(
   asins=['B0HMRPRYWZ','B0F7S9XGJ3','B0F7SG4HYK','B0F7SFWXWV','B0F7SQNN5G','B0F7SR2JXN','B0F7R757LW','B0CXQ11KC4','B0CGPCVSCQ','B0CGP9Z5Z4','B0DBJ7N5S8','B0DBJ59QVK','B0FG3KW65M','B0HM4FM4JX'],
   hero=(life('B0F7SR2JXN'), ['جمعة حلوة', 'ونشاط ما يخلص'],
         ['ورق لعب وكرة قدم وعدادات أصابع وقبضات تقوية', 'للمجلس والملعب والمسبح والطلعات']),
   uses=('أوقات حلوة للعائلة', [(life('B0F7SR2JXN'), 'سهرة المجلس'), (life('B0HMRPRYWZ'), 'الملعب'),
                               (life('B0FG3KW65M'), 'المسبح'), (life('B0HM4FM4JX'), 'الكشتة')]),
   rng=('تشكيلة HABBAA للعب والنشاط', [('B0F7SR2JXN', 'ورق لعب'), ('B0HMRPRYWZ', 'كرة قدم مقاس 5'),
                                     ('B0CXQ11KC4', 'عداد إصبع رقمي'), ('B0DBJ7N5S8', 'قبضة تقوية اليد')]),
   alt=['ورق لعب HABBAA في جلسة المجلس', 'استخدامات منتجات HABBAA للعب والنشاط',
        'تشكيلة HABBAA للعب والنشاط']),
}

if __name__ == '__main__':
    alts = {}
    for k, f in FAM.items():
        for s in f['hero'][1] + f['hero'][2] + [f['uses'][0], f['rng'][0]] + [l for _, l in f['uses'][1]] + [l for _, l in f['rng'][1]] + f['alt']:
            check(s)
        hero(f['hero'][0], f['hero'][1], f['hero'][2], f'{O}/d11-{k}-1-hero')
        L.uses(f['uses'][1], f['uses'][0], f'{O}/d11-{k}-2-uses')
        rng(f['rng'][1], f['rng'][0], f'{O}/d11-{k}-3-feat')
        alts[k] = f['alt']
    json.dump(alts, open(f'{O}/d11-alts.json', 'w'), ensure_ascii=False)
    json.dump({k: f['asins'] for k, f in FAM.items()}, open(f'{O}/d11-asins.json', 'w'))
    print('ok', sum(len(f['asins']) for f in FAM.values()))
