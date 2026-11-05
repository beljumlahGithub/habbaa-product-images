import os, sys, json, re
sys.path.insert(0, '/home/claude/aplus4')
os.environ.setdefault('HB_FONTS', '/home/claude/habbaa-product-images/pipeline/fonts')
import aplus_lib as L
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, '/home/claude/b15')
import gen15 as gen9

B = '/home/claude/b15'; O = f'{B}/aplus'; os.makedirs(O, exist_ok=True)
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
 'play15': dict(
   asins=['B0F92HJZQS','B0F8R3TW1H','B0F92GLDCH','B0F8HRZY8Y','B0F8JCBKB7','B0F8JB3Z16','B0F92K8CDD'],
   hero=(life('party_hL'), ['لعب وصيف', 'ومرح للصغار'],
         ['عوامات مسبح ونظارات شمسية وألعاب يدوية', 'للمسبح والبحر والبيت']),
   uses=('لحظات لعب ممتعة', [(f'{B}/src/51SaJN+UtwL.jpg', 'المسبح'), (f'{B}/src/619Pgk52-vL.jpg', 'الشمس والرحلات'),
                            (f'{B}/src/61GTqqaiHsL.jpg', 'ألعاب يدوية'), (f'{B}/src/31UU6DC-IdL.jpg', 'غرفة الأطفال')]),
   rng=('تشكيلة HABBAA للعب والصيف', [('B0F8JB3Z16', 'عوامة بطة'), ('B0F8HRZY8Y', 'نظارات شمسية للأطفال'),
                                    ('B0F92GLDCH', 'كرات زجاجية'), ('B0F92HJZQS', 'نجوم وهلال مضيئة')]),
   alt=['عوامة البطة من HABBAA على حافة المسبح', 'استخدامات منتجات HABBAA للعب والصيف',
        'تشكيلة HABBAA من ألعاب الأطفال ومنتجات الصيف']),
 'home15': dict(
   asins=['B0CLW6D5J8','B0CLW34XSQ','B0F8BQSQHV','B0F8BPJXZD','B0F8NTNCPM','B0F8NRTTZ6','B0F8P5CHMD','B0F8P5FRTK','B0F8P5RX9T','B0F8P19QLV','B0F8P1K68G','B0F92GZWCR','B0F92HX4C1','B0F8QMPSL4','B0F89CSBWQ','B0F8QQJQVD','B0F8P3L61R'],
   hero=(life('home_hL'), ['بيت مرتب', 'بتفاصيل بسيطة'],
         ['سلال غسيل بامبو ودعاسات وعبوات بخاخ', 'للحمام والمطبخ وكل يوم']),
   uses=('لكل زاوية في البيت', [(f'{B}/src/61cr-2Gq+cL.jpg', 'غرفة الغسيل'), (f'{B}/src/91yktsWzTJL.jpg', 'أرضية الحمام'),
                               (f'{B}/src/71NHXJHpyEL.jpg', 'تصليح الملابس'), (f'{B}/src/41Hx5ZztJML.jpg', 'الدراجة')]),
   rng=('تشكيلة HABBAA للبيت', [('B0CLW34XSQ', 'سلة غسيل بامبو'), ('B0F8BQSQHV', 'دعاسة مانعة للانزلاق'),
                               ('B0F89CSBWQ', 'إبر خياطة يدوية'), ('B0F8P3L61R', 'قفل دراجة')]),
   alt=['سلة غسيل HABBAA من البامبو في الحمام', 'استخدامات منتجات HABBAA في البيت',
        'تشكيلة HABBAA من منتجات البيت']),
}

if __name__ == '__main__':
    alts = {}
    for k, f in FAM.items():
        for s in f['hero'][1] + f['hero'][2] + [f['uses'][0], f['rng'][0]] + [l for _, l in f['uses'][1]] + [l for _, l in f['rng'][1]] + f['alt']:
            check(s)
        hero(f['hero'][0], f['hero'][1], f['hero'][2], f'{O}/d15-{k}-1-hero')
        L.uses(f['uses'][1], f['uses'][0], f'{O}/d15-{k}-2-uses')
        rng(f['rng'][1], f['rng'][0], f'{O}/d15-{k}-3-feat')
        alts[k] = f['alt']
    json.dump(alts, open(f'{O}/d15-alts.json', 'w'), ensure_ascii=False)
    json.dump({k: f['asins'] for k, f in FAM.items()}, open(f'{O}/d15-asins.json', 'w'))
    print('ok', sum(len(f['asins']) for f in FAM.values()))
