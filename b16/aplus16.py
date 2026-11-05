import os, sys, json, re
sys.path.insert(0, '/home/claude/aplus4')
os.environ.setdefault('HB_FONTS', '/home/claude/habbaa-product-images/pipeline/fonts')
import aplus_lib as L
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, '/home/claude/b16')
import gen16 as gen9

B = '/home/claude/b16'; O = f'{B}/aplus'; os.makedirs(O, exist_ok=True)
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
 'party16': dict(
   asins=['B0FDLDQRKM','B0F8QTX2SW','B0F8HVPMQV','B0DBGDMW3Y','B0F89CMBRH','B0F8R3LFMR','B0F92JNJTY','B0F7LLS5LM','B0FDGZH9SY','B0FDGX1BJT','B0FDGWTL5S','B0FDGRFDW9','B0FDGRD6TS','B0FDGVF6SR'],
   hero=(life('party_hL'), ['هدايا وحفلات', 'بلمسة أنيقة'],
         ['أكياس هدايا وشموع أرقام وبالونات', 'لكل مناسبة سعيدة']),
   uses=('لكل مناسبة', [(f'{B}/src/B0FDGVF6SR.jpg', 'تغليف الهدايا'), (f'{B}/src/B0F8QTX2SW.jpg', 'زينة الكيك'),
                       (f'{B}/src/B0FDLDQRKM.jpg', 'ديكور الحفلة'), (f'{B}/src/B0F92JNJTY.jpg', 'ألعاب العائلة')]),
   rng=('تشكيلة HABBAA للهدايا والحفلات', [('B0FDGVF6SR', 'أكياس هدايا ورقية'), ('B0F8QTX2SW', 'شمعة رقم ذهبية'),
                                          ('B0FDLDQRKM', 'بالون رقم ذهبي'), ('B0F7LLS5LM', 'كرة سلة')]),
   alt=['أكياس هدايا ورقية بيضاء من HABBAA على طاولة حفلة', 'استخدامات منتجات HABBAA للهدايا والحفلات',
        'تشكيلة HABBAA من أكياس الهدايا والشموع والبالونات']),
 'home16': dict(
   asins=['B0F8NVFXFJ','B0F8NRSZ6R','B0F8NT45B7','B0F8NNP871','B0F89C8MF7','B0F8JCX8QQ','B0FFZP1787','B0FFCGPBY7','B0F8P3CRRW','B0F8P14X8T','B0F8QLX8TG','B0F8QM8SR4','B0F8NTRQTB','B0F8JBSC2T','B0F8BB1S7X','B0F897DVYY','B0HP8NQRP4','B0FD8Y1C1N','B0FD8W29YM','B0F7R8K4S4','B0FFZMJ3R8','B0FDHBN5RN','B0D96NDTJF','B0FG3FBSLB'],
   hero=(life('home_hL'), ['بيت مرتب', 'وتفاصيل يومية'],
         ['سلال غسيل ومناشف وأدوات مطبخ', 'للحمام والمطبخ والسيارة']),
   uses=('لكل زاوية في البيت', [(f'{B}/src/B0FDHBN5RN.jpg', 'الحمام'), (f'{B}/src/B0FG3FBSLB.jpg', 'المطبخ'),
                               (f'{B}/src/B0HP8NQRP4.jpg', 'السيارة'), (f'{B}/src/B0FD8Y1C1N.jpg', 'ركن المكتب')]),
   rng=('تشكيلة HABBAA للبيت', [('B0F8QLX8TG', 'مقشرة بمقبض خشبي'), ('B0F8JCX8QQ', 'موس حلاقة'),
                               ('B0FD8W29YM', 'مجسم السلام'), ('B0F8JBSC2T', 'دبابيس شعر')]),
   alt=['سلة غسيل HABBAA من البامبو مع مناشف بيضاء في الحمام', 'استخدامات منتجات HABBAA في البيت',
        'تشكيلة HABBAA من منتجات البيت والاستخدام اليومي']),
}

if __name__ == '__main__':
    alts = {}
    for k, f in FAM.items():
        for s in f['hero'][1] + f['hero'][2] + [f['uses'][0], f['rng'][0]] + [l for _, l in f['uses'][1]] + [l for _, l in f['rng'][1]] + f['alt']:
            check(s)
        hero(f['hero'][0], f['hero'][1], f['hero'][2], f'{O}/d16-{k}-1-hero')
        L.uses(f['uses'][1], f['uses'][0], f'{O}/d16-{k}-2-uses')
        rng(f['rng'][1], f['rng'][0], f'{O}/d16-{k}-3-feat')
        alts[k] = f['alt']
    json.dump(alts, open(f'{O}/d16-alts.json', 'w'), ensure_ascii=False)
    json.dump({k: f['asins'] for k, f in FAM.items()}, open(f'{O}/d16-asins.json', 'w'))
    print('ok', sum(len(f['asins']) for f in FAM.values()))
