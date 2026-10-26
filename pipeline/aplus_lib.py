"""HABBAA A+ composer — Premium full-image modules.
Desktop 1464x600, mobile 600x450. Arabic RTL text rendered with libraqm.
"""
import os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

FONT_DIR = os.environ.get('HB_FONTS', os.path.join(os.path.dirname(__file__), 'fonts'))
INK = (38, 41, 46)
SUB = (92, 96, 102)
ACC = (176, 141, 87)
BG = (247, 245, 241)
DW, DH = 1464, 600
MW, MH = 600, 450


def font(w, s):
    return ImageFont.truetype(os.path.join(FONT_DIR, f'Tajawal-{w}.ttf'), s,
                              layout_engine=ImageFont.Layout.RAQM)


def tw(d, txt, f):
    b = d.textbbox((0, 0), txt, font=f, direction='rtl', language='ar')
    return b[2] - b[0], b


def rtext(d, xr, y, txt, f, fill):
    w, b = tw(d, txt, f)
    d.text((xr - w - b[0], y - b[1]), txt, font=f, fill=fill, direction='rtl', language='ar')
    return w


def ctext(d, xc, y, txt, f, fill):
    w, b = tw(d, txt, f)
    d.text((xc - w / 2 - b[0], y - b[1]), txt, font=f, fill=fill, direction='rtl', language='ar')
    return w


def fit(d, txt, weight, size, maxw):
    """Shrink font until text fits maxw."""
    while size > 14:
        f = font(weight, size)
        if tw(d, txt, f)[0] <= maxw:
            return f
        size -= 1
    return font(weight, size)


def cover(im, W, H, ax=0.5, ay=0.5):
    r = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * r), round(im.height * r)), Image.LANCZOS)
    x = int((im.width - W) * ax)
    y = int((im.height - H) * ay)
    return im.crop((x, y, x + W, y + H))


def cutout(path, thr=236):
    p = Image.open(path).convert('RGB')
    a = np.asarray(p).astype(int)
    m = (a.min(axis=2) < thr).astype('uint8') * 255
    mk = Image.fromarray(m).filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(5)).filter(ImageFilter.GaussianBlur(1.2))
    bb = mk.getbbox()
    return p.crop(bb), mk.crop(bb)


def paste_shadowed(canvas, prod, mask, box):
    x, y, w, h = box
    r = min(w / prod.width, h / prod.height)
    pw, ph = int(prod.width * r), int(prod.height * r)
    pr = prod.resize((pw, ph), Image.LANCZOS)
    mr = mask.resize((pw, ph), Image.LANCZOS)
    ox, oy = x + (w - pw) // 2, y + (h - ph) // 2
    sh = mr.filter(ImageFilter.GaussianBlur(16)).point(lambda v: int(v * 0.45))
    canvas.paste((200, 195, 187), (ox + 12, oy + 18), sh)
    canvas.paste(pr, (ox, oy), mr)


def hero(src, head, sub, out, mirror=False, brand='HABBAA', ax=0.5, panel=False):
    """head: list of 1-2 lines, sub: list of 1-2 lines. Text on the RIGHT (product must be left)."""
    im = Image.open(src).convert('RGB')
    if mirror:
        im = ImageOps.mirror(im)
    h = cover(im, DW, DH, ax)
    if panel:
        g = Image.new('L', (DW, DH), 0)
        gd = ImageDraw.Draw(g)
        x0 = DW - 820
        for x in range(x0, DW):
            gd.line([(x, 0), (x, DH)], fill=int(min(1, (x - x0) / 220) * 235))
        h.paste(Image.new('RGB', (DW, DH), (248, 246, 242)), (0, 0), g)
    d = ImageDraw.Draw(h)
    xr = DW - 90
    maxw = 640
    rtext(d, xr, 120, brand, font('ExtraBold', 30), ACC)
    y = 175
    for line in head:
        f = fit(d, line, 'ExtraBold', 70, maxw)
        rtext(d, xr, y, line, f, INK)
        y += 90
    y += 25
    for line in sub:
        f = fit(d, line, 'Medium', 32, maxw)
        rtext(d, xr, y, line, f, SUB)
        y += 48
    d.rectangle((xr - 90, y + 30, xr, y + 36), fill=ACC)
    h.save(out + '-desktop.jpg', quality=92)
    # mobile: photo top (600x290) + text band
    m = Image.new('RGB', (MW, MH), BG)
    top = cover(im, MW, 290, ax * 0.6)
    m.paste(top, (0, 0))
    d = ImageDraw.Draw(m)
    y = 308
    xr = MW - 32
    t = ' '.join(head)
    f = fit(d, t, 'ExtraBold', 40, MW - 64)
    rtext(d, xr, y, t, f, INK)
    y += 60
    s = ' '.join(sub)
    words = s.split()
    lines, cur = [], ''
    fs = font('Medium', 22)
    for w in words:
        test = (cur + ' ' + w).strip()
        if tw(d, test, fs)[0] > MW - 64 and cur:
            lines.append(cur)
            cur = w
        else:
            cur = test
    lines.append(cur)
    for line in lines[:2]:
        rtext(d, xr, y, line, fs, SUB)
        y += 34
    m.save(out + '-mobile.jpg', quality=92)


def uses(tiles, title, out):
    """tiles: list of 4 (image_path, label) in reading order (first = rightmost)."""
    g = Image.new('RGB', (DW, DH), BG)
    d = ImageDraw.Draw(g)
    ctext(d, DW // 2, 40, title, fit(d, title, 'ExtraBold', 46, DW - 200), INK)
    tw_, th, gap, top = 330, 380, 24, 120
    x0 = (DW - (4 * tw_ + 3 * gap)) // 2
    for i, (p, lab) in enumerate(tiles[::-1]):
        im = cover(Image.open(p).convert('RGB'), tw_, th)
        x = x0 + i * (tw_ + gap)
        mk = Image.new('L', (tw_, th), 0)
        ImageDraw.Draw(mk).rounded_rectangle((0, 0, tw_, th), 18, fill=255)
        g.paste(im, (x, top), mk)
        ctext(d, x + tw_ // 2, top + th + 26, lab, fit(d, lab, 'Bold', 28, tw_ - 10), INK)
    g.save(out + '-desktop.jpg', quality=92)
    # mobile 2x2
    m = Image.new('RGB', (MW, MH), BG)
    d = ImageDraw.Draw(m)
    ctext(d, MW // 2, 16, title, fit(d, title, 'ExtraBold', 30, MW - 40), INK)
    s, gap, top = 180, 14, 62
    cols = [MW - 24 - s, MW - 24 - 2 * s - gap]
    # 2 rows: use wider tiles
    tw2, th2 = 270, 160
    xs = [MW - 20 - tw2, MW - 20 - 2 * tw2 - 20]
    for i, (p, lab) in enumerate(tiles):
        r, c = divmod(i, 2)
        x, y = xs[c], top + r * (th2 + 30)
        im = cover(Image.open(p).convert('RGB'), tw2, th2)
        mk = Image.new('L', (tw2, th2), 0)
        ImageDraw.Draw(mk).rounded_rectangle((0, 0, tw2, th2), 12, fill=255)
        m.paste(im, (x, y), mk)
        ctext(d, x + tw2 // 2, y + th2 + 4, lab, fit(d, lab, 'Bold', 19, tw2 - 6), INK)
    m.save(out + '-mobile.jpg', quality=92)


def _photo(canvas, path, box, rad):
    x, y, w, h = box
    im = cover(Image.open(path).convert('RGB'), w, h)
    mk = Image.new('L', (w, h), 0)
    ImageDraw.Draw(mk).rounded_rectangle((0, 0, w, h), rad, fill=255)
    canvas.paste(im, (x, y), mk)


def features(prod_path, title, feats, out, thr=236, photo=False):
    """feats: list of 3-4 (title, subtitle). photo=True: framed photo instead of cutout (white products)."""
    c = Image.new('RGB', (DW, DH), (244, 241, 236))
    if photo:
        _photo(c, prod_path, (80, 50, 620, 500), 22)
    else:
        prod, mask = cutout(prod_path, thr)
        paste_shadowed(c, prod, mask, (110, 50, 600, 500))
    d = ImageDraw.Draw(c)
    xr = DW - 80
    rtext(d, xr, 60, title, fit(d, title, 'ExtraBold', 50, 640), INK)
    y = 160 if len(feats) == 4 else 185
    for t, s in feats:
        d.ellipse((xr - 14, y + 12, xr, y + 26), fill=ACC)
        rtext(d, xr - 30, y, t, fit(d, t, 'Bold', 34, 600), INK)
        rtext(d, xr - 30, y + 46, s, fit(d, s, 'Medium', 26, 600), SUB)
        y += 100
    c.save(out + '-desktop.jpg', quality=92)
    m = Image.new('RGB', (MW, MH), (244, 241, 236))
    if photo:
        _photo(m, prod_path, (16, 80, 220, 330), 14)
    else:
        paste_shadowed(m, prod, mask, (14, 70, 230, 330))
    d = ImageDraw.Draw(m)
    xr = MW - 26
    rtext(d, xr, 22, title, fit(d, title, 'ExtraBold', 30, MW - 50), INK)
    y = 92
    for t, s in feats:
        d.ellipse((xr - 10, y + 9, xr, y + 19), fill=ACC)
        rtext(d, xr - 20, y, t, fit(d, t, 'Bold', 22, 320), INK)
        rtext(d, xr - 20, y + 30, s, fit(d, s, 'Medium', 16, 320), SUB)
        y += 82 if len(feats) == 4 else 100
    m.save(out + '-mobile.jpg', quality=92)
