import json, os, re, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

B = '/home/claude/b14'
FD = '/home/claude/fonts'
S = 2000
BG = (247, 245, 241); PANEL = (255, 255, 255); SOFT = (238, 234, 226)
INK = (30, 33, 38); SUB = (98, 102, 110); ACC = (176, 141, 87); ACC2 = (120, 92, 52)
KW = dict(direction='rtl', language='ar')
_fc = {}
def F(w, s):
    k = (w, s)
    if k not in _fc: _fc[k] = ImageFont.truetype(f'{FD}/Tajawal-{w}.ttf', s, layout_engine=ImageFont.Layout.RAQM)
    return _fc[k]

C = json.load(open(f'{B}/C14.json'))
_S = json.load(open(f'{B}/sel14.json'))
N = _S['N']
PP = _S['P']

DIMR = re.compile(r'(?<!\u2066)(\d+(?:[.,]\d+)?(?:\s*×\s*\d+(?:[.,]\d+)?)+)')
def fx(s): return s
def tl(d, s, f): return d.textlength(fx(s), font=f, **KW)
def rtext(d, right, y, s, f, fill): d.text((right - tl(d, s, f), y), fx(s), font=f, fill=fill, **KW)
def ctext(d, cx, y, s, f, fill): d.text((cx - tl(d, s, f) / 2, y), fx(s), font=f, fill=fill, **KW)
def wrap(d, s, f, maxw):
    out, cur = [], ''
    for w in s.split():
        t = (cur + ' ' + w).strip()
        if tl(d, t, f) <= maxw: cur = t
        else:
            if cur: out.append(cur)
            cur = w
    if cur: out.append(cur)
    return out
def fit_lines(d, s, f, maxw, n):
    L = wrap(d, s, f, maxw)
    if len(L) > n:
        L = L[:n]
        # end on a complete clause: trim words until it ends cleanly
        last = L[-1].split()
        while len(last) > 2 and tl(d, ' '.join(last) + '…', f) > maxw: last = last[:-1]
        L[-1] = ' '.join(last).rstrip('،,.') + '…'
    return L

def split(b):
    if ':' in b:
        h, r = b.split(':', 1); return h.strip(), r.strip()
    return '', b.strip()

def product(a):
    im = Image.open(f'{B}/' + PP[a]).convert('RGB')
    arr = np.asarray(im).astype(int)
    m = arr.min(axis=2) < 238
    ys, xs = np.where(m)
    if len(xs) > 200:
        pad = int(0.01 * max(im.size))
        im = im.crop((max(xs.min() - pad, 0), max(ys.min() - pad, 0), min(xs.max() + pad, im.width), min(ys.max() + pad, im.height)))
    return im

def white_to_alpha(im):
    """soft mask: near-white pixels become transparent so the product sits on any panel colour"""
    a = np.asarray(im.convert('RGB')).astype(np.float32)
    mn = a.min(axis=2)
    alpha = np.clip((250 - mn) * 255 / 22, 0, 255).astype(np.uint8)
    rgba = im.convert('RGBA'); rgba.putalpha(Image.fromarray(alpha).filter(ImageFilter.GaussianBlur(0.8)))
    return rgba

def place(canvas, im, box, shadow=False):
    x, y, w, h = box
    r = min(w / im.width, h / im.height)
    im2 = im.resize((max(1, int(im.width * r)), max(1, int(im.height * r))), Image.LANCZOS)
    px, py = x + (w - im2.width) // 2, y + (h - im2.height) // 2
    rgba = white_to_alpha(im2)
    if shadow:
        sh = Image.new('RGBA', canvas.size, (0, 0, 0, 0))
        ell = Image.new('L', (int(im2.width * 0.8), max(20, int(im2.height * 0.06))), 0)
        ImageDraw.Draw(ell).ellipse((0, 0, ell.width, ell.height), fill=70)
        ell = ell.filter(ImageFilter.GaussianBlur(18))
        sh.paste((0, 0, 0, 255), (px + int(im2.width * 0.1), py + im2.height - ell.height // 2), ell)
        canvas.alpha_composite(sh) if canvas.mode == 'RGBA' else None
    if canvas.mode == 'RGBA': canvas.alpha_composite(rgba, (px, py))
    else: canvas.paste(rgba, (px, py), rgba)
    return (px, py, im2.width, im2.height)

def brandbar(d, title, sub=None):
    f = F('ExtraBold', 40)
    rtext(d, S - 130, 112, 'HABBAA', f, ACC)
    d.text((130, 112), 'HABBAA', font=f, fill=ACC) if False else None
    rtext(d, S - 130, 168, title, F('ExtraBold', 84), INK)
    y = 290
    if sub:
        rtext(d, S - 130, 282, sub, F('Medium', 44), SUB); y = 360
    d.rectangle((S - 130 - 160, y, S - 130, y + 8), fill=ACC)
    return y + 8

def bullets(a):
    out = []
    for b in C[a]['ar']['b']:
        h, r = split(b)
        if 'محتوى العبوة' in h: continue
        out.append((h, r))
    return out

def box_text(a):
    for b in C[a]['ar']['b']:
        h, r = split(b)
        if 'محتوى العبوة' in h:
            r = r.split('.')[0].split('؛')[0].strip()
            return r if len(r) <= 90 else None
    return None

def short_title(a):
    t = re.sub(r'^HABBAA\s*', '', C[a]['ar']['t'])
    return t.split('،')[0].strip()

# ---------------- designs ----------------
def lifestyle(a, k, idx, out):
    p = f'{B}/life/{a}_{k}.jpg'
    im = Image.open(p).convert('RGB')
    ar = im.width / im.height
    if 0.8 <= ar <= 1.25:
        r = max(S / im.width, S / im.height)
        im2 = im.resize((int(im.width * r) + 1, int(im.height * r) + 1), Image.LANCZOS)
        x = (im2.width - S) // 2; y = (im2.height - S) // 2
        c = im2.crop((x, y, x + S, y + S))
    else:
        r = max(S / im.width, S / im.height)
        bg = im.resize((int(im.width * r) + 1, int(im.height * r) + 1), Image.LANCZOS)
        bg = bg.crop(((bg.width - S) // 2, (bg.height - S) // 2, (bg.width - S) // 2 + S, (bg.height - S) // 2 + S))
        bg = bg.filter(ImageFilter.GaussianBlur(40))
        bg = Image.blend(bg, Image.new('RGB', (S, S), (20, 20, 20)), 0.15)
        r2 = min(S / im.width, S / im.height)
        fg = im.resize((int(im.width * r2), int(im.height * r2)), Image.LANCZOS)
        bg.paste(fg, ((S - fg.width) // 2, (S - fg.height) // 2)); c = bg
    c = c.filter(ImageFilter.UnsharpMask(2, 60, 2)).convert('RGBA')
    # bottom gradient for caption
    g = Image.new('L', (1, 560))
    for yy in range(560): g.putpixel((0, yy), int(205 * (yy / 559) ** 1.6))
    g = g.resize((S, 560))
    ov = Image.new('RGBA', (S, 560), (12, 12, 14, 0)); ov.putalpha(g)
    c.alpha_composite(ov, (0, S - 560))
    d = ImageDraw.Draw(c)
    bl = bullets(a); h, r = bl[idx % len(bl)]
    head = h or short_title(a)
    rtext(d, S - 120, S - 330, 'HABBAA', F('ExtraBold', 40), (226, 200, 150))
    y = S - 270
    for ln in fit_lines(d, head, F('ExtraBold', 84), S - 240, 1):
        rtext(d, S - 120, y, ln, F('ExtraBold', 84), (255, 255, 255)); y += 100
    for ln in fit_lines(d, r, F('Medium', 44), S - 240, 1):
        rtext(d, S - 120, y + 4, ln, F('Medium', 44), (235, 235, 235))
    c.convert('RGB').save(out, quality=93)

def features(a, out):
    im = product(a)
    c = Image.new('RGBA', (S, S), BG + (255,)); d = ImageDraw.Draw(c)
    brandbar(d, 'المميزات الرئيسية', short_title(a))
    d.rounded_rectangle((130, 420, S - 130, 1080), 48, fill=PANEL)
    place(c, im, (230, 460, S - 460, 580))
    bl = bullets(a)[:4]
    cw, ch = (S - 260 - 40) // 2, 400
    for i, (h, r) in enumerate(bl):
        col, row = i % 2, i // 2
        x1 = S - 130 - col * (cw + 40); x0 = x1 - cw; y0 = 1120 + row * (ch + 40)
        d.rounded_rectangle((x0, y0, x1, y0 + ch), 40, fill=PANEL)
        cx, cy = x1 - 85, y0 + 85
        d.ellipse((cx - 44, cy - 44, cx + 44, cy + 44), fill=ACC)
        n = str(i + 1); fn = F('ExtraBold', 52); d.text((cx - d.textlength(n, font=fn) / 2, cy - 34), n, font=fn, fill=(255, 255, 255))
        hh = h or short_title(a)
        hl = fit_lines(d, hh, F('Bold', 52), cw - 200, 1)
        rtext(d, x1 - 160, y0 + 50, hl[0], F('Bold', 52), INK)
        yy = y0 + 150
        for ln in fit_lines(d, r, F('Medium', 38), cw - 90, 4):
            rtext(d, x1 - 50, yy, ln, F('Medium', 38), SUB); yy += 54
    c.convert('RGB').save(out, quality=93)

def box(a, out):
    im = product(a); q = box_text(a)
    c = Image.new('RGBA', (S, S), BG + (255,)); d = ImageDraw.Draw(c)
    if q:
        brandbar(d, 'محتويات العبوة')
    else:
        brandbar(d, 'لمحة سريعة', short_title(a))
    d.rounded_rectangle((130, 440, S - 130, 1460), 48, fill=PANEL)
    place(c, im, (230, 500, S - 460, 900))
    y = 1530
    if q:
        f = F('ExtraBold', 64)
        L = fit_lines(d, q, f, S - 420, 2)
        hgt = 60 + 86 * len(L)
        d.rounded_rectangle((180, y, S - 180, y + hgt), 44, fill=INK)
        yy = y + 30
        for ln in L: ctext(d, S / 2, yy, ln, f, (255, 255, 255)); yy += 86
    else:
        hs = [h for h, r in bullets(a) if h][:3]
        n = len(hs); gap = 30; w = (S - 260 - gap * (n - 1)) // max(n, 1)
        for i, h in enumerate(hs):
            x1 = S - 130 - i * (w + gap); x0 = x1 - w
            d.rounded_rectangle((x0, y, x1, y + 200), 36, outline=ACC, width=5, fill=PANEL)
            f = F('Bold', 50)
            L = fit_lines(d, h, f, w - 60, 2)
            yy = y + 100 - 32 * len(L)
            for ln in L: ctext(d, (x0 + x1) / 2, yy, ln, f, INK); yy += 64
    c.convert('RGB').save(out, quality=93)

MR = re.compile(r'(\d+(?:[.,]\d+)?\s*[×xX\*]\s*\d+(?:[.,]\d+)?(?:\s*[×xX\*]\s*\d+(?:[.,]\d+)?)?\s*(?:سم|مم|م)(?![ء-ي])|\d+(?:[.,]\d+)?\s*(?:سم|مم|مل|لتر|جرام|غرام|كجم|متر|م|حبة|قطعة|ورقة|زوج)(?![ء-ي]))')
def specs_list(a):
    seen = []
    for s in [C[a]['ar']['t']] + C[a]['ar']['b']:
        for mo in MR.finditer(s):
            m = mo.group(1)
            if re.search(r'(حوالي|تقريباً|تقريبا)\s*$', s[:mo.start()]): m = 'حوالي ' + m
            k = re.sub(r'\s+', ' ', m).replace('*', '×').replace('x', '×').replace('X', '×').strip()
            base = lambda z: z.replace('حوالي ', '')
            if base(k) not in [base(z) for z in seen] and not any('×' in p and k.split()[-2] in p.split('×') + [p.split()[0].split('×')[-1]] for p in seen): seen.append(k)
    return seen[:4]

def specs(a, out):
    im = product(a)
    c = Image.new('RGBA', (S, S), BG + (255,)); d = ImageDraw.Draw(c)
    brandbar(d, 'المواصفات', short_title(a))
    segs = [s.strip() for s in re.sub(r'^HABBAA\s*', '', C[a]['ar']['t']).split('،')[1:] if s.strip()]
    ds = specs_list(a)
    rows = segs[:4 if ds else 5]
    H = (270 if ds else 0) + 130 * len(rows)
    pb = S - 120 - H - 40
    d.rounded_rectangle((130, 420, S - 130, pb), 48, fill=PANEL)
    place(c, im, (230, 470, S - 460, pb - 520))
    y = pb + 40
    if ds:
        n = len(ds); gap = 30; w = (S - 260 - gap * (n - 1)) // n
        for i, v in enumerate(ds):
            x1 = S - 130 - i * (w + gap); x0 = x1 - w
            d.rounded_rectangle((x0, y, x1, y + 220), 36, fill=INK)
            f = F('ExtraBold', 76 if tl(d, v, F('ExtraBold', 76)) < w - 60 else 54)
            ctext(d, (x0 + x1) / 2, y + 62, v, f, (255, 255, 255))
        y += 270
    for s in rows:
        d.rounded_rectangle((130, y, S - 130, y + 110), 28, fill=PANEL)
        d.ellipse((S - 200, y + 43, S - 176, y + 67), fill=ACC)
        ln = fit_lines(d, s, F('Bold', 46), S - 420, 1)[0]
        rtext(d, S - 230, y + 30, ln, F('Bold', 46), INK)
        y += 130
        if y > S - 140: break
    c.convert('RGB').save(out, quality=93)

NOCROP = {'B0F8HPRKW1','B0FJNH6GDJ','B0FL2R69R5','B0FL2V7XL5','B0FLK9M9LT'}
WIDE = {'B0F8HPRKW1','B0FJNH6GDJ','B0FL2R69R5','B0FL2V7XL5','B0FLK9M9LT'}
def detail(im, wide=False):
    g = np.asarray(im.convert('L')).astype(np.float32)
    e = np.abs(np.diff(g, axis=0))[:, :-1] + np.abs(np.diff(g, axis=1))[:-1, :]
    H, W = e.shape; best = None
    for frac in (0.45, 0.6):
        cw, ch = int(W * frac), int(H * frac)
        for i in range(5):
            for j in range(5):
                x = int((W - cw) * i / 4); y = int((H - ch) * j / 4)
                sc = e[y:y + ch, x:x + cw].mean() * (1.1 if frac == 0.45 else 1.0)
                if best is None or sc > best[0]: best = (sc, x, y, cw, ch)
    sc, x, y, cw, ch = best
    if sc < 4 or wide:  # almost featureless product: show most of it
        cw, ch = int(W * 0.85), int(H * 0.85); x, y = (W - cw) // 2, (H - ch) // 2
    return im.crop((x, y, x + cw, y + ch))

def closeup(a, out):
    im = product(a)
    c = Image.new('RGBA', (S, S), BG + (255,)); d = ImageDraw.Draw(c)
    bl = bullets(a); h, r = bl[1 % len(bl)]
    brandbar(d, 'تفاصيل عن قرب', h or None)
    # detail crop: central 55% of the product
    if a in NOCROP:
        d.rounded_rectangle((130, 440, S - 130, 1580), 48, fill=PANEL)
        place(c, im, (200, 490, S - 400, 1040))
        yy = 1660
        for ln in fit_lines(d, r, F('Medium', 46), S - 260, 3):
            rtext(d, S - 130, yy, ln, F('Medium', 46), SUB); yy += 66
        c.convert('RGB').save(out, quality=93); return
    crop = detail(im, a in WIDE)
    D = 1100; cx, cy = 130 + D // 2, 470 + D // 2
    r_ = max(D / crop.width, D / crop.height)
    cz = crop.resize((int(crop.width * r_) + 1, int(crop.height * r_) + 1), Image.LANCZOS)
    cz = cz.crop(((cz.width - D) // 2, (cz.height - D) // 2, (cz.width - D) // 2 + D, (cz.height - D) // 2 + D))
    mask = Image.new('L', (D, D), 0); ImageDraw.Draw(mask).ellipse((0, 0, D, D), fill=255)
    d.ellipse((cx - D // 2 - 14, cy - D // 2 - 14, cx + D // 2 + 14, cy + D // 2 + 14), fill=ACC)
    c.paste(cz, (cx - D // 2, cy - D // 2), mask)
    d.rounded_rectangle((1290, 520, S - 130, 1100), 40, fill=PANEL)
    place(c, im, (1330, 560, S - 130 - 1330 - 40, 500))
    yy = 1660
    for ln in fit_lines(d, r, F('Medium', 46), S - 260, 3):
        rtext(d, S - 130, yy, ln, F('Medium', 46), SUB); yy += 66
    c.convert('RGB').save(out, quality=93)

ZIP = []
def zipsizes(a, out):
    c = Image.new('RGBA', (S, S), BG + (255,)); d = ImageDraw.Draw(c)
    brandbar(d, 'اختر المقاس المناسب', 'أكياس سحاب شفافة من HABBAA بعدة مقاسات')
    d.rounded_rectangle((130, 440, S - 130, 1640), 48, fill=PANEL)
    k = 1000 / 28  # px per cm, tallest bag 28 cm -> 1000 px
    xs = S - 190; base = 1430
    for asin, w, h in ZIP:
        pw, ph = int(w * k * 0.62), int(h * k * 0.62)
        cur = asin == a
        lab = '\u2066' + f'{w}×{h}' + '\u2069 سم'
        fl = F('ExtraBold' if cur else 'Bold', 46)
        slot = max(pw, int(tl(d, lab, fl)) + 20)
        x1 = xs - (slot - pw) // 2; x0 = x1 - pw
        d.rounded_rectangle((x0, base - ph, x1, base), 10, fill=(255, 255, 255), outline=ACC if cur else (200, 200, 200), width=8 if cur else 3)
        d.rectangle((x0 + 8, base - ph + 22, x1 - 8, base - ph + 30), fill=(214, 60, 60))
        ctext(d, (x0 + x1) / 2, base + 34, lab, fl, ACC2 if cur else SUB)
        xs = xs - slot - 50
    d.rounded_rectangle((180, 1700, S - 180, 1840), 44, fill=INK)
    ctext(d, S / 2, 1730, 'المقاس المحدد لهذا المنتج باللون الذهبي', F('Bold', 56), (255, 255, 255))
    c.convert('RGB').save(out, quality=93)

ORDER = ['features', 'box', 'specs']
def plan(a):
    need = max(0, 7 - N[a])
    has1 = os.path.exists(f'{B}/life/{a}_0.jpg'); has2 = os.path.exists(f'{B}/life/{a}_1.jpg')
    seq = []
    for t in ORDER:
        if t == 'life1' and not has1: continue
        if t == 'life2' and not has2: continue
        seq.append(t)
    return seq[:need]

def make(a, outdir=f'{B}/gal'):
    os.makedirs(outdir, exist_ok=True); files = []
    for i, t in enumerate(plan(a)):
        out = f'{outdir}/{a}_{i + 1}_{t}.jpg'
        if t == 'life1': lifestyle(a, 0, 0, out)
        elif t == 'life2': lifestyle(a, 1, 2, out)
        elif t == 'features': features(a, out)
        elif t == 'box': box(a, out)
        elif t == 'specs': specs(a, out)
        elif t == 'closeup':
            if a in [z[0] for z in ZIP]: zipsizes(a, out)
            else: closeup(a, out)
        files.append(out)
    return files

if __name__ == '__main__':
    asins = sys.argv[1:] or list(C)
    for a in asins:
        try: print(a, len(make(a)))
        except Exception as e: print('ERR', a, repr(e))
