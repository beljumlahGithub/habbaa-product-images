"""HABBAA Premium A+ 'Pro' template (approved by BJ 2026-11-09).
5 full-image modules, desktop 1464x600 + mobile 600x450, Arabic RTL via raqm.
Restored 2026-11-23 after workspace reset. Fonts: Tajawal-*.ttf in FD.
"""
import os, re
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops

FD = os.environ.get('HB_FONTS', '/home/claude/fonts/')
W, H, MW, MH = 1464, 600, 600, 450
INK = (28, 31, 36); SUB = (92, 96, 104); ACC = (176, 141, 87); BG = (247, 243, 236)
WHITE = (255, 255, 255); DEEP = (34, 52, 60); GOLDT = (200, 178, 140)

BAN = ['مص', 'كس', 'لعن', 'بز', 'ثدي', 'علق', 'هور', 'جن', 'نيك', 'لسبو', 'فوهة', 'شفر', 'عيدالميلاد', 'كريسماس', 'مقبض', 'جماع', 'زنا', 'زب','مني','مخزن','زنى','طيز','قحب','شرموط','عاهر','خول','لوط','سكس','نهد','خصية','عري']
def check(s):
    z = re.sub(r'[ً-ْـ\s]', '', s)
    bad = [b for b in BAN if b in z]
    if bad: raise SystemExit(f'BANNED {bad} in: {s}')
    return s

_fc = {}
def F(w, s):
    k = (w, s)
    if k not in _fc: _fc[k] = ImageFont.truetype(FD + f'Tajawal-{w}.ttf', s, layout_engine=ImageFont.Layout.RAQM)
    return _fc[k]

def tw(d, t, f):
    b = d.textbbox((0, 0), t, font=f, direction='rtl', language='ar'); return b[2] - b[0], b

def rtext(d, xr, y, t, f, fill):
    check(t); w, b = tw(d, t, f); d.text((xr - w - b[0], y), t, font=f, fill=fill, direction='rtl', language='ar'); return w

def ctext(d, xc, y, t, f, fill):
    check(t); w, b = tw(d, t, f); d.text((xc - w / 2 - b[0], y), t, font=f, fill=fill, direction='rtl', language='ar'); return w

def fit(d, t, w, s, maxw, mn=16):
    while s > mn and tw(d, t, F(w, s))[0] > maxw: s -= 1
    return F(w, s)

def wrap(d, t, f, maxw):
    lines = ['']
    for wd in t.split():
        tt = (lines[-1] + ' ' + wd).strip()
        if tw(d, tt, f)[0] > maxw and lines[-1]: lines.append(wd)
        else: lines[-1] = tt
    return lines

def cover(im, w, h, ax=0.5, ay=0.5):
    im = im.convert('RGB'); r = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    x = round((im.width - w) * ax); y = round((im.height - h) * ay)
    return im.crop((x, y, x + w, y + h))

def contain(im, w, h, bg=WHITE):
    im = im.convert('RGB'); im.thumbnail((w, h), Image.LANCZOS)
    c = Image.new('RGB', (w, h), bg); c.paste(im, ((w - im.width) // 2, (h - im.height) // 2)); return c

def trim_white(im, thr=18):
    im = im.convert('RGB'); bb = ImageChops.difference(im, Image.new('RGB', im.size, 'white')).point(lambda v: 255 if v > thr else 0).getbbox()
    return im.crop(bb) if bb else im

def rmask(size, r):
    m = Image.new('L', size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), r, fill=255); return m

def hmask(w, h, x0, x1, rev=False):
    a = np.clip((np.arange(w) - x0) / max(1, (x1 - x0)), 0, 1)
    if rev: a = 1 - a
    return Image.fromarray(np.tile((a * 255).astype('uint8'), (h, 1)))

def vmask(w, h, y0, y1, rev=False):
    a = np.clip((np.arange(h) - y0) / max(1, (y1 - y0)), 0, 1)
    if rev: a = 1 - a
    return Image.fromarray(np.tile((a * 255).astype('uint8')[:, None], (1, w)))

def shadow(base, box, r=24, off=10, blur=22, alpha=55):
    sh = Image.new('L', base.size, 0); ImageDraw.Draw(sh).rounded_rectangle((box[0], box[1] + off, box[2], box[3] + off), r, fill=alpha)
    base.paste(Image.new('RGB', base.size, (0, 0, 0)), (0, 0), sh.filter(ImageFilter.GaussianBlur(blur)))

def pill(d, xr, y, t, f, fg, bg, pad=22, h=56):
    w = tw(d, t, f)[0] + pad * 2
    d.rounded_rectangle((xr - w, y, xr, y + h), h // 2, fill=bg)
    rtext(d, xr - pad, y + (h - f.size) / 2 - 2, t, f, fg); return xr - w

def tick(d, cx, cy, r=26):
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=DEEP)
    d.line([(cx - r * .42, cy + r * .02), (cx - r * .1, cy + r * .34), (cx + r * .45, cy - r * .32)], fill=WHITE, width=max(4, r // 5), joint='curve')

def hero(c, out):
    src = Image.open(c['img'])
    im = cover(src, W, H, c.get('ax', 0.0), c.get('ay', 0.5))
    im.paste(Image.new('RGB', (W, H), BG), (0, 0), hmask(W, H, c.get('fade0', 520), c.get('fade1', 860)).point(lambda v: int(v * .9)))
    d = ImageDraw.Draw(im); xr = W - 80; maxw = 700
    rtext(d, xr, 62, 'HABBAA', F('Bold', 34), ACC)
    y = 112
    for ln in c['head']:
        f = fit(d, ln, 'ExtraBold', 86, maxw); rtext(d, xr, y, ln, f, INK); y += f.size + 14
    y += 18
    for ln in wrap(d, c['sub'], F('Medium', 36), maxw)[:2]:
        rtext(d, xr, y, ln, F('Medium', 36), SUB); y += 48
    y += 26; x = xr
    for i, ch in enumerate(c.get('chips', [])[:3]):
        x = pill(d, x, y, ch, F('Bold', 30), WHITE if i == 0 else INK, DEEP if i == 0 else WHITE) - 14
        assert x > 640, 'chips overflow'
    im.save(out + '-desktop.jpg', quality=93)
    m = Image.new('RGB', (MW, MH), BG); m.paste(cover(src, MW, 250, c.get('ax', 0.0) * 0.5 + 0.1, c.get('ay', 0.5)), (0, 0))
    m.paste(Image.new('RGB', (MW, 60), BG), (0, 190), vmask(MW, 60, 0, 60)); d = ImageDraw.Draw(m)
    t = ' '.join(c['head']); rtext(d, MW - 28, 262, t, fit(d, t, 'ExtraBold', 40, MW - 56), INK)
    for j, ln in enumerate(wrap(d, c['sub'], F('Medium', 23), MW - 56)[:2]): rtext(d, MW - 28, 322 + j * 32, ln, F('Medium', 23), SUB)
    x = MW - 28
    for i, ch in enumerate(c.get('chips', [])[:3]):
        x = pill(d, x, 392, ch, F('Bold', 19), WHITE if i == 0 else INK, DEEP if i == 0 else WHITE, pad=14, h=40) - 8
    m.save(out + '-mobile.jpg', quality=93)

def features(c, out):
    im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    card = (50, 60, 450, 540); shadow(im, card); d.rounded_rectangle(card, 28, fill=WHITE)
    p = Image.open(c['prod']).convert('RGB')
    if c.get('photo'):
        ph = cover(p, 360, 440); im.paste(ph, (card[0] + 20, card[1] + 20), rmask(ph.size, 20))
    else:
        p = trim_white(p); p.thumbnail((330, 410), Image.LANCZOS); im.paste(p, (card[0] + (400 - p.width) // 2, card[1] + (480 - p.height) // 2))
    xr = W - 70
    rtext(d, xr, 48, c['title'], fit(d, c['title'], 'ExtraBold', 60, 880), INK)
    rtext(d, xr, 126, c['sub'], fit(d, c['sub'], 'Medium', 32, 880), SUB)
    cw, ch = 440, 170
    for i, (t, s) in enumerate(c['feats'][:4]):
        col, row = i % 2, i // 2
        x2 = xr - col * (cw + 24); x1 = x2 - cw; y1 = 200 + row * (ch + 22)
        d.rounded_rectangle((x1, y1, x2, y1 + ch), 22, fill=WHITE)
        tick(d, x2 - 58, y1 + 52, 26)
        rtext(d, x2 - 104, y1 + 26, t, fit(d, t, 'ExtraBold', 31, cw - 130), INK)
        ls = wrap(d, s, F('Medium', 24), cw - 130); assert len(ls) <= 2, ('feature sub too long', s)
        for j, ln in enumerate(ls): rtext(d, x2 - 104, y1 + 76 + j * 34, ln, F('Medium', 24), SUB)
    im.save(out + '-desktop.jpg', quality=93)
    m = Image.new('RGB', (MW, MH), BG); d = ImageDraw.Draw(m)
    rtext(d, MW - 24, 18, c['title'], fit(d, c['title'], 'ExtraBold', 34, MW - 48), INK)
    pc = (24, 76, 214, 426); d.rounded_rectangle(pc, 18, fill=WHITE)
    if c.get('photo'):
        ph = cover(p, 170, 330); m.paste(ph, (34, 86), rmask(ph.size, 14))
    else:
        q = p.copy(); q.thumbnail((170, 330), Image.LANCZOS); m.paste(q, (pc[0] + (190 - q.width) // 2, pc[1] + (350 - q.height) // 2))
    for i, (t, s) in enumerate(c['feats'][:4]):
        y = 80 + i * 88; d.rounded_rectangle((232, y, MW - 24, y + 78), 14, fill=WHITE)
        tick(d, MW - 50, y + 39, 15)
        rtext(d, MW - 76, y + 10, t, fit(d, t, 'Bold', 22, 270), INK)
        rtext(d, MW - 76, y + 42, s, fit(d, s, 'Medium', 16, 270, mn=12), SUB)
    m.save(out + '-mobile.jpg', quality=93)

def steps(c, out):
    im = Image.new('RGB', (W, H), WHITE); d = ImageDraw.Draw(im)
    ctext(d, W / 2, 30, c['title'], fit(d, c['title'], 'ExtraBold', 54, 1200), INK)
    pw, ph = 420, 330
    for i, (f, t, s) in enumerate(c['steps'][:3]):
        xr = W - 60 - i * (pw + 42); x1 = xr - pw; y1 = 120
        p = cover(Image.open(f), pw, ph); im.paste(p, (x1, y1), rmask(p.size, 24))
        d.ellipse((xr - 76, y1 + 16, xr - 16, y1 + 76), fill=DEEP); ctext(d, xr - 46, y1 + 24, str(i + 1), F('ExtraBold', 38), WHITE)
        rtext(d, xr, y1 + ph + 18, t, fit(d, t, 'ExtraBold', 34, pw), INK)
        ls = wrap(d, s, F('Medium', 24), pw); assert len(ls) <= 2, ('step sub too long', s)
        for j, ln in enumerate(ls): rtext(d, xr, y1 + ph + 64 + j * 32, ln, F('Medium', 24), SUB)
        if i < 2:
            ax = x1 - 21; ay = y1 + ph / 2; d.polygon([(ax + 8, ay - 14), (ax + 8, ay + 14), (ax - 10, ay)], fill=ACC)
    im.save(out + '-desktop.jpg', quality=93)
    m = Image.new('RGB', (MW, MH), WHITE); d = ImageDraw.Draw(m)
    ctext(d, MW / 2, 16, c['title'], fit(d, c['title'], 'ExtraBold', 32, MW - 40), INK)
    tw_, th_ = 180, 210
    for i, (f, t, s) in enumerate(c['steps'][:3]):
        xr = MW - 15 - i * (tw_ + 15); x1 = xr - tw_
        p = cover(Image.open(f), tw_, th_); m.paste(p, (x1, 70), rmask(p.size, 14))
        d.ellipse((xr - 44, 78, xr - 10, 112), fill=DEEP); ctext(d, xr - 27, 81, str(i + 1), F('ExtraBold', 22), WHITE)
        for j, ln in enumerate(wrap(d, t, F('Bold', 20), tw_)[:2]): rtext(d, xr, 292 + j * 28, ln, F('Bold', 20), INK)
        for j, ln in enumerate(wrap(d, s, F('Medium', 15), tw_)[:3]): rtext(d, xr, 352 + j * 22, ln, F('Medium', 15), SUB)
    m.save(out + '-mobile.jpg', quality=93)

def uses(c, out):
    im = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(im)
    rtext(d, W - 70, 36, c['title'], fit(d, c['title'], 'ExtraBold', 54, 1300), INK)
    rtext(d, W - 70, 108, c['sub'], fit(d, c['sub'], 'Medium', 30, 1300), SUB)
    tw_, th = 316, 330; gap = 26
    for i, (f, lab) in enumerate(c['tiles'][:4]):
        xr = W - 70 - i * (tw_ + gap); x1 = xr - tw_; y1 = 176
        t = cover(Image.open(f), tw_, th); im.paste(t, (x1, y1), rmask(t.size, 22))
        fl = fit(d, lab, 'Bold', 30, tw_ - 70); bw = tw(d, lab, fl)[0] + 40
        d.rounded_rectangle((xr - 16 - bw, y1 + th - 70, xr - 16, y1 + th - 16), 27, fill=WHITE)
        rtext(d, xr - 36, y1 + th - 63, lab, fl, INK)
    if c.get('note'): rtext(d, W - 70, 532, c['note'], fit(d, c['note'], 'Medium', 26, 1300), SUB)
    im.save(out + '-desktop.jpg', quality=93)
    m = Image.new('RGB', (MW, MH), BG); d = ImageDraw.Draw(m)
    rtext(d, MW - 24, 16, c['title'], fit(d, c['title'], 'ExtraBold', 32, MW - 48), INK)
    tw2, th2 = 270, 172
    for i, (f, lab) in enumerate(c['tiles'][:4]):
        col, row = i % 2, i // 2; xr = MW - 20 - col * (tw2 + 20); x1 = xr - tw2; y1 = 70 + row * (th2 + 14)
        t = cover(Image.open(f), tw2, th2); m.paste(t, (x1, y1), rmask(t.size, 14))
        fl = fit(d, lab, 'Bold', 19, tw2 - 40); bw = tw(d, lab, fl)[0] + 24
        d.rounded_rectangle((xr - 10 - bw, y1 + th2 - 42, xr - 10, y1 + th2 - 10), 16, fill=WHITE)
        rtext(d, xr - 22, y1 + th2 - 39, lab, fl, INK)
    m.save(out + '-mobile.jpg', quality=93)

def specs(c, out):
    im = Image.new('RGB', (W, H), DEEP); d = ImageDraw.Draw(im)
    rt = cover(Image.open(c['img']), 640, H, c.get('ax', 0.1), c.get('ay', 0.5)); im.paste(rt, (0, 0), hmask(640, H, 420, 640, rev=True))
    xr = W - 80; rows = c['rows'][:6]
    rtext(d, xr, 52, c.get('title', 'المواصفات'), F('ExtraBold', 58), WHITE)
    step = 66 if len(rows) >= 6 else 74
    for i, (k, v) in enumerate(rows):
        y = 150 + i * step
        rtext(d, xr, y, k, F('Bold', 32), GOLDT)
        rtext(d, xr - 230, y, v, fit(d, v, 'Medium', 32, 520), WHITE)
        if i < len(rows) - 1: d.line((xr - 640, y + step - 12, xr, y + step - 12), fill=(70, 88, 96), width=2)
    im.save(out + '-desktop.jpg', quality=93)
    m = Image.new('RGB', (MW, MH), DEEP); d = ImageDraw.Draw(m)
    rtext(d, MW - 28, 20, c.get('title', 'المواصفات'), F('ExtraBold', 36), WHITE)
    st = 58 if len(rows) >= 6 else 64
    for i, (k, v) in enumerate(rows):
        y = 86 + i * st
        rtext(d, MW - 28, y, k, F('Bold', 22), GOLDT)
        rtext(d, MW - 200, y, v, fit(d, v, 'Medium', 22, 360), WHITE)
        if i < len(rows) - 1: d.line((28, y + st - 12, MW - 28, y + st - 12), fill=(70, 88, 96), width=1)
    m.save(out + '-mobile.jpg', quality=93)

def build(cfg, outdir):
    os.makedirs(outdir, exist_ok=True); n = cfg['id']; outs = []
    mods = [('1-hero', hero, 'hero'), ('2-feat', features, 'feat'), ('3-steps', steps, 'steps'), ('4-uses', uses, 'uses'), ('5-specs', specs, 'specs')]
    for tag, fn, key in mods:
        if cfg.get(key):
            p = f'{outdir}/{n}-{tag}'; globals()[fn.__name__](cfg[key], p); outs.append(p)
    return outs

def sheet(outs, path):
    ims = [Image.open(o + '-desktop.jpg') for o in outs]; mob = [Image.open(o + '-mobile.jpg') for o in outs]
    s = Image.new('RGB', (W + 20 + MW, len(ims) * (H + 12)), (225, 225, 225))
    for i, (a, b) in enumerate(zip(ims, mob)):
        s.paste(a, (0, i * (H + 12))); s.paste(b, (W + 20, i * (H + 12)))
    s.resize((s.width // 2, s.height // 2)).save(path, quality=85)
