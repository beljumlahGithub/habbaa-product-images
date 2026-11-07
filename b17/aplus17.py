import os, sys, json, re
sys.path.insert(0, '/home/claude/aplus4')
os.environ.setdefault('HB_FONTS', '/home/claude/habbaa-product-images/pipeline/fonts')
import aplus_lib as L
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, '/home/claude/b17')
import gen17 as gen9

B = '/home/claude/b17'; O = f'{B}/aplus'; os.makedirs(O, exist_ok=True)
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
 'food17': dict(
   asins=['B0F7XRG42Z','B0F7XQY9CV','B0F7XRDJWM','B0F7XSMVWT','B0F7XRJKJX','B0F7XRX3XM','B0F7XMRGQY','B0F7XMRT1L','B0F7XMP7L7','B0F7XJLNG1','B0F7XGGW86','B0F7XGZ1MH','B0F7RH51KF','B0F7RGJTCD','B0F7R9YM6F','B0F7R6ZLL8','B0F7R672W9','B0F7RS79SZ','B0F7RV7N2Q','B0F7RQ4DXP','B0F7RQ5W3B','B0F7M23229','B0F7M15CRP','B0F7M1Y6BJ','B0F7M199LJ','B0F7M17DP8','B0F7M195LC','B0F7M3R65V','B0F7LZBP8T','B0F7M2HZ4Z','B0F7M2MNGP'],
   hero=(life('food_hL'), ['تقديم وتغليف', 'لكل طلب سفري'],
         ['علب من قصب السكر وعلب بلاستيك وأكواب ورقية', 'للمطاعم والمقاهي والبيت']),
   uses=('لكل طلب', [(f'{B}/src/B0F7XRX3XM.jpg', 'السلطات والوجبات'), (f'{B}/src/B0F7XMP7L7.jpg', 'البرجر والسندويتش'),
                    (f'{B}/src/B0F7RS79SZ.jpg', 'طلبات المشروبات'), (f'{B}/src/B0F7LZBP8T.jpg', 'وجبات السفري')]),
   rng=('تشكيلة HABBAA للتقديم والسفري', [('B0F7XRDJWM', 'علبة قصب مربعة'), ('B0F7XMRT1L', 'علبة بغطاء متصل'),
                                         ('B0F7RS79SZ', 'حامل 4 أكواب'), ('B0F7M3R65V', 'علبة سوداء بغطاء')]),
   alt=['علب تقديم من قصب السكر وأكواب ورقية على كاونتر مطعم', 'استخدامات علب وأكواب HABBAA للسفري',
        'تشكيلة HABBAA من علب الطعام وحوامل الأكواب']),
 'party17': dict(
   asins=['B0F8JFRZNL','B0F8JBKT24','B0F8JL2NJ3','B0F8JH66NW','B0F8JDN116','B0F8JG4PK9','B0F8JG3XBH','B0F8JFQ9W9','B0F8R24T4K','B0F8QZT17N','B0F8R2772Y','B0F8QXG9VV','B0F8R1RWDZ','B0F8QV4XNY','B0F8QXGFY6','B0F8QWRR8H','B0F8QX65JN','B0F8QXXPF8','B0F8QXYSZD'],
   hero=(life('party_hL'), ['هدايا مرتبة', 'لكل مناسبة'],
         ['أكياس هدايا ورقية بمقابض مجدولة', 'وشموع أرقام للكيك']),
   uses=('لكل مناسبة', [(f'{B}/src/bag_brown.jpg', 'تغليف الهدايا'), (f'{B}/life/party_t1.jpg', 'هدايا الحفلات'),
                       (f'{B}/life/party_t2.jpg', 'توزيعات المناسبات'), (f'{B}/life/party_t3.jpg', 'أكياس للمتاجر')]),
   rng=None,
   alt=['أكياس هدايا ورقية بلون بني وكحلي وأحمر بجانب كيكة', 'استخدامات أكياس الهدايا الورقية من HABBAA']),
}

if __name__ == '__main__':
    alts = {}
    for k, f in FAM.items():
        T = f['hero'][1] + f['hero'][2] + [f['uses'][0]] + [l for _, l in f['uses'][1]] + f['alt']
        if f['rng']: T += [f['rng'][0]] + [l for _, l in f['rng'][1]]
        for s in T: check(s)
        hero(f['hero'][0], f['hero'][1], f['hero'][2], f'{O}/d17-{k}-1-hero')
        L.uses(f['uses'][1], f['uses'][0], f'{O}/d17-{k}-2-uses')
        if f['rng']: rng(f['rng'][1], f['rng'][0], f'{O}/d17-{k}-3-feat')
        alts[k] = f['alt']
    json.dump(alts, open(f'{O}/d17-alts.json', 'w'), ensure_ascii=False)
    json.dump({k: f['asins'] for k, f in FAM.items()}, open(f'{O}/d17-asins.json', 'w'))
    print('ok', sum(len(f['asins']) for f in FAM.values()))
