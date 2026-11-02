import os, sys, json, re
sys.path.insert(0, '/home/claude/aplus4')
os.environ.setdefault('HB_FONTS', '/home/claude/habbaa-product-images/pipeline/fonts')
import aplus_lib as L
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, '/home/claude/b12')
import gen12 as gen9

B = '/home/claude/b12'; O = f'{B}/aplus'; os.makedirs(O, exist_ok=True)
DW, DH, MW, MH = L.DW, L.DH, L.MW, L.MH
life = lambda n: f'{B}/life/{n}.png'
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
 'party5': dict(
   asins=['B0F92KYMNY','B0F92K971T','B0F92KT7HX','B0F92LBYQJ','B0F92L4YY9','B0F92KMLFW','B0F8QS2H9M','B0F8QQ7KL7','B0F8QQCTZJ','B0F8QRP9NH','B0F8QRQ5KP','B0F8QW4T93','B0F8QT81NH','B0F8J3YXQT','B0F8J859BQ','B0F8J7TJ35','B0F8J9QRR8','B0F92KBF7C'],
   hero=(life('party_h1L'), ['حفلتك تلمع', 'بلمسة ذهبية'],
         ['بالونات أرقام وشموع ذهبية وقصاصات ملونة', 'تزيين سهل لكل مناسبة حلوة']),
   uses=('لكل مناسبة فرحة', [(life('cake'), 'كيكة الحفلة'), (life('popper'), 'حفلات التخرج'),
                            (life('party_h2L'), 'زينة المكان'), (life('stickers'), 'غرفة الأطفال')]),
   rng=('تشكيلة HABBAA للحفلات', [('B0F92KT7HX', 'بالونات أرقام ذهبية'), ('B0F8QRQ5KP', 'شموع أرقام للكيك'),
                                ('B0F8J859BQ', 'مطلق قصاصات ملونة'), ('B0F92KBF7C', 'نجوم ثلج تضيء ليلاً')]),
   alt=['بالونة رقم ذهبية من HABBAA مع تاج في صالة حفلة', 'استخدامات منتجات HABBAA للحفلات والمناسبات',
        'تشكيلة HABBAA من زينة الحفلات']),
 'kitchen5': dict(
   asins=['B0FJ9KMVYQ','B0FJ9NPYWG','B0FJB36H8H','B0FJ9RJ4JG','B0F8R3H8ZS','B0F8R4L7M5','B0F8R2XKCH','B0F8R2FRLR','B0F8R3B25Y','B0F8R14Q3G','B0F8R83CSK','B0F8R2LFH2','B0F8R2FD6V','B0F8R4YKLC','B0F7RCSXD7','B0F7R9QK18','B0F7RDMTQP','B0F7M1HVYL','B0F7LRFJTD'],
   hero=(life('cups_h1L'), ['مشروبك البارد', 'بشكل أنيق'],
         ['أكواب نصف سوداء بغطاء قبة وأدوات تقديم', 'للبيت والمقاهي والعزايم']),
   uses=('من الشوي إلى التقديم', [(life('skewers'), 'الشوي'), (life('containers'), 'حفظ الأكل'),
                                (life('forks'), 'تقديم الفواكه'), (f'{B}/src/61NThHcOIhL.jpg', 'غرف الشوربة')]),
   rng=('تشكيلة HABBAA للمطبخ والتقديم', [('B0FJ9KMVYQ', 'أكواب نصف سوداء'), ('B0F8R83CSK', 'أعواد شوي بامبو'),
                                       ('B0F7RCSXD7', 'علب ورق كرافت'), ('B0F8R2FD6V', 'مغارف شوربة')]),
   alt=['أكواب HABBAA نصف السوداء مع قهوة مثلجة في مقهى', 'استخدامات منتجات HABBAA في المطبخ والتقديم',
        'تشكيلة HABBAA من أدوات المطبخ والتقديم']),
 'home5': dict(
   asins=['B0F8NJJSNR','B0F89C4JTT','B0F8BQFDYB','B0F7Y4XTSD','B0F8NM2P2J','B0F8NM3MS9','B0F8BG456V','B0F8B9KL13','B0F8P2N4S6','B0F8HFXT1L','B0F7Y3FYT9','B0F7XZFX1T','B0DKPLZGF3','B0DNB6246Q','B0DNB77VL5'],
   hero=(life('wagon_h1L'), ['طلعاتك أسهل', 'وبيتك أرتب'],
         ['عربة قابلة للطي بعجلات وأغراض يومية', 'للبيت والسفر والطلعات']),
   uses=('لكل يوم ولكل طلعة', [(life('flash'), 'الكشتة'), (life('twine'), 'تغليف الهدايا'),
                              (life('caps'), 'الحمام'), (f'{B}/src/610r42Ism2L.jpg', 'السفر')]),
   rng=('تشكيلة HABBAA للبيت والطلعات', [('B0DNB6246Q', 'عربة قابلة للطي'), ('B0DKPLZGF3', 'سلة غسيل بغطاء'),
                                       ('B0F8HFXT1L', 'كشاف صغير'), ('B0F8NM3MS9', 'مرآة يد')]),
   alt=['عربة HABBAA القابلة للطي على الشاطئ', 'استخدامات منتجات HABBAA في البيت والطلعات',
        'تشكيلة HABBAA للبيت والطلعات']),
}

if __name__ == '__main__':
    alts = {}
    for k, f in FAM.items():
        for s in f['hero'][1] + f['hero'][2] + [f['uses'][0], f['rng'][0]] + [l for _, l in f['uses'][1]] + [l for _, l in f['rng'][1]] + f['alt']:
            check(s)
        hero(f['hero'][0], f['hero'][1], f['hero'][2], f'{O}/d12-{k}-1-hero')
        L.uses(f['uses'][1], f['uses'][0], f'{O}/d12-{k}-2-uses')
        rng(f['rng'][1], f['rng'][0], f'{O}/d12-{k}-3-feat')
        alts[k] = f['alt']
    json.dump(alts, open(f'{O}/d12-alts.json', 'w'), ensure_ascii=False)
    json.dump({k: f['asins'] for k, f in FAM.items()}, open(f'{O}/d12-asins.json', 'w'))
    print('ok', sum(len(f['asins']) for f in FAM.values()))
