#!/usr/bin/env python3
"""HABBAA brand store v3 — 'هبّة / Catch the gust'.
Real AI-integrated product scenes (Nano Banana 2.1 w/ product refs), giant type behind
levitating products, spotlight studio, editorial splits, mobile crops."""
import os, sys, random
from PIL import Image, ImageDraw, ImageFilter, ImageOps
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen2 import font, kw, tw, cover, logo, cta, B

RAW = os.path.join(B, 'v3', 'raw'); CUT = os.path.join(B, 'v3', 'cut')
OUT = os.path.join(B, 'out3'); os.makedirs(OUT, exist_ok=True)
INK = '#10201F'; TEAL = '#008080'; TEAL_D = '#0B3F3F'; GOLD = '#DBC500'; CREAM = '#F6F1E7'

C = {  # key: (ar, en)
 'tag': ('كل يوم له هبّة', 'Every day has its gust'),
 'h_eye': ('هبّة الحفلات', 'THE PARTY GUST'), 'h_t': ('خلّها تهب', 'Let it burst.'),
 'h_s': ('قصاصات، أشرطة، أكياس هدايا وكل ما تحتاجه الفرحة', 'Confetti, ribbons, gift bags and everything a celebration needs'),
 'h_c': ('تسوّق الحفلات', 'Shop party'), 'h_word': ('هبّة', 'HABBAA'),
 'k_party': ('الحفلات', 'Party'), 'k_host': ('الضيافة', 'Hosting'), 'k_office': ('المكتب والمدرسة', 'Office & School'),
 'k_home': ('البيت والتنظيم', 'Home & Storage'), 'disc': ('اكتشف', 'Explore'),
 'th_eye': ('هبّة الضيافة', 'THE HOSTING GUST'), 'th_t': ('القهوة على حرارتها', 'Coffee, kept warm.'),
 'th_c': ('تسوّق الترامس', 'Shop flasks'), 'th_word': ('قهوة', 'COFFEE'),
 'mj_t': ('مجلسك جاهز', 'Your majlis, ready'), 'mj_c': ('تسوّق الضيافة', 'Shop hosting'),
 'cup_t': ('قهوة، شاي، عصير', 'Coffee. Tea. Juice.'), 'cup_s': ('أكواب ورقية بيضاء لكل ضيافة', 'White paper cups for every gathering'),
 'cup_c': ('تسوّق الأكواب', 'Shop cups'),
 'sh_t': ('ضيافة على أصولها', 'Hosting, done right.'), 'sh_s': ('اضغط على المنتج للتسوق', 'Tap a product to shop'),
 'sc_eye': ('هبّة المكتب والمدرسة', 'THE DESK GUST'), 'sc_t': ('تحت الضوء', 'In the spotlight.'),
 'sc_s': ('ورق A4، مقصات، أقلام رصاص وأصابع غراء', 'A4 paper, scissors, pencils and glue sticks'), 'sc_c': ('تسوّق المكتب', 'Shop office'),
 'a4_t': ('ورق A4 لكل شغلك', 'A4 for every task'), 'a4_c': ('تسوّق الورق', 'Shop paper'),
 'cd_word': ('سهرة', 'GAME ON'), 'cd_t': ('ورق لعب لسهرة الشلة', 'Cards for game night'), 'cd_c': ('تسوّق الألعاب', 'Shop games'),
 'tr_eye': ('هبّة المشاوير', 'THE ERRAND GUST'), 'tr_t': ('مشوار السوق صار أخف', 'Errands, lighter.'),
 'tr_s': ('عربة تسوق قابلة للطي بعجلات للدرج', 'Foldable shopping trolley with stair-climbing wheels'), 'tr_c': ('تسوّق العربات', 'Shop trolleys'),
 'ct_word': ('طازج', 'FRESH'), 'ct_t': ('خلّ أكلك طازج', 'Keep it fresh.'), 'ct_c': ('تسوّق الحافظات', 'Shop containers'),
 'bk_t': ('ركن مرتّب', 'A tidy corner'), 'bk_c': ('تسوّق السلال', 'Shop baskets'),
 'gf_t': ('غلّفها بحب', 'Wrap it with love'), 'gf_c': ('تسوّق التغليف', 'Shop gift wrap'),
 'gal': ('هبّة في كل بيت', 'A gust in every home'),
 'kt_eye': ('قصة اسمنا', 'OUR NAME'), 'kt_t': ('الهبّة.. نسمة تغيّر الجو', 'Habbaa: the gust that lifts the mood.'),
 'kt_s': ('من الحفلة للمكتب للمشوار، نجمع لك أغراض يومك في مكان واحد', 'From party to desk to errands, everyday essentials in one place'),
 'kt_c': ('كل المنتجات', 'All products'),
 'um_word': ('مطر', 'RAIN'), 'um_t': ('شفافة وخفيفة', 'Clear & light'),
 'bb_t': ('العب برّا', 'Play outside'), 'fn_t': ('توزيعات الأعراس', 'Wedding favours'), 'bs_t': ('سلال الغسيل', 'Laundry baskets'),
 'rm_eye': ('قريباً', 'COMING UP'), 'rm_t': ('رمضان على الأبواب', 'Ramadan is near.'),
 'rm_s': ('جهّز مجلسك وضيافتك من الحين', 'Get your majlis and hosting ready'), 'rm_c': ('رمضان والعيد', 'Ramadan & Eid'),
 'why': [('توصيل Prime', 'Prime delivery'), ('شحن من أمازون', 'Fulfilled by Amazon'),
         ('منتجات ليومك كله', 'Essentials for every day'), ('إرجاع حسب سياسة أمازون', 'Amazon returns policy')],
}
def c(k, L): return C[k][0] if L == 'ar' else C[k][1]

# ---------- helpers ----------
def raw(n): return Image.open(os.path.join(RAW, n + '.png')).convert('RGB')
def cut(n): return Image.open(os.path.join(CUT, n + '.png')).convert('RGBA')

def fit(im, size, focus=(0.5, 0.5)): return ImageOps.fit(im, size, Image.LANCZOS, centering=focus)

def grain(im, amt=7, seed=3):
    import numpy as np
    a = np.asarray(im.convert('RGB')).astype(np.int16)
    rng = np.random.default_rng(seed); n = rng.normal(0, amt, a.shape[:2])[..., None]
    return Image.fromarray(np.clip(a + n, 0, 255).astype('uint8'))

def shade(im, side='left', frac=0.6, strength=0.7, color=(0, 0, 0)):
    w, h = im.size; g = Image.new('L', (w, 1))
    for x in range(w):
        t = (w * frac - x) / (w * frac) if side == 'left' else (x - w * (1 - frac)) / (w * frac)
        if side == 'top': t = 0
        g.putpixel((x, 0), int(255 * strength * max(0, min(1, t)) ** 1.5))
    g = g.resize((w, h))
    if side in ('top', 'bottom'):
        g = Image.new('L', (1, h))
        for y in range(h):
            t = (h * frac - y) / (h * frac) if side == 'top' else (y - h * (1 - frac)) / (h * frac)
            g.putpixel((0, y), int(255 * strength * max(0, min(1, t)) ** 1.5))
        g = g.resize((w, h))
    ov = Image.new('RGBA', (w, h), color + (0,)); ov.putalpha(g)
    o = im.convert('RGBA'); o.alpha_composite(ov); return o

def giant(base, word, L, cy, size, fill=(255, 255, 255), alpha=235, blur=2, cx=None, track=0):
    w, h = base.size; cx = w / 2 if cx is None else cx
    lay = Image.new('RGBA', base.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    f = font(L, 'b', size)
    # shrink to 94% width
    while d.textlength(word, font=f, **kw(L)) > w * 0.94: size -= 10; f = font(L, 'b', size)
    d.text((cx, cy), word, font=f, fill=fill + (alpha,), anchor='mm', **kw(L))
    if blur: lay = lay.filter(ImageFilter.GaussianBlur(blur))
    base.alpha_composite(lay)

def extend_left(im, size, shift=0.0, push=0):
    """Scale to height, right-align, and fill the left with the stretched, blurred edge (seamless studio extension)."""
    W, H = size; im = im.convert('RGB'); w = int(im.width * H / im.height); im = im.resize((w, H), Image.LANCZOS)
    extra = int(W * shift)
    if w >= W + extra: return im.crop((w - W - extra, 0, w - extra, H)) if extra else ImageOps.fit(im, size, Image.LANCZOS, centering=(0.5, 0.5))
    if push: im = im.crop((0, 0, w - push, H)); w -= push
    out = Image.new('RGB', (W, H)); left = W - w
    edge = im.crop((0, 0, 8, H)).resize((left + 200, H), Image.BILINEAR).filter(ImageFilter.GaussianBlur(40))
    out.paste(edge, (0, 0)); m = Image.new('L', (w, 1), 255)
    for x in range(200): m.putpixel((x, 0), int(255 * x / 200))
    out.paste(im, (left, 0), m.resize((w, H))); return out

def extend_left_rgba(im, size):
    W, H = size; w = int(im.width * H / im.height); im = im.resize((w, H), Image.LANCZOS)
    out = Image.new('RGBA', (W, H), (0, 0, 0, 0)); out.paste(im, (W - w, 0)) if w <= W else out.paste(ImageOps.fit(im, size), (0, 0)); return out

def mobile_canvas(bgname, focusx, cutname=None, S=1500, ih=1020):
    """Image at the bottom (height ih), top extended from its own top edge for text."""
    src = raw(bgname); w = int(src.width * ih / src.height); im = src.resize((w, ih), Image.LANCZOS)
    x0 = int(max(0, min(w - S, focusx * w - S / 2))); im = im.crop((x0, 0, x0 + S, ih))
    out = Image.new('RGB', (S, S)); top = S - ih
    edge = im.crop((0, 0, S, 60)).resize((60, 4), Image.BILINEAR).resize((S, top + 160), Image.BICUBIC).filter(ImageFilter.GaussianBlur(60))
    out.paste(edge, (0, 0)); m = Image.new('L', (1, ih), 255)
    for y in range(160): m.putpixel((0, y), int(255 * y / 160))
    out.paste(im, (0, top), m.resize((S, ih))); out = out.convert('RGBA')
    if cutname:
        cimg = cut(cutname).resize((w, ih), Image.LANCZOS).crop((x0, 0, x0 + S, ih)); out.alpha_composite(cimg, (0, top))
    return out

def layered(bgname, cutname, size, focus, word, L, cy_frac=0.5, wsize=None, fill=(255, 255, 255), alpha=235, ext=False, wcx=None):
    if ext:
        bg = extend_left(raw(bgname), size).convert('RGBA'); ct = extend_left_rgba(cut(cutname), size)
    else:
        bg = fit(raw(bgname), size, focus).convert('RGBA'); ct = fit(cut(cutname), size, focus)
    if alpha: giant(bg, word, L, size[1] * cy_frac, wsize or int(size[1] * 0.42), fill, alpha, cx=wcx)
    bg.alpha_composite(ct); return bg

def block(img, L, x, y, eye=None, title=None, sub=None, button=None, tsize=150, fg='white', eye_col=None,
          btn_bg='white', btn_fg=INK, maxw=None, align=None):
    """Editorial text block. x = start edge (left for en, right for ar unless align given)."""
    d = ImageDraw.Draw(img); ar = L == 'ar'; anc = align or ('r' if ar else 'l')
    maxw = maxw or img.width * 0.42; yy = y
    if eye:
        es = max(36, int(tsize * 0.30))
        f = font(L, 'b', es)
        lw = int(tsize * 0.55)
        if anc == 'r':
            d.line((x - lw, yy + es * 0.55, x, yy + es * 0.55), fill=eye_col or fg, width=max(3, es // 8))
            d.text((x - lw - es * 0.6, yy), eye, font=f, fill=eye_col or fg, anchor='ra', **kw(L))
        else:
            d.line((x, yy + es * 0.55, x + lw, yy + es * 0.55), fill=eye_col or fg, width=max(3, es // 8))
            d.text((x + lw + es * 0.6, yy), eye, font=f, fill=eye_col or fg, anchor='la', **kw(L))
        yy += es * 2.2
    if title:
        s = tsize
        while tw(d, title, L, 'b', s) > maxw and s > 40: s -= 4
        # wrap in two lines if still long
        d.text((x, yy), title, font=font(L, 'b', s), fill=fg, anchor=anc + 'a', **kw(L))
        bb = d.textbbox((x, yy), title, font=font(L, 'b', s), anchor=anc + 'a', **kw(L)); yy = bb[3] + s * 0.35
    if sub:
        ss = int(tsize * 0.30)
        words = sub.split(); lines = []; cur = ''
        for wd in words:
            t = (cur + ' ' + wd).strip()
            if tw(d, t, L, 'r', ss) > maxw and cur: lines.append(cur); cur = wd
            else: cur = t
        lines.append(cur)
        for ln in lines:
            d.text((x, yy), ln, font=font(L, 'r', ss), fill=fg, anchor=anc + 'a', **kw(L)); yy += ss * 1.45
        yy += ss * 0.5
    if button:
        bs = int(tsize * 0.27)
        bb = cta(d, x, int(yy), button, L, size=bs, fg=btn_fg, bg=btn_bg, anchor_right=(anc == 'r'))
        yy = bb[3]
    return yy

def sx(img, L, pad):  # start x for text on the LEFT region in both languages
    return pad if L == 'en' else None

def save(img, name, q=90):
    p = os.path.join(OUT, name); img.convert('RGB').save(p, quality=q, optimize=True)
    if os.path.getsize(p) > 4_800_000: img.convert('RGB').save(p, quality=82, optimize=True)

def left_block(img, L, pad, y, width_frac=0.40, **k):
    """Text sits in the left zone of the image for both languages; Arabic right-aligned inside that zone."""
    zone = img.width * width_frac
    x = pad if L == 'en' else pad + zone
    return block(img, L, x, y, maxw=zone, **k)

# ---------- tiles ----------
def header(L, W=3000, H=600):
    im = fit(raw('header_b'), (W, H), (0.5, 0.55)).convert('RGBA')
    im = shade(im, 'bottom', 0.5, 0.25)
    # frosted pill in calm centre
    cx = W * 0.46; pw, ph = 900, 380
    box = (int(cx - pw / 2), int(H / 2 - ph / 2), int(cx + pw / 2), int(H / 2 + ph / 2))
    reg = im.crop(box).filter(ImageFilter.GaussianBlur(26))
    m = Image.new('L', reg.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, pw - 1, ph - 1), 60, fill=255)
    tint = Image.new('RGBA', reg.size, (6, 70, 72, 150)); reg.alpha_composite(tint)
    im.paste(reg, box[:2], m)
    ImageDraw.Draw(im).rounded_rectangle(box, 60, outline=(255, 255, 255, 120), width=3)
    lg = logo('white', 230); im.alpha_composite(lg, (int(cx - lg.width / 2), int(H / 2 - 150)))
    d = ImageDraw.Draw(im)
    d.text((cx, H / 2 + 125), c('tag', L), font=font(L, 'm', 46), fill='white', anchor='mm', **kw(L))
    return im

def hero(L, W=3000, H=1500, mobile=False):
    if mobile:
        im = mobile_canvas('party_b', 0.68)
        x = 1400 if L == 'ar' else 100
        block(im, L, x, 90, c('h_eye', L), c('h_t', L), c('h_s', L), c('h_c', L), tsize=130, maxw=1300, eye_col=GOLD)
        return im
    im = layered('party_b', 'party', (W, H), (0.5, 0.5), c('h_word', L), L, 0.5, 820 if L == 'ar' else 400, alpha=70, ext=True, wcx=W * 0.66)
    im = shade(im, 'left', 0.55, 0.55, (4, 40, 42))
    left_block(im, L, 190, 400, 0.30, eye=c('h_eye', L), title=c('h_t', L), sub=c('h_s', L), button=c('h_c', L),
               tsize=230, eye_col=GOLD)
    return im

def cat_tile(L, key, scene_, focus, S=750):
    im = fit(raw(scene_), (S, S), focus).convert('RGBA')
    im = shade(im, 'bottom', 0.55, 0.78, (8, 20, 20))
    d = ImageDraw.Draw(im); ar = L == 'ar'; x = S - 56 if ar else 56
    s = 78
    while tw(d, c(key, L), L, 'b', s) > S - 112: s -= 4
    d.text((x, S - 150), c(key, L), font=font(L, 'b', s), fill='white', anchor=('rs' if ar else 'ls'), **kw(L))
    # small discover link with chevron
    fs = 34; t = c('disc', L); tx = x
    d.text((tx, S - 80), t, font=font(L, 'm', fs), fill=GOLD, anchor=('rs' if ar else 'ls'), **kw(L))
    tlen = tw(d, t, L, 'm', fs); ax = tx - tlen - 30 if ar else tx + tlen + 30; cy = S - 92; a = 10
    pts = [(ax + a, cy - a), (ax, cy), (ax + a, cy + a)] if ar else [(ax - a, cy - a), (ax, cy), (ax - a, cy + a)]
    d.line(pts, fill=GOLD, width=5, joint='curve')
    return im

def word_tile(L, bg, ct, word, eye, title, button, focus=(0.5, 0.5), S=(1500, 1500), cy=0.5, wsize=None,
              alpha=235, text_top=True, fg='white', btn_bg='white', btn_fg=INK, fill=(255, 255, 255)):
    im = layered(bg, ct, S, focus, word, L, cy, wsize, fill=fill, alpha=alpha)
    W, H = S; ar = L == 'ar'
    if text_top:
        im = shade(im, 'top', 0.3, 0.35, (0, 0, 0))
        x = W - 90 if ar else 90
        block(im, L, x, 80, eye, title, None, None, tsize=96, fg=fg, maxw=W - 180)
    d = ImageDraw.Draw(im)
    bs = 40
    if button:
        x = W - 90 if ar else 90
        cta(d, x, H - 170, button, L, size=bs, fg=btn_fg, bg=btn_bg, anchor_right=ar)
    return im

def photo_medium(L, scene_, focus, title, button, W=1500, H=750, side='bottom'):
    im = fit(raw(scene_), (W, H), focus).convert('RGBA')
    im = shade(im, 'bottom', 0.6, 0.75, (10, 16, 16)); ar = L == 'ar'
    x = W - 80 if ar else 80
    d = ImageDraw.Draw(im)
    d.text((x, H - 170), title, font=font(L, 'b', 80), fill='white', anchor=('rs' if ar else 'ls'), **kw(L))
    cta(d, x, H - 140, button, L, size=34, fg=INK, bg='white', anchor_right=ar)
    return im

def info_card(L, W=1500, H=750):
    im = Image.new('RGBA', (W, H), CREAM); d = ImageDraw.Draw(im)
    # soft radial glow + thin gold arc (brand gesture)
    glow = Image.new('L', (W, H), 0); ImageDraw.Draw(glow).ellipse((W * 0.55, -H * 0.4, W * 1.35, H * 1.1), fill=255)
    glow = glow.filter(ImageFilter.GaussianBlur(120))
    im.paste(Image.new('RGBA', (W, H), (232, 214, 182, 255)), (0, 0), glow.point(lambda v: v // 2))
    d.arc((W * 0.62, H * 0.12, W * 1.25, H * 1.4), 180, 300, fill=GOLD, width=10)
    d.arc((W * 0.7, H * 0.3, W * 1.25, H * 1.6), 180, 290, fill=TEAL, width=10)
    im = grain(im, 6).convert('RGBA')
    ar = L == 'ar'; x = W - 110 if ar else 110
    block(im, L, x if not ar else W * 0.62, 150, None, c('cup_t', L), c('cup_s', L), c('cup_c', L), tsize=110, fg=INK,
          btn_bg=TEAL, btn_fg='white', maxw=W * 0.52)
    return im

def full_photo(L, scene_, focus, eye, title, sub, button, W=3000, H=1500, shade_col=(0, 0, 0), strength=0.6,
               tsize=190, y=None, eye_col=GOLD, frac=0.6, zone=0.38, mobile=False, mfocus=None, ext=False, push=0):
    if mobile:
        im = mobile_canvas(scene_, (mfocus or focus)[0])
        im = shade(im, 'top', 0.4, 0.45, shade_col)
        x = 1400 if L == 'ar' else 100
        block(im, L, x, 90, eye, title, sub, button, tsize=120, maxw=1300, eye_col=eye_col)
        return im
    im = (extend_left(raw(scene_), (W, H), push=push) if ext else fit(raw(scene_), (W, H), focus)).convert('RGBA')
    im = shade(im, 'left', frac, strength, shade_col)
    left_block(im, L, 170, y or int(H * 0.27), zone, eye=eye, title=title, sub=sub, button=button, tsize=tsize, eye_col=eye_col)
    return im

def kite_story(L, W=3000, H=1500, mobile=False):
    if mobile:
        im = mobile_canvas('kite_a', 0.72)
        x = 1400 if L == 'ar' else 100
        block(im, L, x, 90, c('kt_eye', L), c('kt_t', L), c('kt_s', L), c('kt_c', L), tsize=110, maxw=1300)
        return im
    im = layered('kite_a', 'kite', (W, H), (0.5, 0.5), c('h_word', L), L, 0.36, 1000, fill=(255, 236, 214), alpha=0, wcx=W * 0.66)
    im = shade(im, 'left', 0.55, 0.45, (90, 40, 10))
    left_block(im, L, 170, 400, 0.36, eye=c('kt_eye', L), title=c('kt_t', L), sub=c('kt_s', L), button=c('kt_c', L), tsize=150)
    return im

def small_label(L, scene_, focus, title, S=750, layeredspec=None):
    if layeredspec:
        im = layered(scene_, layeredspec[0], (S, S), focus, layeredspec[1], L, layeredspec[2], layeredspec[3], alpha=layeredspec[4])
    else:
        im = fit(raw(scene_), (S, S), focus).convert('RGBA')
    im = shade(im, 'bottom', 0.4, 0.7, (5, 15, 15)); d = ImageDraw.Draw(im); ar = L == 'ar'
    x = S - 50 if ar else 50
    d.text((x, S - 60), title, font=font(L, 'b', 62), fill='white', anchor=('rs' if ar else 'ls'), **kw(L))
    return im

def gallery(L):
    picks = [('majlis_b', (0.6, 0.6)), ('ram_b', (0.6, 0.55)), ('gift_b', (0.7, 0.5)), ('trolley_b', (0.7, 0.5)),
             ('fan_a', (0.5, 0.45)), ('ball_a', (0.5, 0.55)), ('basket_b', (0.55, 0.6)), ('school_a', (0.6, 0.6))]
    return [fit(raw(n), (1500, 750), f) for n, f in picks]

def icon(d, i, cx, cy, col=GOLD, w=7):
    if i == 0:   # fast delivery: truck with speed lines
        d.rounded_rectangle((cx - 40, cy - 34, cx + 18, cy + 18), 6, outline=col, width=w)
        d.polygon([(cx + 18, cy - 18), (cx + 42, cy - 18), (cx + 58, cy), (cx + 58, cy + 18), (cx + 18, cy + 18)], outline=col, width=w)
        for x in (cx - 22, cx + 36): d.ellipse((x - 12, cy + 12, x + 12, cy + 36), fill=TEAL_D, outline=col, width=w)
        for k in range(3): d.line((cx - 92, cy - 22 + k * 18, cx - 56, cy - 22 + k * 18), fill=col, width=w - 2)
    elif i == 1:  # box
        d.polygon([(cx, cy - 48), (cx + 48, cy - 24), (cx, cy), (cx - 48, cy - 24)], outline=col, width=w)
        d.line((cx - 48, cy - 24, cx - 48, cy + 28), fill=col, width=w); d.line((cx + 48, cy - 24, cx + 48, cy + 28), fill=col, width=w)
        d.line((cx, cy, cx, cy + 52), fill=col, width=w); d.line((cx - 48, cy + 28, cx, cy + 52), fill=col, width=w); d.line((cx + 48, cy + 28, cx, cy + 52), fill=col, width=w)
    elif i == 2:  # gust swirl (brand)
        d.arc((cx - 50, cy - 44, cx + 50, cy + 30), 190, 360, fill=col, width=w)
        d.arc((cx - 10, cy - 14, cx + 30, cy + 20), 270, 520, fill=col, width=w)
        d.line((cx - 60, cy + 30, cx + 30, cy + 30), fill=col, width=w); d.line((cx - 40, cy + 50, cx + 50, cy + 50), fill=col, width=w)
    else:  # return arrow
        d.arc((cx - 46, cy - 40, cx + 46, cy + 48), 300, 220, fill=col, width=w)
        d.polygon([(cx - 56, cy - 2), (cx - 22, cy - 8), (cx - 44, cy + 22)], fill=col)

def why(L, W=3000, H=560):
    im = Image.new('RGBA', (W, H), TEAL_D); d = ImageDraw.Draw(im)
    # gust lines
    for i in range(7):
        y = 60 + i * 70
        d.arc((-400 + i * 90, y - 900, W + 300 - i * 60, y + 300), 200, 330, fill=(255, 255, 255, 14), width=4)
    im = grain(im, 5).convert('RGBA'); d = ImageDraw.Draw(im)
    items = C['why']; n = len(items); cw = W / n; ar = L == 'ar'
    order = list(range(n))[::-1] if ar else list(range(n))
    for slot, i in enumerate(order):
        cx = cw * slot + cw / 2
        icon(d, i, cx, 198)
        t = items[i][0] if ar else items[i][1]
        s = 52
        while tw(d, t, L, 'b', s) > cw - 80: s -= 2
        d.text((cx, 330), t, font=font(L, 'b', s), fill='white', anchor='mm', **kw(L))
        if slot: d.line((cw * slot, 170, cw * slot, 380), fill=(255, 255, 255, 50), width=2)
    return im

R = {
 'r1_eye': ('رمضان والعيد', 'RAMADAN & EID'), 'r1_t': ('ليالي تجمعنا', 'Nights that bring us together'),
 'r1_s': ('ضيافة رمضان وتوزيعات العيد في مكان واحد', 'Ramadan hosting and Eid favours in one place'), 'r1_c': ('تسوّق الضيافة', 'Shop hosting'),
 'r2_t': ('قهوة الفطور', 'Iftar coffee'), 'r2_c': ('تسوّق الترامس', 'Shop flasks'),
 'r3_t': ('سفرة جاهزة', 'Table, ready'), 'r3_c': ('تسوّق الصواني', 'Shop trays'),
 'r4_t': ('أكواب للضيوف', 'Cups for guests'), 'r4_c': ('تسوّق الأكواب', 'Shop cups'),
 'e1_eye': ('العيد', 'EID'), 'e1_t': ('عيدكم هبّة فرح', 'Eid, in full bloom.'),
 'e1_s': ('قصاصات، أشرطة وأكياس عيدية', 'Confetti, ribbons and Eidiya gift bags'), 'e1_c': ('تسوّق العيد', 'Shop Eid'),
 'e2_t': ('أكياس العيدية', 'Eidiya bags'), 'e2_c': ('تسوّق الأكياس', 'Shop bags'),
 'e3_t': ('توزيعات أنيقة', 'Elegant favours'), 'e3_c': ('تسوّق المراوح', 'Shop fans'),
}
def r(k, L): return R[k][0] if L == 'ar' else R[k][1]

def build_ramadan(L):
    P = f'{L}_RE_'
    im = Image.new('RGB', (3000, 600)); bg = fit(raw('ram_b'), (3000, 600), (0.6, 0.45)).convert('RGBA')
    bg = shade(bg, 'left', 0.7, 0.75, (6, 10, 30)); d = ImageDraw.Draw(bg)
    x = 1100 if L == 'ar' else 170
    d.text((x, 300), r('r1_eye', L), font=font(L, 'b', 140), fill='white', anchor=('rm' if L == 'ar' else 'lm'), **kw(L))
    save(bg, P + '00_header_3000x600.jpg')
    save(full_photo(L, 'ram_b', (0.5, 0.5), r('r1_eye', L), r('r1_t', L), r('r1_s', L), r('r1_c', L), shade_col=(6, 10, 30),
                    strength=0.6, y=420), P + '01_hero_3000x1500.jpg')
    save(full_photo(L, 'ram_b', (0.5, 0.5), r('r1_eye', L), r('r1_t', L), r('r1_s', L), r('r1_c', L), mobile=True,
                    mfocus=(0.72, 0.5), shade_col=(6, 10, 30)), P + '01m_hero_mobile_1500.jpg')
    save(word_tile(L, 'thermos_a', 'thermos', c('th_word', L), None, r('r2_t', L), r('r2_c', L), cy=0.52, wsize=560, alpha=230),
         P + '02a_thermos_large_1500.jpg')
    save(photo_medium(L, 'ram_a', (0.72, 0.6), r('r3_t', L), r('r3_c', L)), P + '02b_tray_medium_1500x750.jpg')
    save(photo_medium(L, 'majlis_a', (0.68, 0.62), r('r4_t', L), r('r4_c', L)), P + '02c_cups_medium_1500x750.jpg')
    save(full_photo(L, 'party_a', (0.5, 0.5), r('e1_eye', L), r('e1_t', L), r('e1_s', L), r('e1_c', L), shade_col=(4, 40, 42),
                    strength=0.55, y=420, ext=True, push=200, zone=0.32), P + '03_eid_3000x1500.jpg')
    save(photo_medium(L, 'gift_b', (0.8, 0.5), r('e2_t', L), r('e2_c', L)), P + '04a_bags_medium_1500x750.jpg')
    save(photo_medium(L, 'fan_b', (0.5, 0.4), r('e3_t', L), r('e3_c', L)), P + '04b_fans_medium_1500x750.jpg')

def build(L):
    P = f'{L}_'
    save(header(L), P + '00_header_3000x600.jpg')
    save(hero(L), P + '01_hero_fullwidth_3000x1500.jpg')
    save(hero(L, mobile=True), P + '01m_hero_mobile_1500.jpg')
    for i, (k, s, f) in enumerate([('k_party', 'party_a', (0.6, 0.5)), ('k_host', 'majlis_a', (0.68, 0.6)),
                                   ('k_office', 'school_a', (0.7, 0.85)), ('k_home', 'cont_b', (0.5, 0.5))]):
        save(cat_tile(L, k, s, f), P + f'02{"abcd"[i]}_cat_small_750.jpg')
    save(word_tile(L, 'thermos_a', 'thermos', c('th_word', L), c('th_eye', L), c('th_t', L), c('th_c', L),
                   cy=0.52, wsize=560, alpha=230), P + '03a_thermos_large_1500.jpg')
    save(photo_medium(L, 'majlis_b', (0.75, 0.6), c('mj_t', L), c('mj_c', L)), P + '03b_majlis_medium_1500x750.jpg')
    save(info_card(L), P + '03c_cups_card_medium_1500x750.jpg')
    save(full_photo(L, 'majlis_a', (0.5, 0.5), None, c('sh_t', L), c('sh_s', L), None, shade_col=(30, 18, 6), strength=0.62,
                    y=560), P + '04_majlis_shoppable_3000x1500.jpg')
    save(full_photo(L, 'school_b', (0.5, 0.5), c('sc_eye', L), c('sc_t', L), c('sc_s', L), c('sc_c', L), W=3000, H=1300,
                    strength=0.35, y=330, ext=True, zone=0.30, push=330), P + '05_spotlight_office_3000x1300.jpg')
    save(full_photo(L, 'school_b', (0.5, 0.5), c('sc_eye', L), c('sc_t', L), c('sc_s', L), c('sc_c', L), mobile=True,
                    mfocus=(0.62, 0.5)), P + '05m_spotlight_mobile_1500.jpg')
    save(word_tile(L, 'a4_b', 'a4', 'A4', None, c('a4_t', L), c('a4_c', L), cy=0.5, wsize=900, alpha=235),
         P + '06a_a4_large_1500.jpg')
    save(word_tile(L, 'cards_b', 'cards', c('cd_word', L), None, c('cd_t', L), c('cd_c', L), cy=0.5, wsize=600, alpha=210,
                   fill=(255, 214, 214)), P + '06b_cards_large_1500.jpg')
    save(full_photo(L, 'trolley_a', (0.5, 0.5), c('tr_eye', L), c('tr_t', L), c('tr_s', L), c('tr_c', L),
                    shade_col=(70, 40, 10), strength=0.35, y=380), P + '07_trolley_fullwidth_3000x1500.jpg')
    save(full_photo(L, 'trolley_a', (0.5, 0.5), c('tr_eye', L), c('tr_t', L), c('tr_s', L), c('tr_c', L), mobile=True,
                    mfocus=(0.75, 0.5), shade_col=(70, 40, 10)), P + '07m_trolley_mobile_1500.jpg')
    save(word_tile(L, 'cont_a', 'cont', c('ct_word', L), None, c('ct_t', L), c('ct_c', L), cy=0.5, wsize=620, alpha=0),
         P + '08a_containers_large_1500.jpg')
    save(photo_medium(L, 'basket_a', (0.5, 0.62), c('bk_t', L), c('bk_c', L)), P + '08b_basket_medium_1500x750.jpg')
    save(photo_medium(L, 'gift_a', (0.8, 0.5), c('gf_t', L), c('gf_c', L)), P + '08c_gift_medium_1500x750.jpg')
    for i, g in enumerate(gallery(L)): save(g, P + f'09{"abcdefgh"[i]}_gallery_1500x750.jpg')
    save(kite_story(L), P + '10_story_kite_3000x1500.jpg')
    save(kite_story(L, mobile=True), P + '10m_story_mobile_1500.jpg')
    save(small_label(L, 'umb_b', (0.5, 0.5), c('um_t', L), layeredspec=('umb', c('um_word', L), 0.42, 300, 230)),
         P + '11a_umbrella_small_750.jpg')
    save(small_label(L, 'ball_b', (0.5, 0.5), c('bb_t', L)), P + '11b_ball_small_750.jpg')
    save(small_label(L, 'fan_b', (0.45, 0.5), c('fn_t', L)), P + '11c_fan_small_750.jpg')
    save(small_label(L, 'basket_b', (0.6, 0.55), c('bs_t', L)), P + '11d_basket_small_750.jpg')
    save(full_photo(L, 'ram_a', (0.5, 0.5), c('rm_eye', L), c('rm_t', L), c('rm_s', L), c('rm_c', L),
                    shade_col=(6, 10, 30), strength=0.55, y=420), P + '12_ramadan_teaser_3000x1500.jpg')
    save(why(L), P + '13_why_3000x560.jpg')
    build_ramadan(L)

if __name__ == '__main__':
    for L in (sys.argv[1:] or ['ar', 'en']): build(L)
    print('ok', len(os.listdir(OUT)))
