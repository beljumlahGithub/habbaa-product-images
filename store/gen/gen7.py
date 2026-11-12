#!/usr/bin/env python3
"""HABBAA store v7 — ONE bilingual asset set (Amazon Stores cannot localise images per language).
Arabic stays the headline; English rides as eyebrow / tile sub-label / button twin. No section numbers on strips,
no fake 'shop the scene' badges."""
import os, sys, json
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen2, gen3 as g, gen4 as v4, gen5 as v5
from gen2 import font, kw, tw, logo, INK, TEAL
from gen3 import raw, fit, shade, grain, extend_left, mobile_canvas, GOLD, CREAM, B

OUT = os.path.join(B, 'out7'); os.makedirs(OUT, exist_ok=True); v4.OUT = OUT; v5.OUT = OUT
GREY = v4.GREY; L = 'ar'

class Bi(str):
    en = None
def bi(pair):
    s = Bi(pair[0]); s.en = pair[1]; return s
def EN(s): return getattr(s, 'en', None)

def x7(k, L_='ar'): return bi(v4.X[k])
def c7(k, L_='ar'):
    v = g.C[k]; return bi(v) if isinstance(v, tuple) else v
def r7(k, L_='ar'): return bi(g.R[k])
v4.x = v5.x = x7; g.c = c7; g.r = r7

LAT = str.maketrans('٠١٢٣٤٥٦٧٨٩', '0123456789')
def efont(w, s): return font('en', w, s)
def etw(d, t, w, s): return d.textlength(t, font=efont(w, s))

def cta7(d, x, y, text, lang='ar', size=50, fg='white', bg=TEAL, anchor_right=False, arrow=True):
    """Pill button. Bilingual: Arabic | English, chevron on the far (left) side."""
    en = EN(text); gap = size * 0.9
    wa = int(tw(d, text, 'ar', 'b', size)); we = int(etw(d, en, 'm', int(size * 0.86))) if en else 0
    w = wa + (we + gap * 2 if en else 0) + size * 2.6; h = int(size * 1.9)
    x0 = x - w if anchor_right else x
    d.rounded_rectangle((x0, y, x0 + w, y + h), h // 2, fill=bg); cy = y + h / 2
    rx = x0 + w - size * 0.85
    d.text((rx, cy + size * 0.06), text, font=font('ar', 'b', size), fill=fg, anchor='rm', **kw('ar'))
    if en:
        sx_ = rx - wa - gap
        d.line((sx_, cy - size * 0.42, sx_, cy + size * 0.42), fill=fg, width=max(2, size // 16))
        d.text((sx_ - gap, cy + size * 0.02), en, font=efont('m', int(size * 0.86)), fill=fg, anchor='rm')
    a = size * 0.32; ax = x0 + size * 0.95
    d.line([(ax + a, cy - a), (ax, cy), (ax + a, cy + a)], fill=fg, width=max(4, size // 9), joint='curve')
    return (x0, y, x0 + w, y + h)

def block7(img, L_, x, y, eye=None, title=None, sub=None, button=None, tsize=150, fg='white', eye_col=None,
           btn_bg='white', btn_fg=INK, maxw=None, align=None):
    d = ImageDraw.Draw(img); anc = align or 'r'; maxw = maxw or img.width * 0.42; yy = y
    num = eye.translate(LAT) if eye and eye.translate(LAT).isdigit() else None
    etxt = EN(eye).upper() if EN(eye) else (EN(title) or '')
    if num and etxt: etxt = f'{num}   {etxt}'
    elif num: etxt = num
    if etxt:
        es = max(36, int(tsize * 0.30)); lw = int(tsize * 0.55)
        while etw(d, etxt, 'b', es) + lw + es * 0.6 > maxw and es > 26: es -= 2
        col = eye_col or fg; f = efont('b', es)
        if anc == 'r':
            d.line((x - lw, yy + es * 0.55, x, yy + es * 0.55), fill=col, width=max(3, es // 8))
            d.text((x - lw - es * 0.6, yy), etxt, font=f, fill=col, anchor='ra')
        else:
            d.line((x, yy + es * 0.55, x + lw, yy + es * 0.55), fill=col, width=max(3, es // 8))
            d.text((x + lw + es * 0.6, yy), etxt, font=f, fill=col, anchor='la')
        yy += max(36, int(tsize * 0.30)) * 2.2
    if title:
        s = tsize
        while tw(d, title, 'ar', 'b', s) > maxw and s > 40: s -= 4
        d.text((x, yy), title, font=font('ar', 'b', s), fill=fg, anchor=anc + 'a', **kw('ar'))
        bb = d.textbbox((x, yy), title, font=font('ar', 'b', s), anchor=anc + 'a', **kw('ar')); yy = bb[3] + s * 0.35
    if sub:
        ss = int(tsize * 0.30); lines = []; cur = ''
        for wd in sub.split():
            t = (cur + ' ' + wd).strip()
            if tw(d, t, 'ar', 'r', ss) > maxw and cur: lines.append(cur); cur = wd
            else: cur = t
        lines.append(cur)
        for ln in lines:
            d.text((x, yy), ln, font=font('ar', 'r', ss), fill=fg, anchor=anc + 'a', **kw('ar')); yy += ss * 1.45
        yy += ss * 0.5
    if button:
        bs = int(tsize * 0.27)
        while bs > 24:
            w = tw(d, button, 'ar', 'b', bs) + (etw(d, EN(button), 'm', int(bs * 0.86)) + bs * 1.8 if EN(button) else 0) + bs * 2.6
            if w <= max(maxw, 520): break
            bs -= 2
        yy = cta7(d, x, int(yy), button, 'ar', size=bs, fg=btn_fg, bg=btn_bg, anchor_right=(anc == 'r'))[3]
    return yy
g.block = v4.block = v5.block = block7; g.cta = v4.cta = cta7; gen2.cta = cta7

def tile7(L_, scene, focus, title, size=(750, 750), link=None, word=None, badge=None):
    """Photo tile: Arabic title, English name underneath in gold with a chevron."""
    W, H = size
    if word:
        im = g.layered(scene, word[0], size, focus, word[1], 'ar', word[2], word[3], alpha=word[4],
                       fill=word[5] if len(word) > 5 else (255, 255, 255))
    else:
        im = fit(raw(scene), size, focus).convert('RGBA')
    im = shade(im, 'bottom', 0.55, 0.82, (8, 18, 18)); d = ImageDraw.Draw(im)
    pad = int(W * 0.06) if W <= 750 else 90; xx = W - pad
    ts = {750: 74, 1500: 96}[W] if H < 1500 else 120
    while tw(d, title, 'ar', 'b', ts) > W - 2 * pad: ts -= 4
    base = H - int(ts * 1.75)
    d.text((xx, base), title, font=font('ar', 'b', ts), fill='white', anchor='rs', **kw('ar'))
    fs = int(ts * 0.46); t = EN(title) or 'Explore'
    while etw(d, t, 'm', fs) > W - 2 * pad - fs * 1.4: fs -= 2
    d.text((xx, base + fs * 1.72), t, font=efont('m', fs), fill=GOLD, anchor='rs')
    tl = etw(d, t, 'm', fs); ax = xx - tl - fs * 0.8; cy = base + fs * 1.40; a = fs * 0.28
    d.line([(ax + a, cy - a), (ax, cy), (ax + a, cy + a)], fill=GOLD, width=max(4, fs // 7), joint='curve')
    return im
v4.tile = v5.tile = tile7
v5.scene_tile = lambda L_, scene, focus, title, size=(1500, 1500): tile7(L_, scene, focus, title, size)

def sec7(L_, num, title, sub, W=3000, H=380, bg=CREAM):
    """Title strip: no numbers (they clashed with the cascade 01-04). Arabic title, English twin beside it."""
    im = Image.new('RGBA', (W, H), bg); d = ImageDraw.Draw(im)
    v4.gust(d, W, H, 'left', [TEAL, GOLD, '#60A591']); im = grain(im, 5).convert('RGBA'); d = ImageDraw.Draw(im)
    k = H / 380; xx = W - 170; tsz = int(118 * k ** 0.6); es = int(54 * k ** 0.5)
    en = EN(title) or ''
    if W < 2000:      # mobile strip: stacked
        d.line((xx - 150, H * 0.13, xx, H * 0.13), fill=GOLD, width=7)
        d.text((xx, H * 0.44), title, font=font('ar', 'b', tsz), fill=INK, anchor='rm', **kw('ar'))
        d.text((xx, H * 0.84), en, font=efont('m', int(es * 1.15)), fill=GREY, anchor='rm')
        return im
    cy = H / 2
    d.text((xx, cy), title, font=font('ar', 'b', tsz), fill=INK, anchor='rm', **kw('ar'))
    tl = tw(d, title, 'ar', 'b', tsz); lx = xx - tl - 70
    d.line((lx, cy - tsz * 0.42, lx, cy + tsz * 0.42), fill=GOLD, width=7)
    d.text((lx - 70, cy + 4), en, font=efont('m', int(tsz * 0.62)), fill=GREY, anchor='rm')
    return im
v4.sec = v5.sec = sec7

def phead7(L_, scene, focus, title, shade_col=(6, 40, 42), strength=0.8, ext=False, W=3000, H=600):
    im = (extend_left(raw(scene), (W, H)) if ext else fit(raw(scene), (W, H), focus)).convert('RGBA')
    im = shade(im, 'left', 0.72, max(strength, 0.55), shade_col)
    d = ImageDraw.Draw(im); lg = logo('white', 210); ts = 140; en = EN(title) or ''
    tl = int(max(tw(d, title, 'ar', 'b', ts), etw(d, en, 'm', 62))); gap = 70; x0 = 170
    d.text((x0 + tl, H / 2 - 40), title, font=font('ar', 'b', ts), fill='white', anchor='rm', **kw('ar'))
    d.text((x0 + tl, H / 2 + 95), en, font=efont('m', 62), fill=GOLD, anchor='rm')
    lx = x0 + tl + gap; d.line((lx, H / 2 - 120, lx, H / 2 + 130), fill=GOLD, width=6)
    im.alpha_composite(lg, (lx + gap, int(H / 2 - lg.height / 2)))
    return im
v4.phead = phead7

def header7(L_='ar', W=3000, H=600):
    im = fit(raw('header_b'), (W, H), (0.5, 0.55)).convert('RGBA'); im = shade(im, 'bottom', 0.5, 0.25)
    cx = W * 0.46; pw, ph = 900, 420
    box = (int(cx - pw / 2), int(H / 2 - ph / 2), int(cx + pw / 2), int(H / 2 + ph / 2))
    reg = im.crop(box).filter(ImageFilter.GaussianBlur(26))
    m = Image.new('L', reg.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, pw - 1, ph - 1), 60, fill=255)
    reg.alpha_composite(Image.new('RGBA', reg.size, (6, 70, 72, 150))); im.paste(reg, box[:2], m)
    ImageDraw.Draw(im).rounded_rectangle(box, 60, outline=(255, 255, 255, 120), width=3)
    lg = logo('white', 210); im.alpha_composite(lg, (int(cx - lg.width / 2), int(H / 2 - 180)))
    d = ImageDraw.Draw(im)
    d.text((cx, H / 2 + 75), g.C['tag'][0], font=font('ar', 'm', 46), fill='white', anchor='mm', **kw('ar'))
    d.text((cx, H / 2 + 140), g.C['tag'][1], font=efont('m', 36), fill=GOLD, anchor='mm')
    return im
g.header = header7

def save(im, n):
    p = os.path.join(OUT, n); im.convert('RGB').save(p, quality=90, optimize=True)
    if os.path.getsize(p) > 4_800_000: im.convert('RGB').save(p, quality=82, optimize=True)

def mobile_extras():
    src = Image.open(os.path.join(B, 'v3', 'raw', 'casc_hq.jpg')).convert('RGB')
    src = src.resize((3000, int(src.height * 3000 / src.width)), Image.LANCZOS); H = src.height // 4
    for i in range(4):
        sl = src.crop((0, i * H, 3000, (i + 1) * H)); S = 1500; ih = 1050
        w = int(3000 * ih / H); sl = sl.resize((w, ih), Image.LANCZOS); x0 = w - S if i % 2 == 0 else 0
        sl = sl.crop((x0, 0, x0 + S, ih)); im = Image.new('RGB', (S, S)); top = S - ih
        edge = sl.crop((0, 0, S, 40)).resize((1, 4)).resize((S, top + 120), Image.BICUBIC)
        im.paste(edge.filter(ImageFilter.GaussianBlur(50)), (0, 0)); m = Image.new('L', (1, ih), 255)
        for y in range(120): m.putpixel((0, y), int(255 * y / 120))
        im.paste(sl, (0, top), m.resize((S, ih))); im = shade(im.convert('RGBA'), 'top', 0.45, 0.4, (0, 0, 0))
        k = f'c{i + 1}'
        block7(im, L, 1400, 80, f'{i + 1:02d}', x7(k), x7(k + 's'), x7(k + 'c'), tsize=125, maxw=1300, eye_col=GOLD)
        save(im, f'ar_m_cascade_{i + 1}.jpg')
    save(sec7(L, 0, x7('s2'), '', W=1500, H=420), 'ar_m_sec_best.jpg')
    save(sec7(L, 0, x7('s3'), '', W=1500, H=420), 'ar_m_sec_picks.jpg')
    save(v4.mbanner(L, 'majlis_a', 0.72, None, x7('sh_t'), None, None, shade_col=(30, 18, 6)), 'ar_m_majlis.jpg')
    # mobile squares for the two text-only cards whose desktop text is too small on a phone
    im = Image.new('RGBA', (1500, 1500), CREAM); d = ImageDraw.Draw(im); v4.gust(d, 1500, 1500 * 0.8, 'left', [TEAL, GOLD, '#60A591'])
    im = grain(im, 5).convert('RGBA')
    block7(im, L, 1390, 430, None, x7('vid_t'), x7('vid_s'), x7('vid_c'), tsize=170, fg=INK, btn_bg=TEAL, btn_fg='white', maxw=1280)
    save(im, 'ar_m_card_coffee.jpg')

if __name__ == '__main__':
    json.dump(v5.pages('ar'), open(os.path.join(OUT, 'layout_ar.json'), 'w'), ensure_ascii=False, indent=1)
    mobile_extras()
    print('ok', len(os.listdir(OUT)))
