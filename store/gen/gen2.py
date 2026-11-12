#!/usr/bin/env python3
"""HABBAA brand store v2 — 'من الصبح… للعزيمة' (From breakfast to the majlis).
Signature devices: arch windows, golden-hour photography, time chips, bauhaus shapes."""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

B = os.path.dirname(os.path.abspath(__file__))
HQ = os.path.join(B, 'hq'); CUT = os.path.join(B, 'cut')
OUT = os.path.join(B, 'out2'); os.makedirs(OUT, exist_ok=True)
F = lambda n: os.path.join(B, 'fonts', n)

TEAL = '#008080'; TEAL_D = '#005E5E'; TEAL_DD = '#0B3F3F'; GOLD = '#DBC500'; ORANGE = '#FF7900'
SAGE = '#60A591'; EMERALD = '#02AF80'; AMBER = '#DE802D'; BRICK = '#B64E3E'
TAN = '#D49E5E'; MINT = '#97C6B2'; CREAM = '#FAF5EA'; SAND = '#F1E6D2'; INK = '#123B3B'

# ---------------- type ----------------
def font(lang, w, size):
    if lang == 'ar':
        return ImageFont.truetype(F({'b': 'SST-Bold.ttf', 'm': 'SST-Medium.ttf', 'r': 'SST-Roman.ttf'}[w]), size)
    f = ImageFont.truetype(F('Acumin.otf'), size)
    try: f.set_variation_by_axes([{'b': 720, 'm': 560, 'r': 400}[w], 100])
    except Exception: pass
    return f

def kw(lang): return dict(direction='rtl', language='ar') if lang == 'ar' else {}

def T(d, xy, s, lang, w, size, fill, anchor=None, maxw=None):
    """Draw text; anchor default = start side (rtl -> right)."""
    if anchor is None: anchor = 'rs' if lang == 'ar' else 'ls'
    while maxw and size > 20:
        if d.textlength(s, font=font(lang, w, size), **kw(lang)) <= maxw: break
        size -= 4
    d.text(xy, s, font=font(lang, w, size), fill=fill, anchor=anchor, **kw(lang))
    return d.textbbox(xy, s, font=font(lang, w, size), anchor=anchor, **kw(lang))

def tw(d, s, lang, w, size): return d.textlength(s, font=font(lang, w, size), **kw(lang))

def AN(lang, n):   # numerals
    return n.translate(str.maketrans('0123456789', '٠١٢٣٤٥٦٧٨٩')) if lang == 'ar' else n

# ---------------- images & masks ----------------
def scene(name): return Image.open(os.path.join(HQ, name + '.jpg')).convert('RGB')

def cover(im, size, focus=(0.5, 0.5)):
    return ImageOps.fit(im, size, Image.LANCZOS, centering=focus)

def arch_mask(w, h):
    m = Image.new('L', (w, h), 0); d = ImageDraw.Draw(m)
    d.pieslice((0, 0, w - 1, w - 1), 180, 360, fill=255)
    d.rectangle((0, w // 2, w - 1, h - 1), fill=255)
    return m

def round_mask(w, h, r):
    m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w - 1, h - 1), r, fill=255); return m

def paste_masked(base, im, xy, mask, shadow=True):
    if shadow:
        sh = Image.new('RGBA', base.size, (0, 0, 0, 0))
        sm = Image.new('L', base.size, 0); sm.paste(mask, (xy[0], xy[1] + 22))
        sh.putalpha(sm.point(lambda v: int(v * 0.22))); sh = sh.filter(ImageFilter.GaussianBlur(28))
        base.alpha_composite(sh)
    layer = Image.new('RGBA', base.size, (0, 0, 0, 0)); layer.paste(im.convert('RGBA'), xy, mask)
    base.alpha_composite(layer)

def arch(base, img, x, y, w, h, focus=(0.5, 0.5), outline=None, shadow=True):
    paste_masked(base, cover(img, (w, h), focus), (x, y), arch_mask(w, h), shadow)
    if outline:
        d = ImageDraw.Draw(base)
        d.arc((x - 18, y - 18, x + w + 17, y + w + 17), 180, 360, fill=outline, width=8)
        d.line((x - 14, y + w // 2, x - 14, y + h + 10), fill=outline, width=8)
        d.line((x + w + 13, y + w // 2, x + w + 13, y + h + 10), fill=outline, width=8)

def cutout(name, h):
    im = Image.open(os.path.join(CUT, name + '.png')).convert('RGBA'); im = im.crop(im.getbbox())
    return im.resize((int(im.width * h / im.height), h), Image.LANCZOS)

def logo(kind, h):
    im = Image.open(os.path.join(B, {'color': 'logo_t.png', 'white': 'logo_w.png', 'wg': 'logo_wg.png'}[kind])).convert('RGBA')
    return im.resize((int(im.width * h / im.height), h), Image.LANCZOS)

def gradient_bottom(im, frac=0.45, strength=0.75, color=(10, 40, 40)):
    w, h = im.size; g = Image.new('L', (1, h), 0)
    for y in range(h):
        t = (y - h * (1 - frac)) / (h * frac); g.putpixel((0, y), int(255 * strength * max(0, min(1, t)) ** 1.4))
    ov = Image.new('RGBA', (w, h), color + (0,)); ov.putalpha(g.resize((w, h)))
    out = im.convert('RGBA'); out.alpha_composite(ov); return out

def gradient_side(im, side='left', frac=0.55, strength=0.8, color=(10, 40, 40)):
    w, h = im.size; g = Image.new('L', (w, 1), 0)
    for x in range(w):
        t = (w * frac - x) / (w * frac) if side == 'left' else (x - w * (1 - frac)) / (w * frac)
        g.putpixel((x, 0), int(255 * strength * max(0, min(1, t)) ** 1.3))
    ov = Image.new('RGBA', (w, h), color + (0,)); ov.putalpha(g.resize((w, h)))
    out = im.convert('RGBA'); out.alpha_composite(ov); return out

# ---------------- brand elements ----------------
def chip(d, x, y, text, lang, size=46, fg=INK, bg=GOLD, anchor_right=False):
    w = int(tw(d, text, lang, 'b', size)) + size * 1.4; h = int(size * 1.9)
    x0 = x - w if anchor_right else x
    d.rounded_rectangle((x0, y, x0 + w, y + h), h // 2, fill=bg)
    d.text((x0 + w / 2, y + h / 2 + size * 0.06), text, font=font(lang, 'b', size), fill=fg, anchor='mm', **kw(lang))
    return (x0, y, x0 + w, y + h)

def cta(d, x, y, text, lang, size=50, fg='white', bg=TEAL, anchor_right=False, arrow=True):
    w = int(tw(d, text, lang, 'b', size)) + size * 2.6; h = int(size * 1.9)
    x0 = x - w if anchor_right else x
    d.rounded_rectangle((x0, y, x0 + w, y + h), h // 2, fill=bg)
    ar = lang == 'ar'; cy = y + h / 2; a = size * 0.32
    tx = x0 + w / 2 + (size * 0.45 if ar else -size * 0.45)
    d.text((tx, cy + size * 0.06), text, font=font(lang, 'b', size), fill=fg, anchor='mm', **kw(lang))
    ax = x0 + size * 0.95 if ar else x0 + w - size * 0.95
    if ar: d.line([(ax + a, cy - a), (ax, cy), (ax + a, cy + a)], fill=fg, width=max(4, size // 9), joint='curve')
    else: d.line([(ax - a, cy - a), (ax, cy), (ax - a, cy + a)], fill=fg, width=max(4, size // 9), joint='curve')
    return (x0, y, x0 + w, y + h)

def sun(d, cx, cy, r, col): d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col)

def qcirc(d, x, y, r, col, corner='br'):
    # quarter circle whose centre is (x, y)
    a = {'br': (0, 90), 'bl': (90, 180), 'tl': (180, 270), 'tr': (270, 360)}[corner]
    d.pieslice((x - r, y - r, x + r, y + r), a[0], a[1], fill=col)

def stripes(d, x, y, w, h, col, n=8, vertical=False):
    for i in range(n):
        if vertical: d.rectangle((x + i * w / n, y, x + i * w / n + w / (2 * n), y + h), fill=col)
        else: d.rectangle((x, y + i * h / n, x + w, y + i * h / n + h / (2 * n)), fill=col)

def label_block(base, lang, title, sub=None, cta_text=None, pad=70, size=96, align_bottom=True, fg='white'):
    """Title + sub + CTA on the start side of a dark-graded image."""
    d = ImageDraw.Draw(base); W, H = base.size
    x = W - pad if lang == 'ar' else pad
    y = H - pad
    if cta_text:
        bb = cta(d, x, y - 112, cta_text, lang, 44, INK, GOLD, anchor_right=(lang == 'ar')); y = bb[1] - 34
    if sub:
        T(d, (x, y), sub, lang, 'r', int(size * 0.5), fg, maxw=W - 2 * pad); y -= int(size * 0.5) + 30
    T(d, (x, y), title, lang, 'b', size, fg, maxw=W - 2 * pad)

# ---------------- copy ----------------
C = {
 'slogan': ('من الصبح… للعزيمة', 'From breakfast to the majlis'),
 'slogan_sub': ('كل ما يحتاجه يومك في البيت والمناسبات، في مكان واحد', 'Everything your day needs, at home and for every occasion'),
 'shop_best': ('تسوّق الأكثر مبيعاً', 'Shop best sellers'),
 'shop': ('تسوّق', 'Shop'),
 'shop_now': ('تسوّق الآن', 'Shop now'),
 'day': ('يومك مع هبّة', 'A day with HABBAA'),
 'day_sub': ('من أول فنجال قهوة الصبح… لين آخر الليل', 'From the first morning coffee to the end of the night'),
 'corners': ('تسوّق حسب الركن', 'Shop by corner'),
 'best': ('الأكثر هبّة', 'Most loved'),
 'best_sub': ('اختيارات عملائنا هذا الأسبوع', "What our customers are choosing"),
 'occ': ('لكل مناسبة… هبّة', 'An occasion for everything'),
}
def c(k, lang): return C[k][0] if lang == 'ar' else C[k][1]

TIMES = {
 't1': ('7:00', 'ص', 'AM', 'فطور البيت', 'Breakfast at home', 'ترمس، حافظات، وأدوات مطبخ', 'Flasks, containers and kitchen tools'),
 't2': ('10:00', 'ص', 'AM', 'دراسة وشغل', 'Study & work', 'ورق، أقلام، ومقصات', 'Paper, pencils and scissors'),
 't3': ('4:00', 'م', 'PM', 'الطلعة', 'Out & about', 'مظلات ومراوح للجو الحار', 'Umbrellas and fans for the sun'),
 't4': ('8:00', 'م', 'PM', 'العزيمة', 'The majlis', 'ضيافة كاملة: ترامس، صواني، وأكواب', 'Hosting made easy: flasks, trays and cups'),
 't5': ('11:00', 'م', 'PM', 'آخر الليل', 'Late night', 'ترتيب البيت قبل النوم', 'Tidy up before bed'),
}
def tchip(lang, k):
    t, a, e = TIMES[k][0], TIMES[k][1], TIMES[k][2]
    return f'{AN(lang, t)} {a}' if lang == 'ar' else f'{t} {e}'

CORN = [  # key, scene, AR, EN, colour, focus
 ('party', 'c_party', 'الحفلات والمناسبات', 'Party & Occasions', ORANGE, (0.5, 0.5)),
 ('pack', 'c_pack', 'التغليف والهدايا', 'Packaging & Gifts', GOLD, (0.5, 0.5)),
 ('home', 'c_home', 'البيت والتنظيم', 'Home & Organising', EMERALD, (0.5, 0.5)),
 ('cups', 'c_cups', 'الكاسات والضيافة', 'Cups & Serving', TEAL, (0.5, 0.6)),
 ('kitchen', 'c_kitchen', 'المطبخ وحفظ الطعام', 'Kitchen & Storage', SAGE, (0.4, 0.6)),
 ('station', 'c_station', 'القرطاسية', 'Stationery & Crafts', AMBER, (0.6, 0.6)),
 ('clean', 'c_clean', 'التنظيف والحمّام', 'Cleaning & Bath', MINT, (0.5, 0.45)),
 ('toys', 'c_toys', 'الألعاب والترفيه', 'Toys & Games', BRICK, (0.6, 0.5)),
 ('travel', 'c_travel', 'السفر والرحلات', 'Travel & Outdoor', TAN, (0.5, 0.6)),
]
def corner(k): return next(x for x in CORN if x[0] == k)

# ---------------- tiles ----------------
def header(lang, W=3000, H=600):
    img = Image.new('RGBA', (W, H), TEAL); d = ImageDraw.Draw(img); ar = lang == 'ar'
    # arch windows on the end side with real scenes
    ax = 120 if ar else W - 120 - 3 * 250 - 2 * 40
    for i, (s, f) in enumerate([('t1_morning', (0.4, 0.6)), ('t4_majlis', (0.5, 0.7)), ('c_party', (0.5, 0.55))]):
        hh = [430, 500, 430][i]
        arch(img, scene(s), ax + i * 290, H - hh, 250, hh, f, shadow=False)
    sun(d, (W - 260) if ar else 260, 120, 190, GOLD)
    stripes(d, (W - 560) if ar else 360, 360, 200, 240, '#ffffff', 8)
    lg = logo('wg', 250)
    if ar:
        img.alpha_composite(lg, (W - 520 - lg.width, (H - lg.height) // 2 - 10))
        x = W - 520 - lg.width - 70
        d.line((x + 35, 200, x + 35, 400), fill='white', width=5)
        T(d, (x, 290), c('slogan', lang), lang, 'b', 96, 'white')
        T(d, (x, 380), 'حفلات  |  ضيافة  |  تغليف  |  مطبخ  |  تنظيم', lang, 'r', 52, GOLD)
    else:
        img.alpha_composite(lg, (520, (H - lg.height) // 2 - 10))
        x = 520 + lg.width + 70
        d.line((x - 35, 200, x - 35, 400), fill='white', width=5)
        T(d, (x, 290), c('slogan', lang), lang, 'b', 80, 'white', maxw=1950 - x)
        T(d, (x, 380), 'Party  |  Serving  |  Packaging  |  Kitchen  |  Home', lang, 'r', 46, GOLD, maxw=1950 - x)
    return img

def hero(lang, W=3000, H=1500):
    img = Image.new('RGBA', (W, H), CREAM); d = ImageDraw.Draw(img); ar = lang == 'ar'
    # three arches = the day: morning / majlis / party
    aw = 500; gap = 50
    xs = [W - 120 - aw * 3 - gap * 2 + i * (aw + gap) for i in range(3)] if not ar else [120 + i * (aw + gap) for i in range(3)]
    hs = [1060, 1260, 1060]
    sun(d, xs[1] + aw // 2, 240 + 120, 420, GOLD)
    for i, (s, f) in enumerate([('t1_morning', (0.35, 0.6)), ('t4_majlis', (0.45, 0.75)), ('c_party', (0.5, 0.6))]):
        arch(img, scene(s), xs[i], H - 120 - hs[i], aw, hs[i], f)
    # floor line
    d.rectangle((0, H - 120, W, H), fill=TEAL)
    stripes(d, 0, H - 120, W, 120, TEAL_D, 6, vertical=True)
    # text block
    tx = W - 160 if ar else 160
    lg = logo('color', 230)
    img.alpha_composite(lg, (tx - lg.width, 170) if ar else (tx, 170))
    l1, l2 = ('من الصبح…', 'للعزيمة') if ar else ('From breakfast', 'to the majlis')
    T(d, (tx, 620), l1, lang, 'b', 150, TEAL_DD, maxw=1050)
    T(d, (tx, 800), l2, lang, 'b', 150, TEAL, maxw=1050)
    if not ar:
        d.rectangle((0, 0, 0, 0))
    T(d, (tx, 920), c('slogan_sub', lang), lang, 'r', 50, INK, maxw=1000)
    cta(d, tx, 1010, c('shop_best', lang), lang, 54, 'white', TEAL, anchor_right=ar)
    # small bauhaus accents
    qcirc(d, (W // 2 + 60) if not ar else (W // 2 - 60), H - 120, 150, ORANGE, 'tl' if not ar else 'tr')
    return img

def strip(lang, key, subkey=None, W=3000, H=520, bg=CREAM, accent=TEAL, deco='arch'):
    img = Image.new('RGBA', (W, H), bg); d = ImageDraw.Draw(img); ar = lang == 'ar'
    x = W - 170 if ar else 170
    T(d, (x, 300), c(key, lang), lang, 'b', 130, TEAL_DD)
    if subkey: T(d, (x, 400), c(subkey, lang), lang, 'r', 54, INK)
    ex = 170 if ar else W - 170 - 620
    if deco == 'arch':
        sun(d, ex + 380, 260, 140, GOLD)
        d.pieslice((ex, 120, ex + 260, 380), 180, 360, fill=accent); d.rectangle((ex, 250, ex + 260, 440), fill=accent)
        stripes(d, ex + 300, 330, 220, 110, ORANGE, 6)
    elif deco == 'palette':
        cols = [ORANGE, GOLD, EMERALD, TEAL, SAGE, AMBER, MINT, BRICK, TAN]
        for i, cl in enumerate(cols):
            x = ex + i * 70; d.pieslice((x, 130, x + 60, 190), 180, 360, fill=cl); d.rectangle((x, 160, x + 60, 340), fill=cl)
    elif deco == 'star':
        sun(d, ex + 380, H // 2, 170, GOLD); sun(d, ex + 380, H // 2, 130, CREAM)
        d.text((ex + 380, H // 2 + 10), AN(lang, '1'), font=font(lang, 'b', 170), fill=TEAL_DD, anchor='mm')
        stripes(d, ex + 80, H // 2 - 60, 140, 120, ORANGE, 6, vertical=True)
    elif deco == 'confetti':
        import random; rnd = random.Random(4)
        for i in range(26):
            x = ex + rnd.randint(0, 600); y = rnd.randint(60, H - 60); r = rnd.randint(8, 22)
            d.ellipse((x - r, y - r, x + r, y + r), fill=rnd.choice([ORANGE, GOLD, TEAL, EMERALD, BRICK]))
        cx, cy, r = ex + 470, H // 2, 120
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GOLD); d.ellipse((cx - r + 50, cy - r - 20, cx + r + 50, cy + r - 20), fill=bg)
    return img

def timeline_strip(lang, W=3000, H=640):
    img = strip(lang, 'day', 'day_sub', W, H)
    d = ImageDraw.Draw(img); ar = lang == 'ar'
    # dots line under the text: times
    keys = ['t1', 't2', 't3', 't4', 't5']
    y = 540; x0, x1 = (W - 170 - 1500, W - 170) if ar else (170, 170 + 1500)
    d.line((x0, y, x1, y), fill=TEAL, width=6)
    for i, k in enumerate(keys):
        x = (x1 - i * 375) if ar else (x0 + i * 375)
        sun(d, x, y, 22, [GOLD, AMBER, ORANGE, TEAL, TEAL_DD][i])
        d.text((x, y + 60), tchip(lang, k), font=font(lang, 'm', 40), fill=INK, anchor='mm', **kw(lang))
    return img

def moment(lang, k, scene_name, size, focus=(0.5, 0.5), title_size=None):
    W, H = size; ar = lang == 'ar'
    im = gradient_bottom(cover(scene(scene_name), (W, H), focus), 0.55, 0.85)
    d = ImageDraw.Draw(im)
    pad = int(min(W, H) * 0.07)
    chip(d, (W - pad) if ar else pad, pad, tchip(lang, k), lang, int(min(W, H) * 0.035), INK, GOLD, anchor_right=ar)
    ts = title_size or int(min(W, H) * 0.085)
    t = TIMES[k]
    label_block(im, lang, t[3] if ar else t[4], t[5] if ar else t[6], c('shop', lang), pad=pad, size=ts)
    return im

def corner_tile(lang, k, size, focus=None, title_size=None, style='photo'):
    key, sc, ar_t, en_t, col, f = corner(k); W, H = size; ar = lang == 'ar'
    if style == 'arch':   # coloured ground + arch window (small tiles)
        im = Image.new('RGBA', (W, H), col); d = ImageDraw.Draw(im)
        aw = int(W * 0.62); ah = int(H * 0.66)
        sun(d, (W * 0.22) if ar else (W * 0.78), H * 0.2, W * 0.16, CREAM if col != CREAM else GOLD)
        arch(im, scene(sc), (W - aw) // 2, int(H * 0.08), aw, ah, focus or f)
        tc = INK if col in (GOLD, MINT, TAN) else 'white'
        d.text((W / 2, H * 0.86), ar_t if ar else en_t, font=font(lang, 'b', int(W * 0.075)), fill=tc, anchor='mm', **kw(lang))
        return im
    band = int(H * (0.2 if H == W else 0.28))
    im = Image.new('RGBA', (W, H), col)
    im.paste(cover(scene(sc), (W, H - band), focus or f), (0, 0))
    d = ImageDraw.Draw(im); pad = int(W * 0.05)
    tc = INK if col in (GOLD, MINT, TAN) else 'white'
    ts = title_size or int(band * 0.42)
    x = W - pad if ar else pad
    T(d, (x, H - band // 2 + ts * 0.36), ar_t if ar else en_t, lang, 'b', ts, tc, maxw=W - 2 * pad - 420)
    bx = pad if ar else W - pad
    cta(d, bx, H - band // 2 - int(ts * 0.42), c('shop', lang), lang, int(ts * 0.45), col if tc == 'white' else 'white', 'white' if tc == 'white' else INK, anchor_right=not ar)
    return im

def care_tile(lang, W=1500, H=750):
    im = Image.new('RGBA', (W, H), TEAL_D); d = ImageDraw.Draw(im); ar = lang == 'ar'
    sun(d, (380) if ar else W - 380, H // 2, 260, TEAL)
    sc = cutout('scissors', 520); im.alpha_composite(sc, ((380 - sc.width // 2) if ar else (W - 380 - sc.width // 2), (H - sc.height) // 2))
    x = W - 90 if ar else 90
    T(d, (x, 330), 'أدوات العناية' if ar else 'Personal care tools', lang, 'b', 96, 'white', maxw=W - 820)
    T(d, (x, 420), 'مقصات دقيقة وأدوات يومية' if ar else 'Precision scissors and daily tools', lang, 'r', 46, GOLD, maxw=W - 820)
    cta(d, x, 480, c('shop', lang), lang, 44, INK, GOLD, anchor_right=ar)
    return im

def tomorrow_tile(lang, W=1500, H=750):
    im = Image.new('RGBA', (W, H), TEAL); d = ImageDraw.Draw(im); ar = lang == 'ar'
    qcirc(d, 0 if not ar else W, H, 420, TEAL_D, 'tr' if not ar else 'tl')
    sun(d, (W - 250) if not ar else 250, 210, 120, GOLD)
    stripes(d, (W - 420) if not ar else 180, 420, 240, 200, '#ffffff', 7)
    lg = logo('wg', 170)
    x = W - 110 if ar else 110
    img_x = (x - lg.width) if ar else x
    im.alpha_composite(lg, (img_x, 120))
    T(d, (x, 450), 'وبكرة… يوم جديد' if ar else 'And tomorrow, a new day', lang, 'b', 92, 'white', maxw=W - 560)
    T(d, (x, 535), 'هبّة معك في كل لحظة' if ar else 'HABBAA, for every moment', lang, 'r', 50, GOLD, maxw=W - 560)
    return im

def occasion(lang, k, W=750, H=750):
    ar = lang == 'ar'
    data = {
     'bday': (ORANGE, 'c_party', (0.5, 0.45), 'عيد ميلاد', 'Birthdays'),
     'majlis': (TEAL, 't4_majlis', (0.45, 0.7), 'العزايم', 'Gatherings'),
     'school': (AMBER, 't2_study', (0.45, 0.65), 'رجعة المدارس', 'Back to school'),
     'ramadan': (TEAL_DD, None, None, 'رمضان والعيد', 'Ramadan & Eid'),
    }[k]
    col, sc, f, at, et = data
    im = Image.new('RGBA', (W, H), col); d = ImageDraw.Draw(im)
    aw, ah = 440, 470
    if sc:
        arch(im, scene(sc), (W - aw) // 2, 70, aw, ah, f, outline=CREAM)
    else:  # ramadan: crescent + stars in an arch
        m = arch_mask(aw, ah); a = Image.new('RGBA', (aw, ah), TEAL); a.putalpha(m)
        im.alpha_composite(a, ((W - aw) // 2, 70)); d = ImageDraw.Draw(im)
        cx, cy, r = W // 2, 70 + 270, 120
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GOLD); d.ellipse((cx - r + 55, cy - r - 25, cx + r + 55, cy + r - 25), fill=TEAL)
        for sx, sy, sr in [(cx + 110, cy - 120, 14), (cx + 150, cy - 40, 9), (cx - 140, cy + 90, 10)]:
            d.ellipse((sx - sr, sy - sr, sx + sr, sy + sr), fill='white')
        d.arc(((W - aw) // 2 - 18, 52, (W + aw) // 2 + 17, 70 + aw + 17), 180, 360, fill=CREAM, width=8)
        d.line(((W - aw) // 2 - 14, 70 + aw // 2, (W - aw) // 2 - 14, 70 + ah + 10), fill=CREAM, width=8)
        d.line(((W + aw) // 2 + 13, 70 + aw // 2, (W + aw) // 2 + 13, 70 + ah + 10), fill=CREAM, width=8)
    d.text((W / 2, 640), at if ar else et, font=font(lang, 'b', 64), fill='white', anchor='mm', **kw(lang))
    return im

def why(lang, W=3000, H=760):
    img = Image.new('RGBA', (W, H), TEAL_DD); d = ImageDraw.Draw(img); ar = lang == 'ar'
    items = [
        (GOLD, 'تشكيلة واسعة', 'Wide range', 'للبيت والمناسبات', 'For home and occasions', 0),
        (ORANGE, 'كميات تناسبك', 'Pack sizes for you', 'للعائلة والضيافة', 'For families and gatherings', 1),
        (EMERALD, 'توصيل سريع', 'Fast delivery', 'عبر أمازون', 'Delivered via Amazon', 2),
    ]
    if ar: items = items[::-1]
    colw = W // 3
    for i, (col, a1, e1, a2, e2, ic) in enumerate(items):
        cx = colw * i + colw // 2
        # arch badge
        aw, ah = 240, 270
        a = Image.new('RGBA', (aw, ah), col); a.putalpha(arch_mask(aw, ah)); img.alpha_composite(a, (cx - aw // 2, 90)); d = ImageDraw.Draw(img)
        icon(d, ic, cx, 245, INK)
        d.text((cx, 500), a1 if ar else e1, font=font(lang, 'b', 82), fill='white', anchor='mm', **kw(lang))
        d.text((cx, 590), a2 if ar else e2, font=font(lang, 'r', 50), fill=GOLD, anchor='mm', **kw(lang))
        if i: d.line((colw * i, 170, colw * i, 620), fill=TEAL, width=4)
    return img

def icon(d, k, cx, cy, w):
    if k == 0:
        for dx in (-36, 36):
            for dy in (-36, 36): d.rounded_rectangle((cx + dx - 28, cy + dy - 28, cx + dx + 28, cy + dy + 28), 10, fill=w)
    elif k == 1:
        d.rounded_rectangle((cx - 70, cy + 5, cx - 5, cy + 70), 8, fill=w); d.rounded_rectangle((cx + 5, cy + 5, cx + 70, cy + 70), 8, fill=w)
        d.rounded_rectangle((cx - 33, cy - 62, cx + 33, cy - 2), 8, fill=w)
    else:
        d.rounded_rectangle((cx - 80, cy - 45, cx + 20, cy + 30), 8, fill=w)
        d.polygon([(cx + 25, cy - 25), (cx + 60, cy - 25), (cx + 82, cy + 5), (cx + 82, cy + 30), (cx + 25, cy + 30)], fill=w)
        for wx in (cx - 50, cx + 50): d.ellipse((wx - 20, cy + 25, wx + 20, cy + 65), fill=w)

def majlis_full(lang, W=3000, H=1500):
    ar = lang == 'ar'
    im = gradient_side(cover(scene('t4_majlis'), (W, H), (0.5, 0.6)), 'right' if ar else 'left', 0.5, 0.8)
    d = ImageDraw.Draw(im); pad = 170
    x = W - pad if ar else pad
    chip(d, x, 200, tchip(lang, 't4'), lang, 58, INK, GOLD, anchor_right=ar)
    T(d, (x, 520), TIMES['t4'][3] if ar else TIMES['t4'][4], lang, 'b', 190, 'white')
    T(d, (x, 640), TIMES['t4'][5] if ar else TIMES['t4'][6], lang, 'r', 62, 'white', maxw=1250)
    T(d, (x, 740), 'اضغط على المنتجات للتسوّق مباشرة' if ar else 'Tap the products to shop the scene', lang, 'm', 48, GOLD, maxw=1250)
    return im

def save(img, name):
    p = os.path.join(OUT, name); img.convert('RGB').save(p, quality=92); return p

def build(lang):
    L = lang
    save(header(L), f'{L}_01_header_3000x600.jpg')
    save(hero(L), f'{L}_02_hero_3000x1500.jpg')
    save(timeline_strip(L), f'{L}_03_strip_day_3000x640.jpg')
    save(moment(L, 't1', 't1_morning', (1500, 1500), (0.45, 0.6)), f'{L}_04a_t1_large_1500.jpg')
    save(moment(L, 't2', 't2_study', (1500, 750), (0.5, 0.72)), f'{L}_04b_t2_medium_1500x750.jpg')
    save(moment(L, 't3', 't3_outing', (1500, 750), (0.5, 0.7)), f'{L}_04c_t3_medium_1500x750.jpg')
    save(majlis_full(L), f'{L}_05_t4_majlis_shoppable_3000x1500.jpg')
    save(moment(L, 't5', 'bedroom_wide', (1500, 750), (0.6, 0.6)), f'{L}_06a_t5_medium_1500x750.jpg')
    save(tomorrow_tile(L), f'{L}_06b_tomorrow_medium_1500x750.jpg')
    save(strip(L, 'corners', None, 3000, 460, CREAM, ORANGE, 'palette'), f'{L}_07_strip_corners_3000x460.jpg')
    save(corner_tile(L, 'party', (1500, 1500)), f'{L}_08a_party_large_1500.jpg')
    save(corner_tile(L, 'pack', (1500, 750)), f'{L}_08b_pack_medium_1500x750.jpg')
    save(corner_tile(L, 'home', (1500, 750)), f'{L}_08c_home_medium_1500x750.jpg')
    for i, k in enumerate(['cups', 'kitchen', 'station', 'clean']):
        save(corner_tile(L, k, (750, 750), style='arch'), f'{L}_09{"abcd"[i]}_{k}_small_750.jpg')
    save(corner_tile(L, 'travel', (1500, 1500), (0.5, 0.6)), f'{L}_10a_travel_large_1500.jpg')
    save(corner_tile(L, 'toys', (1500, 750)), f'{L}_10b_toys_medium_1500x750.jpg')
    save(care_tile(L), f'{L}_10c_care_medium_1500x750.jpg')
    save(strip(L, 'best', 'best_sub', 3000, 520, SAND, GOLD, 'star'), f'{L}_11_strip_best_3000x520.jpg')
    save(strip(L, 'occ', None, 3000, 460, CREAM, TEAL, 'confetti'), f'{L}_12_strip_occ_3000x460.jpg')
    for i, k in enumerate(['bday', 'majlis', 'school', 'ramadan']):
        save(occasion(L, k), f'{L}_13{"abcd"[i]}_occ_{k}_750.jpg')
    save(why(L), f'{L}_14_why_3000x760.jpg')

if __name__ == '__main__':
    for L in (sys.argv[1:] or ['ar', 'en']): build(L)
    print('ok', len(os.listdir(OUT)))
