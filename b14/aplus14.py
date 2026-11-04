import os, sys, json, re
sys.path.insert(0, '/home/claude/aplus4')
os.environ.setdefault('HB_FONTS', '/home/claude/habbaa-product-images/pipeline/fonts')
import aplus_lib as L
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, '/home/claude/b14')
import gen14 as gen9

B = '/home/claude/b14'; O = f'{B}/aplus'; os.makedirs(O, exist_ok=True)
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
 'tools14': dict(
   asins=['B0GWY4W755','B0F7Y4KR1R','B0F898XRBQ','B0F7Y49KLW','B0GQZRF82H','B0F8P12DZV','B0F8J7FTYP'],
   hero=(life('sew_hL'), ['خياطة وتصليحات', 'بأدوات بسيطة'],
         ['إبر وخيوط وشريط لاصق ومقص للبيت', 'لتصليح الملابس والأشغال اليومية']),
   uses=('لكل شغلة في البيت', [(f'{B}/src/41XEW-Sk4UL.jpg', 'تصليح الملابس'), (f'{B}/src/6119xq1Z7gL.jpg', 'التطريز والحياكة'),
                             (f'{B}/src/51kbScG7lYL.jpg', 'تثبيت الصور'), (f'{B}/srcup/21f10LhYMLL.jpg', 'قص الورق')]),
   rng=('تشكيلة HABBAA للخياطة والأدوات', [('B0GWY4W755', 'طقم إبر خياطة'), ('B0F7Y4KR1R', 'بكرة خيط تطريز'),
                                        ('B0F898XRBQ', 'حبل مطاط 5 ياردة'), ('B0GQZRF82H', 'شريط لاصق دبل فيس')]),
   alt=['طقم إبر خياطة HABBAA على طاولة خشب مع قماش وبكرة خيط', 'استخدامات أدوات HABBAA للخياطة والبيت',
        'تشكيلة HABBAA من أدوات الخياطة والأدوات المنزلية']),
 'care14': dict(
   asins=['B0D9WM8YGH','B0F89B1W38','B0F89DR29Z','B0F896WTW5','B0F8N9MTJQ','B0D9P1YXL1','B0FG3DSCJM','B0F8JG3JL1','B0F8JKD1MF','B0F7Y5CV6L','B0F8JCGHZ3','B0F8J9373V','B0F8NJDWLQ','B0F8N76B82'],
   hero=(life('care_hL'), ['روتينك اليومي', 'براحة وترتيب'],
         ['ليف قفاز ومبارد قدم وأدوات أظافر وشعر', 'للحمام والسفر وكل يوم']),
   uses=('أدوات لكل وقت', [(f'{B}/src/81TmTX2GglL.jpg', 'وقت الاستحمام'), (f'{B}/src/61fxhK32LTL.jpg', 'راحة القدم'),
                          (f'{B}/src/61COneifR8L.jpg', 'الأظافر'), (f'{B}/src/51tQiNgO18L.jpg', 'وقت النوم')]),
   rng=('تشكيلة HABBAA للروتين اليومي', [('B0FG3DSCJM', 'ليفة قفاز للاستحمام'), ('B0F89B1W38', 'مبرد قدم بوجهين'),
                                       ('B0D9WM8YGH', 'قصاصة جلد الأظافر'), ('B0F8JCGHZ3', 'علب سفر بلاستيك')]),
   alt=['ليفة قفاز HABBAA الزرقاء على رخام الحمام مع منشفة', 'استخدامات منتجات HABBAA في الروتين اليومي',
        'تشكيلة HABBAA من أدوات الروتين اليومي']),
 'kitchen14': dict(
   asins=['B0F8P3MQ1B','B0F8P2X25W','B0F8NYSHS9','B0F8P4CVDK','B0F8P22RLR','B0F8P2J97V','B0F8P3RXB4','B0F8P53DSZ','B0F7LC2YP4','B0F7XRTGNH','B0F8J7N9R3'],
   hero=(life('kitchen_hL'), ['مطبخك أرتب', 'وأكلك محفوظ'],
         ['أكياس حفظ شفافة بسحاب بمقاسات متعددة', 'للمطبخ والفريزر والرحلات']),
   uses=('من الحفظ إلى التقديم', [(f'{B}/src/41V+aF+iRZL.jpg', 'حفظ الأكل'), (f'{B}/src/612jXzHDeQL.jpg', 'العصيرات'),
                                (f'{B}/src/410brG43pEL.jpg', 'الحفلات'), (f'{B}/srcup/21wh-zZRp9L.jpg', 'تحضير السمك')]),
   rng=('تشكيلة HABBAA للمطبخ', [('B0F8P4CVDK', 'أكياس حفظ بسحاب'), ('B0F7LC2YP4', 'شفاطات شفافة'),
                               ('B0F7XRTGNH', 'شفاطات مرنة'), ('B0F8J7N9R3', 'مقص سمك')]),
   alt=['أكياس حفظ HABBAA الشفافة بالسحاب على رخام المطبخ', 'استخدامات منتجات HABBAA في المطبخ',
        'تشكيلة HABBAA من أدوات المطبخ']),
 'home14': dict(
   asins=['B0F8NXV58Y','B0F8BPLWPP','B0F8NMC4ZL','B0F7Y63K73','B0F893CXDW','B0F8C2TFS8','B0F8NJTWRB'],
   hero=(life('home_hL'), ['تفاصيل البيت', 'أسهل كل يوم'],
         ['مشابك غسيل ودعاسة ومراوح يد', 'للبيت والخروج والصيف']),
   uses=('لكل يوم', [(f'{B}/srcup/31cVOkPD6LL.jpg', 'نشر الغسيل'), (f'{B}/src/71BLMwMJ5rL.jpg', 'أرضية الحمام'),
                    (f'{B}/src/51mI6J9CUaL.jpg', 'الأيام الحارة'), (f'{B}/srcup/21x0hibH0hL.jpg', 'المسبح')]),
   rng=('تشكيلة HABBAA للبيت', [('B0F8NXV58Y', 'مشابك غسيل'), ('B0F8BPLWPP', 'دعاسة مانعة للانزلاق'),
                              ('B0F893CXDW', 'مروحة يد بنقشة ورد'), ('B0F8NJTWRB', 'عوامة سباحة للأطفال')]),
   alt=['مشابك غسيل HABBAA الملونة على حبل الغسيل', 'استخدامات منتجات HABBAA في البيت',
        'تشكيلة HABBAA من منتجات البيت']),
}

if __name__ == '__main__':
    alts = {}
    for k, f in FAM.items():
        for s in f['hero'][1] + f['hero'][2] + [f['uses'][0], f['rng'][0]] + [l for _, l in f['uses'][1]] + [l for _, l in f['rng'][1]] + f['alt']:
            check(s)
        hero(f['hero'][0], f['hero'][1], f['hero'][2], f'{O}/d14-{k}-1-hero')
        L.uses(f['uses'][1], f['uses'][0], f'{O}/d14-{k}-2-uses')
        rng(f['rng'][1], f['rng'][0], f'{O}/d14-{k}-3-feat')
        alts[k] = f['alt']
    json.dump(alts, open(f'{O}/d14-alts.json', 'w'), ensure_ascii=False)
    json.dump({k: f['asins'] for k, f in FAM.items()}, open(f'{O}/d14-asins.json', 'w'))
    print('ok', sum(len(f['asins']) for f in FAM.values()))
