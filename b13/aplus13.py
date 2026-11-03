import os, sys, json, re
sys.path.insert(0, '/home/claude/aplus4')
os.environ.setdefault('HB_FONTS', '/home/claude/habbaa-product-images/pipeline/fonts')
import aplus_lib as L
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, '/home/claude/b13')
import gen13 as gen9

B = '/home/claude/b13'; O = f'{B}/aplus'; os.makedirs(O, exist_ok=True)
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
 'party6': dict(
   asins=['B0F8QNPM1P','B0F8R15B25','B0F8BT4ZV3','B0F8BYDPMQ','B0F92L9BRL','B0DBGQB5F8','B0F92JLG8X','B0DZW2DWYW','B0F92K2Z5Z','B0F92JN242'],
   hero=(life('party_hL'), ['لحظة الفرحة', 'تكمل بالتفاصيل'],
         ['قصاصات ملونة وإضاءة وشموع وأدوات تقديم', 'لتزيين الحفلات والجمعات العائلية']),
   uses=('لكل مناسبة حلوة', [(f'{B}/src/91TyscbjwKL.jpg', 'لحظة الاحتفال'), (f'{B}/src/51e8nUtWulL.jpg', 'إضاءة المكان'),
                            (f'{B}/src/61xN5sjKUTL.jpg', 'كيك الحفلة'), (f'{B}/src/6124+L+tBzL.jpg', 'غرفة الأطفال')]),
   rng=('تشكيلة HABBAA للحفلات', [('B0F8QNPM1P', 'مطلق قصاصات ملونة'), ('B0F8R15B25', 'إضاءة LED بطول 5 م'),
                                ('B0F8BT4ZV3', 'شموع بقواعد للكيك'), ('B0F92L9BRL', 'طقم تقطيع الكيك')]),
   alt=['مطلق قصاصات HABBAA في حفلة عائلية مع إضاءة وكيك', 'استخدامات منتجات HABBAA للحفلات',
        'تشكيلة HABBAA من مستلزمات الحفلات']),
 'kitchen6': dict(
   asins=['B0F8R681CQ','B0F8R2858D','B0F8QLFQWB','B0F8C3HBJ3','B0F8BNPRR6','B0F7RH62GN','B0F7RD3PWM','B0F7RG7F9J','B0F7RF6HV2','B0F7XK4949','B0F7XNJD5W','B0F7XP9D68','B0F7RQF32L','B0F7LZ9WSQ','B0FLDZXN5Q','B0FQ64LXMZ','B0F8P44X2V','B0F8P218M3'],
   hero=(life('kitchen_hL'), ['قهوتك وشواك', 'بترتيب أنيق'],
         ['أكواب ورق سوداء بأغطية وأعواد شوي خشبية', 'للبيت والمقاهي والعزايم']),
   uses=('من التحضير إلى التقديم', [(f'{B}/src/310WWQMoLZL.jpg', 'القهوة'), (f'{B}/src/41CfMLjLhcL.jpg', 'الشوي'),
                                 (f'{B}/srcup/31HWfSnXUsL.jpg', 'القلاية الهوائية'), (f'{B}/src/61KbubUCx4L.jpg', 'العصائر')]),
   rng=('تشكيلة HABBAA للمطبخ والتقديم', [('B0F7RH62GN', 'أكواب ورق بأغطية'), ('B0F7XK4949', 'أعواد شوي خشبية'),
                                       ('B0F7RQF32L', 'ورق القلاية الهوائية'), ('B0F8P44X2V', 'أكياس حفظ بسحاب')]),
   alt=['أكواب HABBAA الورقية السوداء مع أسياخ شوي في مقهى', 'استخدامات منتجات HABBAA في المطبخ',
        'تشكيلة HABBAA من أدوات المطبخ والتقديم']),
 'care6': dict(
   asins=['B0FLWNJ3PP','B0FM8G7CQF','B0FG8J75LY','B0FG8KFP9V','B0F8BK72JT','B0F8BKVSB7','B0F89C1Z8P','B0F897XCMT','B0F895WVVJ','B0F89632K9','B0F895NGZL','B0F7Y4BGL2','B0F894VNJ3'],
   hero=(life('care_hL'), ['روتينك اليومي', 'أسهل وأرتب'],
         ['بخاخات شعر وفوط تجفيف وأقنعة نوم ومرايا', 'للحمام والسفر وروتين كل يوم']),
   uses=('عناية لكل وقت', [(f'{B}/src/71AlIzEuhpL.jpg', 'تجفيف الشعر'), (f'{B}/srcup/31hRy1Sd4YL.jpg', 'وقت النوم'),
                          (f'{B}/src/51jDkwa-iQL.jpg', 'ترطيب الشعر'), (f'{B}/src/41uNaoNKtHL.jpg', 'المكياج')]),
   rng=('تشكيلة HABBAA لروتينك اليومي', [('B0FLWNJ3PP', 'بخاخ شعر 250 مل'), ('B0FG8KFP9V', 'قبعة تجفيف الشعر'),
                                ('B0F895NGZL', 'مروحة يد قابلة للطي'), ('B0F7Y4BGL2', 'مرآة مكياج صغيرة')]),
   alt=['بخاخ شعر HABBAA وقبعة تجفيف على رخام الحمام', 'استخدامات منتجات HABBAA في الروتين اليومي',
        'تشكيلة HABBAA من أدوات الروتين اليومي']),
 'home6': dict(
   asins=['B0F8QGZFXL','B0F8QBH86Z','B0F8P1V9NZ','B0F8BNDDPH','B0F8BPT7XB','B0F7Y3ZPLV','B0CHK6LPDN','B0CHWNSBLM','B0F8QMQ58R'],
   hero=(life('home_hL'), ['يومك أسهل', 'في البيت والطريق'],
         ['مظلة شفافة وأدوات بيت وسيارة', 'لاستخدام يومي عملي']),
   uses=('لكل يوم', [(f'{B}/src/61zSTo+IO-L.jpg', 'تنظيف السيارة'), (f'{B}/src/816zoJ8-dzL.jpg', 'أرضية البيت'),
                    (f'{B}/src/616BbtxXegL.jpg', 'لوحة الملاحظات'), (f'{B}/srcup/21RrdXPx4oL.jpg', 'التصليحات')]),
   rng=('تشكيلة HABBAA للبيت والسيارة', [('B0CHWNSBLM', 'مظلة شفافة'), ('B0CHK6LPDN', 'حامل أكواب للسيارة'),
                                       ('B0F7Y3ZPLV', 'فرشاة تنظيف السيارة'), ('B0F8P1V9NZ', 'طقم مفكات')]),
   alt=['مظلة HABBAA الشفافة في شارع ممطر', 'استخدامات منتجات HABBAA في البيت والسيارة',
        'تشكيلة HABBAA للبيت والسيارة']),
}

if __name__ == '__main__':
    alts = {}
    for k, f in FAM.items():
        for s in f['hero'][1] + f['hero'][2] + [f['uses'][0], f['rng'][0]] + [l for _, l in f['uses'][1]] + [l for _, l in f['rng'][1]] + f['alt']:
            check(s)
        hero(f['hero'][0], f['hero'][1], f['hero'][2], f'{O}/d13-{k}-1-hero')
        L.uses(f['uses'][1], f['uses'][0], f'{O}/d13-{k}-2-uses')
        rng(f['rng'][1], f['rng'][0], f'{O}/d13-{k}-3-feat')
        alts[k] = f['alt']
    json.dump(alts, open(f'{O}/d13-alts.json', 'w'), ensure_ascii=False)
    json.dump({k: f['asins'] for k, f in FAM.items()}, open(f'{O}/d13-asins.json', 'w'))
    print('ok', sum(len(f['asins']) for f in FAM.values()))
