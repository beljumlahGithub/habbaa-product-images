import os, sys, json, re
sys.path.insert(0, '/home/claude/aplus4')
os.environ.setdefault('HB_FONTS', '/home/claude/habbaa-product-images/pipeline/fonts')
import aplus_lib as L
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, '/home/claude/b18')
import gen18 as gen9

B = '/home/claude/b18'; O = f'{B}/aplus'; os.makedirs(O, exist_ok=True)
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
 'kitchen18': dict(
   asins=['B0DLLK8D7R','B0DF8RHRMB','B0DDZ5G3X5','B0DDVN4JTW','B0CTYK19D9','B0CQ2XQJ89','B0CPM4FHF9','B0CPM214ZF','B0CPM2RHQ9','B0CPJH3R6W','B0CPJHW5XT','B0CPJGXG93','B0CPC17F19','B0CM1HG3LM','B0CLB5ZNND','B0CKWJ3TQ7','B0CHQQC31T','B0CHK3YGFM','B0CGNZDDZH','B0FQ65SCMJ','B0CGZQMQYR'],
   hero=(life('kit_hL'), ['أدوات مطبخ', 'تسهّل يومك'],
         ['أدوات تحضير وتخزين وتقديم', 'لمطبخ مرتب وعملي']),
   uses=('لكل خطوة في المطبخ', [(f'{B}/src/jar_pad.jpg', 'تخزين الحبوب'), (f'{B}/src/B0CPM4FHF9.jpg', 'هرس البطاطس'),
                    (f'{B}/src/B0CLB5ZNND.jpg', 'تنظيم البهارات'), (f'{B}/src/B0CM1HG3LM.jpg', 'تقديم الطعام')]),
   rng=('من تشكيلة HABBAA للمطبخ', [('B0CPM214ZF', 'فرشاة وملعقة سيليكون'), ('B0CQ2XQJ89', 'قطاعة بيتزا'),
                                    ('B0DDVN4JTW', 'قوالب ثلج'), ('B0CTYK19D9', 'مطارة ستانلس ستيل')]),
   alt=['أدوات مطبخ HABBAA مع طقم ملاعق ذهبي ومهراسة بطاطس', 'استخدامات أدوات مطبخ HABBAA', 'تشكيلة HABBAA من أدوات المطبخ']),
 'home18': dict(
   asins=['B0DFV365WQ','B0DDZ1FC4N','B0DDVVJDYF','B0DBWXTKB4','B0D6S3J3ML','B0CY3G5JPD','B0CXRQJ3LT','B0CQXNZL5S','B0CPF8TKJG','B0CP5Y2THY','B0CLVT4T3R','B0CLSDKDHW','B0CL7SYWNF','B0CL7MMSZX','B0CL7TK82Q','B0CKFJQRD9','B0CKFKCS9P','B0CJYGKWPC','B0CJ78FZZ4','B0CHK6S3TL','B0CH15FNTM','B0CGVLKMQB','B0F8NWNQJ3','B0GWYD7ZXW','B0G6XZ318T','B0GWYDYZ36'],
   hero=(life('home_hL'), ['بيت مرتب', 'بخطوات بسيطة'],
         ['منظمات ورفوف وسلال تخزين', 'لكل غرفة في البيت']),
   uses=('لكل ركن في البيت', [(f'{B}/src/B0CY3G5JPD.jpg', 'ترتيب الملابس'), (f'{B}/src/B0CXRQJ3LT.jpg', 'رفوف الحمام'),
                       (f'{B}/src/B0CL7MMSZX.jpg', 'سلال المهملات'), (f'{B}/src/puz_pad.jpg', 'غرف الأطفال')]),
   rng=None, feat2=(f'{B}/life/home_f.png', ['مساحة أكبر', 'وفوضى أقل'], ['حلول تخزين عملية', 'للخزائن والأدراج والرفوف']),
   alt=['منظمات ملابس بيج داخل خزانة', 'استخدامات منتجات HABBAA للتنظيم المنزلي', 'منظمات ملابس HABBAA داخل الخزانة']),
}

if __name__ == '__main__':
    alts = {}
    for k, f in FAM.items():
        T = f['hero'][1] + f['hero'][2] + [f['uses'][0]] + [l for _, l in f['uses'][1]] + f['alt']
        if f['rng']: T += [f['rng'][0]] + [l for _, l in f['rng'][1]]
        for s in T: check(s)
        hero(f['hero'][0], f['hero'][1], f['hero'][2], f'{O}/d18-{k}-1-hero')
        L.uses(f['uses'][1], f['uses'][0], f'{O}/d18-{k}-2-uses')
        if f['rng']: rng(f['rng'][1], f['rng'][0], f'{O}/d18-{k}-3-feat')
        else:
            for z in f['feat2'][1]+f['feat2'][2]: check(z)
            hero(f['feat2'][0], f['feat2'][1], f['feat2'][2], f'{O}/d18-{k}-3-feat')
        alts[k] = f['alt']
    json.dump(alts, open(f'{O}/d18-alts.json', 'w'), ensure_ascii=False)
    json.dump({k: f['asins'] for k, f in FAM.items()}, open(f'{O}/d18-asins.json', 'w'))
    print('ok', sum(len(f['asins']) for f in FAM.values()))
