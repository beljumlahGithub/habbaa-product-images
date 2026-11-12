#!/usr/bin/env python3
"""HABBAA Amazon brand store asset generator (brand colours, SST Arabic + Acumin)."""
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

B = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(B, 'out'); os.makedirs(OUT, exist_ok=True)
F = lambda n: os.path.join(B, 'fonts', n)

TEAL = '#008080'; TEAL_D = '#006666'; GOLD = '#DBC500'; ORANGE = '#FF7900'
SAGE = '#60A591'; EMERALD = '#02AF80'; AMBER = '#DE802D'; BRICK = '#B64E3E'
TAN = '#D49E5E'; MINT = '#97C6B2'; CREAM = '#FBF8F1'; INK = '#123B3B'

def font(lang, w, size):
    if lang == 'ar':
        return ImageFont.truetype(F({'b': 'SST-Bold.ttf', 'm': 'SST-Medium.ttf', 'r': 'SST-Roman.ttf'}[w]), size)
    f = ImageFont.truetype(F('Acumin.otf'), size)
    try:
        f.set_variation_by_axes([{'b': 700, 'm': 560, 'r': 400}[w], 100])
    except Exception:
        pass
    return f

def text(d, xy, s, lang, w, size, fill, anchor='mm'):
    f = font(lang, w, size)
    kw = dict(direction='rtl', language='ar') if lang == 'ar' else {}
    d.text(xy, s, font=f, fill=fill, anchor=anchor, **kw)
    return d.textbbox(xy, s, font=f, anchor=anchor, **kw)

def fit_text(d, xy, s, lang, w, size, fill, maxw, anchor='mm'):
    while size > 20:
        f = font(lang, w, size)
        kw = dict(direction='rtl', language='ar') if lang == 'ar' else {}
        bb = d.textbbox(xy, s, font=f, anchor=anchor, **kw)
        if bb[2] - bb[0] <= maxw:
            break
        size -= 4
    return text(d, xy, s, lang, w, size, fill, anchor)

def logo(kind, h):
    im = Image.open(os.path.join(B, {'color': 'logo_t.png', 'white': 'logo_w.png', 'wg': 'logo_wg.png'}[kind])).convert('RGBA')
    return im.resize((int(im.width * h / im.height), h), Image.LANCZOS)

def product(asin, box, crop=None):
    im = Image.open(os.path.join(B, 'src', asin + '.jpg')).convert('RGB')
    if crop:
        w, h = im.size
        im = im.crop((int(crop[0]*w), int(crop[1]*h), int(crop[2]*w), int(crop[3]*h)))
    im.thumbnail(box, Image.LANCZOS)
    return im

def rounded(size, r, fill):
    m = Image.new('L', size, 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, size[0]-1, size[1]-1), r, fill=255)
    tile = Image.new('RGBA', size, fill)
    tile.putalpha(m)
    return tile

def shadow(canvas, box, r, off=18, blur=30, alpha=60):
    sh = Image.new('RGBA', canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle((box[0], box[1]+off, box[2], box[3]+off), r, fill=(0, 0, 0, alpha))
    sh = sh.filter(ImageFilter.GaussianBlur(blur))
    canvas.alpha_composite(sh)

def card(canvas, box, asin, r=60, crop=None, pad=0.08, bg='white', fit='contain'):
    """White rounded card with the product photo inside."""
    x0, y0, x1, y1 = box; w, h = x1-x0, y1-y0
    shadow(canvas, box, r)
    c = rounded((w, h), r, bg)
    im = Image.open(os.path.join(B, 'src', asin + '.jpg')).convert('RGB')
    if crop:
        iw, ih = im.size
        im = im.crop((int(crop[0]*iw), int(crop[1]*ih), int(crop[2]*iw), int(crop[3]*ih)))
    if fit == 'cover':
        im = ImageOps.fit(im, (w, h), Image.LANCZOS)
        m = Image.new('L', (w, h), 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, w-1, h-1), r, fill=255)
        c.paste(im, (0, 0), m)
    else:
        p = int(min(w, h) * pad)
        im.thumbnail((w-2*p, h-2*p), Image.LANCZOS)
        c.paste(im, ((w-im.width)//2, (h-im.height)//2))
    canvas.alpha_composite(c, (x0, y0))

# ---------- brand geometric pattern (from the HABBAA brand board) ----------
def qcircle(d, x, y, s, col, corner):
    # quarter circle filling square (x,y,s) anchored at corner
    cx = {'tl': x, 'tr': x+s, 'bl': x, 'br': x+s}[corner]
    cy = {'tl': y, 'tr': y, 'bl': y+s, 'br': y+s}[corner]
    d.pieslice((cx-s, cy-s, cx+s, cy+s), 0, 360, fill=col)

def pattern_block(img, x, y, s, kind, c1, c2, bg=None):
    """Draw one s x s pattern cell clipped to the cell."""
    cell = Image.new('RGBA', (s, s), bg or (0, 0, 0, 0))
    d = ImageDraw.Draw(cell)
    if kind == 'circle':
        d.ellipse((0, 0, s, s), fill=c1)
    elif kind == 'q':
        d.pieslice((-s, 0, s, 2*s), 270, 360, fill=c1)
    elif kind == 'q2':
        d.pieslice((0, 0, 2*s, 2*s), 180, 270, fill=c1)
    elif kind == 'half':
        d.rectangle((0, s//2, s, s), fill=c2); d.pieslice((0, 0, s, s), 180, 360, fill=c1)
    elif kind == 'hstripe':
        n = 9
        for i in range(n):
            d.rectangle((0, i*s/n, s, i*s/n + s/(2*n)), fill=c1)
    elif kind == 'vstripe':
        n = 9
        for i in range(n):
            d.rectangle((i*s/n, 0, i*s/n + s/(2*n), s), fill=c1)
    elif kind == 'diag':
        for i in range(-s, 2*s, s//7):
            d.polygon([(i, 0), (i+s//14, 0), (i+s//14-s, s), (i-s, s)], fill=c1)
    elif kind == 'tri':
        d.polygon([(0, 0), (s, 0), (s, s)], fill=c1); d.polygon([(0, 0), (0, s), (s, s)], fill=c2)
    elif kind == 'dots':
        d.rectangle((0, 0, s, s), fill=c2)
        for cx in (0.3, 0.7):
            for cy in (0.3, 0.7):
                r = s*0.09; d.ellipse((cx*s-r, cy*s-r, cx*s+r, cy*s+r), fill=c1)
    elif kind == 'four':
        h = s//2
        for i, col in enumerate([c1, c2, c2, c1]):
            ox, oy = (i % 2)*h, (i//2)*h
            d.ellipse((ox, oy, ox+h, oy+h), fill=col)
    img.alpha_composite(cell, (x, y))

PAL = [GOLD, ORANGE, SAGE, EMERALD, AMBER, TEAL, BRICK, TAN, MINT]

def pattern_strip(img, x, y, s, cells):
    for i, (kind, c1, c2, bg) in enumerate(cells):
        pattern_block(img, x + i*s, y, s, kind, c1, c2, bg)

# ---------- assets ----------
CATS = [
    # key, AR, EN, colour, asin, crop, fit
    ('party',  'الحفلات والمناسبات',   'Party & Occasions',    ORANGE,  'B0F8QM9JGJ', None, 'cover'),
    ('cups',   'الكاسات والضيافة',     'Cups & Serving',       TEAL,    'B0CHF69K3C', (0, 0, 1, .78), 'cover'),
    ('pack',   'التغليف والهدايا',     'Packaging & Gifts',    GOLD,    'B0F8JL2NJ3', None, 'contain'),
    ('kitchen','المطبخ وحفظ الطعام',   'Kitchen & Storage',    SAGE,    'B0FHFXK464', None, 'contain'),
    ('home',   'البيت والتنظيم',       'Home & Organisation',  EMERALD, 'B0FVF7MQLG', None, 'contain'),
    ('clean',  'التنظيف والحمّام',      'Cleaning & Bath',      MINT,    'B0F8NZ73G7', (0, 0, 1, .80), 'cover'),
    ('station','القرطاسية والأشغال',   'Stationery & Crafts',  AMBER,   'B0FF3MN8NX', None, 'contain'),
    ('toys',   'الألعاب والترفيه',     'Toys & Games',         BRICK,   'B0F7LLS5LM', None, 'contain'),
    ('travel', 'السفر والرحلات',       'Travel & Outdoor',     TAN,     'B0CGRJJGFZ', None, 'contain'),
    ('care',   'أدوات العناية',        'Personal Care Tools',  TEAL_D,  'B0GWYBYW48', None, 'contain'),
]

def light(col):
    return col in (GOLD, MINT, TAN)

def cat_tile(c, lang, S=1500):
    key, ar, en, col, asin, crop, fit = c
    img = Image.new('RGBA', (S, S), col)
    d = ImageDraw.Draw(img)
    # pattern corner (top-left for EN, top-right for AR)
    s = 220
    others = [p for p in PAL if p != col]
    cells = [('q', others[0], None, None), ('circle', others[1], None, None), ('hstripe', 'white', None, None)]
    if lang == 'ar':
        cells = cells[::-1]
    px = 0 if lang == 'en' else S - 3*s
    pattern_strip(img, px, 0, s, cells)
    # product card
    card(img, (150, 300, S-150, S-330), asin, r=70, crop=crop, fit=fit)
    # label
    tc = INK if light(col) else 'white'
    label = ar if lang == 'ar' else en
    fit_text(d, (S//2, S-165), label, lang, 'b', 118 if lang == 'ar' else 110, tc, S-200)
    return img

def header(lang, W=3000, H=600):
    img = Image.new('RGBA', (W, H), TEAL)
    s = 300
    left = [('q', GOLD, None, None), ('hstripe', 'white', None, TEAL), ('circle', ORANGE, None, None)]
    right = [('dots', 'white', SAGE, None), ('half', GOLD, ORANGE, None), ('q2', EMERALD, None, None)]
    for i, cl in enumerate(left):
        pattern_block(img, (i % 2)*s if i < 2 else 0, (i//2)*s, s, *cl) if False else None
    pattern_strip(img, 0, 0, s, left[:2]); pattern_strip(img, 0, s, s, [left[2], ('vstripe', GOLD, None, None)])
    pattern_strip(img, W-2*s, 0, s, right[:2]); pattern_strip(img, W-2*s, s, s, [right[2], ('tri', AMBER, GOLD, None)])
    d = ImageDraw.Draw(img)
    lg = logo('wg', 280)
    if lang == 'ar':
        t1, t2, s1, s2 = 'كل ما يحتاجه بيتك ومناسباتك', 'تشكيلة واسعة للبيت والمناسبات', 84, 56
    else:
        t1, t2, s1, s2 = 'Everything your home needs', 'Home & occasion essentials in one place', 80, 50
    kw = dict(direction='rtl', language='ar') if lang == 'ar' else {}
    tw = max(d.textlength(t1, font=font(lang, 'b', s1), **kw), d.textlength(t2, font=font(lang, 'r', s2), **kw))
    gap = 90
    total = lg.width + gap + tw
    x0 = (W - total) / 2   # group centred between the pattern blocks (600..2400)
    if lang == 'ar':
        lx = int(x0 + tw + gap); img.alpha_composite(lg, (lx, (H - lg.height)//2))
        d.line((lx - gap//2, 200, lx - gap//2, 400), fill='white', width=5)
        text(d, (x0 + tw, 255), t1, 'ar', 'b', s1, 'white', anchor='rm')
        text(d, (x0 + tw, 360), t2, 'ar', 'r', s2, GOLD, anchor='rm')
    else:
        img.alpha_composite(lg, (int(x0), (H - lg.height)//2))
        tx = x0 + lg.width + gap
        d.line((tx - gap//2, 200, tx - gap//2, 400), fill='white', width=5)
        text(d, (tx, 255), t1, 'en', 'b', s1, 'white', anchor='lm')
        text(d, (tx, 360), t2, 'en', 'r', s2, GOLD, anchor='lm')
    return img

def hero(lang, W=3000, H=1500):
    img = Image.new('RGBA', (W, H), CREAM)
    d = ImageDraw.Draw(img)
    # colour field + pattern
    s = 250
    ar = lang == 'ar'
    fx0 = W - 1300 if ar else 0
    d.rectangle((fx0, 0, fx0 + 1300, H), fill=TEAL)
    cells = [('q', GOLD, None, None), ('hstripe', 'white', None, None), ('circle', ORANGE, None, None),
             ('dots', 'white', SAGE, None), ('half', GOLD, AMBER, None)]
    pattern_strip(img, fx0, H - s, s, cells if not ar else cells[::-1])
    cx = fx0 + 650
    lg = logo('wg', 230)
    img.alpha_composite(lg, (cx - lg.width//2, 170))
    if ar:
        fit_text(d, (cx, 560), 'احتياجات البيت والمناسبات', 'ar', 'b', 110, 'white', 1150)
        fit_text(d, (cx, 700), 'في مكان واحد', 'ar', 'b', 110, GOLD, 1150)
        fit_text(d, (cx, 860), 'حفلات · ضيافة · تغليف · مطبخ · تنظيم', 'ar', 'r', 60, 'white', 1150)
        btn = 'تسوّق الأكثر مبيعاً'
    else:
        fit_text(d, (cx, 560), 'Home & occasion', 'en', 'b', 120, 'white', 1150)
        fit_text(d, (cx, 700), 'essentials, all in one place', 'en', 'b', 96, GOLD, 1150)
        fit_text(d, (cx, 860), 'Party · Serving · Packaging · Kitchen · Home', 'en', 'r', 56, 'white', 1150)
        btn = 'Shop best sellers'
    bw, bh = 620, 130
    d.rounded_rectangle((cx-bw//2, 960, cx+bw//2, 960+bh), 65, fill=GOLD)
    text(d, (cx, 960+bh//2), btn, lang, 'b', 62, INK)
    # product collage
    gx0 = 60 if ar else 1300 + 60
    gw = W - 1300 - 120
    picks = [('B0FVF7MQLG', None, 'contain'), ('B0F8QM9JGJ', None, 'cover'), ('B0F8JL2NJ3', None, 'contain'),
             ('B0F7S411SR', None, 'cover'), ('B0F7LLS5LM', None, 'contain'), ('B0FHFXK464', None, 'contain')]
    cw = (gw - 2*40)//3; ch = (H - 120 - 40)//2
    for i, (a, cr, ft) in enumerate(picks):
        x = gx0 + (i % 3)*(cw + 40); y = 60 + (i//3)*(ch + 40)
        card(img, (x, y, x+cw, y+ch), a, r=50, crop=cr, fit=ft)
    return img

def story(key, lang, W=3000, H=1100):
    cfg = {
        'party': (ORANGE, 'جهّز حفلتك', 'Get your party ready', 'زينة، ضيافة، وتغليف هدايا', 'Decor, serving and gift wrapping',
                  [('B0F8QM9JGJ', None, 'cover'), ('B0CHF69K3C', (0, 0, 1, .78), 'cover'), ('B0F8JL2NJ3', None, 'contain'), ('B0HQ79SDY8', None, 'contain')]),
        'home': (EMERALD, 'بيت مرتب', 'An organised home', 'تنظيم، مطبخ، وتنظيف', 'Organising, kitchen and cleaning',
                 [('B0CGZVLNFT', None, 'contain'), ('B0FVF7MQLG', None, 'contain'), ('B0FHFXK464', None, 'contain'), ('B0GR1JZ7FL', None, 'contain')]),
    }[key]
    col, ar1, en1, ar2, en2, picks = cfg
    ar = lang == 'ar'
    img = Image.new('RGBA', (W, H), col)
    d = ImageDraw.Draw(img)
    s = 220
    pattern_strip(img, 0 if not ar else W - 3*s, 0, s,
                  [('circle', GOLD if col != GOLD else TEAL, None, None), ('vstripe', 'white', None, None), ('q', TEAL, None, None)])
    tx = W - 450 if ar else 450
    tc = 'white'
    fit_text(d, (tx, 470), ar1 if ar else en1, lang, 'b', 130, tc, 760)
    fit_text(d, (tx, 620), ar2 if ar else en2, lang, 'r', 62, tc, 760)
    bw, bh = 520, 120
    d.rounded_rectangle((tx-bw//2, 730, tx+bw//2, 730+bh), 60, fill='white')
    text(d, (tx, 730+bh//2), 'تسوّق الآن' if ar else 'Shop now', lang, 'b', 58, col if not light(col) else INK)
    gx0 = 80 if ar else 900
    gw = W - 900 - 80
    cw = (gw - 3*40)//4
    for i, (a, cr, ft) in enumerate(picks):
        x = gx0 + i*(cw + 40)
        card(img, (x, 200, x+cw, H-200), a, r=50, crop=cr, fit=ft)
    return img

def icon(d, k, cx, cy):
    w = 'white'
    if k == 0:   # grid of 4 rounded squares = range
        for dx in (-36, 36):
            for dy in (-36, 36):
                d.rounded_rectangle((cx+dx-28, cy+dy-28, cx+dx+28, cy+dy+28), 10, fill=w)
    elif k == 1:  # stacked boxes = pack sizes
        d.rounded_rectangle((cx-70, cy+5, cx-5, cy+70), 8, fill=w)
        d.rounded_rectangle((cx+5, cy+5, cx+70, cy+70), 8, fill=w)
        d.rounded_rectangle((cx-33, cy-62, cx+33, cy-2), 8, fill=w)
    else:         # delivery truck
        d.rounded_rectangle((cx-80, cy-45, cx+20, cy+30), 8, fill=w)
        d.polygon([(cx+25, cy-25), (cx+60, cy-25), (cx+82, cy+5), (cx+82, cy+30), (cx+25, cy+30)], fill=w)
        for wx in (cx-50, cx+50):
            d.ellipse((wx-20, cy+25, wx+20, cy+65), fill=w)

def why(lang, W=3000, H=700):
    img = Image.new('RGBA', (W, H), CREAM)
    d = ImageDraw.Draw(img)
    items = [
        (TEAL, 'تشكيلة واسعة', 'Wide range', 'للبيت والمناسبات', 'For home and occasions'),
        (ORANGE, 'كميات تناسبك', 'Pack sizes for you', 'للعائلة والضيافة', 'For families and gatherings'),
        (GOLD, 'توصيل سريع', 'Fast delivery', 'عبر أمازون', 'Delivered via Amazon'),
    ]
    if lang == 'ar':
        items = items[::-1]
    colw = W // 3
    for i, (col, a1, e1, a2, e2) in enumerate(items):
        cx = colw*i + colw//2
        r = 120
        d.ellipse((cx - r, 120, cx + r, 120 + 2*r), fill=col)
        icon(d, i if lang == 'en' else 2 - i, cx, 240)
        text(d, (cx, 470), a1 if lang == 'ar' else e1, lang, 'b', 80, INK)
        text(d, (cx, 570), a2 if lang == 'ar' else e2, lang, 'r', 54, TEAL)
    return img

def page_header(c, lang, W=3000, H=600):
    key, ar, en, col, asin, crop, fit = c
    img = Image.new('RGBA', (W, H), col)
    d = ImageDraw.Draw(img)
    s = 300
    others = [p for p in PAL if p != col]
    isar = lang == 'ar'
    pattern_strip(img, 0 if not isar else W - 2*s, 0, s, [('q', others[0], None, None), ('hstripe', 'white', None, None)])
    pattern_strip(img, 0 if not isar else W - 2*s, s, s, [('circle', others[2], None, None), ('dots', 'white', others[3], None)])
    card(img, ((W - 1000) if not isar else 100, 60, (W - 100) if not isar else 1000, H - 60), asin, r=50, crop=crop, fit=fit)
    tc = INK if light(col) else 'white'
    tx = 760 if not isar else W - 760
    text(d, (tx, H//2), ar if isar else en, lang, 'b', 120, tc, anchor='lm' if not isar else 'rm')
    return img

def ramadan(lang, W=3000, H=600):
    img = Image.new('RGBA', (W, H), TEAL_D)
    d = ImageDraw.Draw(img)
    # crescent + stars in gold (generic, no emblems)
    cx, cy, r = (W - 420, 300, 200) if lang == 'ar' else (420, 300, 200)
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GOLD)
    d.ellipse((cx - r + 90, cy - r - 30, cx + r + 90, cy + r - 30), fill=TEAL_D)
    for (sx, sy, sr) in [(cx + 230, 150, 18), (cx + 300, 250, 12), (cx + 190, 420, 14)] if lang == 'en' else [(cx - 230, 150, 18), (cx - 300, 250, 12), (cx - 190, 420, 14)]:
        d.ellipse((sx - sr, sy - sr, sx + sr, sy + sr), fill='white')
    s = 300
    pattern_strip(img, W - 2*s if lang == 'en' else 0, 0, s, [('hstripe', GOLD, None, None), ('q', ORANGE, None, None)])
    pattern_strip(img, W - 2*s if lang == 'en' else 0, s, s, [('circle', SAGE, None, None), ('vstripe', 'white', None, None)])
    if lang == 'ar':
        text(d, (W//2 + 300, 250), 'رمضان والعيد', 'ar', 'b', 140, 'white', anchor='rm')
        text(d, (W//2 + 300, 390), 'كل ما تحتاجه للضيافة والزينة والتوزيعات', 'ar', 'r', 64, GOLD, anchor='rm')
    else:
        text(d, (W//2 - 300, 250), 'Ramadan & Eid', 'en', 'b', 140, 'white', anchor='lm')
        text(d, (W//2 - 300, 390), 'Serving, decor and giveaways for the season', 'en', 'r', 60, GOLD, anchor='lm')
    return img

def save(img, name):
    p = os.path.join(OUT, name)
    img.convert('RGB').save(p, quality=92)
    return p

if __name__ == '__main__':
    which = sys.argv[1:] or ['all']
    for lang in ('ar', 'en'):
        if 'all' in which or 'header' in which: save(header(lang), f'{lang}_01_header_3000x600.jpg')
        if 'all' in which or 'hero' in which: save(hero(lang), f'{lang}_02_hero_3000x1500.jpg')
        if 'all' in which or 'tiles' in which:
            for i, c in enumerate(CATS):
                save(cat_tile(c, lang), f'{lang}_03_tile_{i+1:02d}_{c[0]}_1500.jpg')
        if 'all' in which or 'story' in which:
            save(story('party', lang), f'{lang}_04_story_party_3000x1100.jpg')
            save(story('home', lang), f'{lang}_05_story_home_3000x1100.jpg')
        if 'all' in which or 'why' in which: save(why(lang), f'{lang}_06_why_3000x700.jpg')
        if 'all' in which or 'pages' in which:
            for i, c in enumerate(CATS):
                save(page_header(c, lang), f'{lang}_07_page_{i+1:02d}_{c[0]}_3000x600.jpg')
        if 'all' in which or 'ramadan' in which: save(ramadan(lang), f'{lang}_08_ramadan_3000x600.jpg')
    print('done', len(os.listdir(OUT)))
