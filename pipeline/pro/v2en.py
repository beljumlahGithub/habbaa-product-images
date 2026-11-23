"""English overlay for AR v2 A+ (aplus/dN-<fam>-{1-hero,2-uses,3-feat}-{desktop,mobile}.jpg).
usage: python3 v2en.py dN-fam   (copy in en_copy/v2/<dN-fam>.json)
json: hero{head[1-2],sub[1-2]}, uses{title,labels[4] AR order (first=rightmost)},
      feat{type:'grid',title,labels[4]} | feat{type:'list',title,feats[[t,s]x3-4]}
out: aplus/<dN-fam>EN-<n>-<mod>-{desktop,mobile}.jpg + /tmp/<key>EN.jpg sheet
"""
import os, sys, json
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
AP = os.path.join(ROOT, 'aplus')
FD = os.environ.get('HB_FONTS', os.path.join(ROOT, 'pipeline', 'fonts'))
INK = (38, 41, 46); SUB = (92, 96, 102); ACC = (176, 141, 87)


def F(w, s):
    return ImageFont.truetype(os.path.join(FD, f'Tajawal-{w}.ttf'), s)


def W(d, t, f):
    b = d.textbbox((0, 0), t, font=f); return b[2] - b[0], b


def fit(d, t, w, s, mx):
    while s > 12:
        f = F(w, s)
        if W(d, t, f)[0] <= mx: return f
        s -= 1
    return F(w, s)


def ltext(d, x, y, t, f, c):
    w, b = W(d, t, f); d.text((x - b[0], y - b[1]), t, font=f, fill=c); return w


def ctext(d, xc, y, t, f, c):
    w, b = W(d, t, f); d.text((xc - w / 2 - b[0], y - b[1]), t, font=f, fill=c); return w


def wrap(d, t, f, mx):
    out, cur = [], ''
    for w in t.split():
        s = (cur + ' ' + w).strip()
        if W(d, s, f)[0] > mx and cur: out.append(cur); cur = w
        else: cur = s
    out.append(cur); return out


def bgcol(a, pts):
    return tuple(int(v) for v in np.median(np.array([a[y, x] for x, y in pts]), axis=0))


def inpaint_text(im, box):
    a = np.asarray(im).copy()
    x0, y0, x1, y1 = box
    reg = a[y0:y1, x0:x1]
    g = cv2.cvtColor(reg, cv2.COLOR_RGB2GRAY).astype(int)
    bl = cv2.medianBlur(cv2.cvtColor(reg, cv2.COLOR_RGB2GRAY), 41).astype(int)
    m = (np.abs(g - bl) > 12).astype('uint8') * 255
    m = cv2.dilate(m, np.ones((13, 13), np.uint8))
    full = np.zeros(a.shape[:2], np.uint8); full[y0:y1, x0:x1] = m
    r = cv2.inpaint(cv2.cvtColor(a, cv2.COLOR_RGB2BGR), full, 11, cv2.INPAINT_TELEA)
    r = cv2.cvtColor(r, cv2.COLOR_BGR2RGB)
    # soften: blur the patched area slightly
    bl2 = cv2.GaussianBlur(r, (0, 0), 6)
    mm = cv2.GaussianBlur(full, (0, 0), 6)[..., None] / 255.0
    r = (r * (1 - mm) + bl2 * mm).astype('uint8')
    return Image.fromarray(r)


def hero(key, c):
    im = Image.open(f'{AP}/{key}-1-hero-desktop.jpg').convert('RGB')
    a0 = np.asarray(im).astype(int)
    strip = a0[:, 1440:1464].reshape(-1, 3)
    if strip.std(axis=0).max() < 4 and np.abs(strip.mean(axis=0) - np.array([247, 245, 241])).max() < 6:
        ImageDraw.Draw(im).rectangle((700, 0, 1464, 600), fill=(247, 245, 241))
    else:
        im = inpaint_text(im, (600, 55, 1420, 575))
    d = ImageDraw.Draw(im)
    x0, mx = 770, 610
    ltext(d, x0, 120, 'HABBAA', F('ExtraBold', 30), ACC)
    y = 175
    for ln in c['head']:
        ltext(d, x0, y, ln, fit(d, ln, 'ExtraBold', 68, mx), INK); y += 88
    y += 25
    for ln in c['sub']:
        ltext(d, x0, y, ln, fit(d, ln, 'Medium', 31, mx), SUB); y += 46
    d.rectangle((x0, y + 30, x0 + 90, y + 36), fill=ACC)
    im.save(f'{AP}/{key}EN-1-hero-desktop.jpg', quality=92)
    m = Image.open(f'{AP}/{key}-1-hero-mobile.jpg').convert('RGB')
    a = np.asarray(m)
    bg = bgcol(a, [(5, 445), (595, 445), (300, 445)])
    d = ImageDraw.Draw(m)
    d.rectangle((0, 292, 600, 450), fill=bg)
    t = ' '.join(c['head'])
    ltext(d, 32, 308, t, fit(d, t, 'ExtraBold', 36, 536), INK)
    fs = F('Medium', 21); y = 366
    for ln in wrap(d, ' '.join(c['sub']), fs, 536)[:2]:
        ltext(d, 32, y, ln, fs, SUB); y += 32
    m.save(f'{AP}/{key}EN-1-hero-mobile.jpg', quality=92)


def bands(a, bg, tol=14):
    diff = np.abs(a.astype(int) - np.array(bg)).max(axis=2) > tol
    fr = diff.mean(axis=1)
    cls = np.where(fr > 0.28, 2, np.where(fr > 0.002, 1, 0))
    segs, s = [], 0
    for y in range(1, len(cls) + 1):
        if y == len(cls) or cls[y] != cls[s]:
            segs.append((cls[s], s, y)); s = y
    return segs, diff


def cols(diff, y0, y1):
    fc = diff[y0:y1].mean(axis=0) > 0.5
    out, s = [], None
    for x, v in enumerate(list(fc) + [False]):
        if v and s is None: s = x
        if not v and s is not None:
            if x - s > 40: out.append((s, x))
            s = None
    return out


def grid(key, n, mod, title, labels, mobile):
    p = f'{AP}/{key}-{n}-{mod}-{"mobile" if mobile else "desktop"}.jpg'
    im = Image.open(p).convert('RGB'); a = np.asarray(im)
    bg = bgcol(a, [(3, 3), (a.shape[1] - 4, 3), (3, a.shape[0] - 4), (a.shape[1] - 4, a.shape[0] - 4), (a.shape[1] // 2, 8)])
    d = ImageDraw.Draw(im)
    if not mobile:
        d.rectangle((0, 18, 1464, 112), fill=bg)
        ctext(d, 732, 42, title, fit(d, title, 'ExtraBold', 46, 1264), INK)
        d.rectangle((0, 503, 1464, 598), fill=bg)
        for i, lab in enumerate(labels[::-1]):
            x = 36 + i * 354
            ctext(d, x + 165, 530, lab, fit(d, lab, 'Bold', 28, 320), INK)
    else:
        d.rectangle((0, 4, 600, 58), fill=bg)
        ctext(d, 300, 18, title, fit(d, title, 'ExtraBold', 30, 560), INK)
        for r in range(2):
            y = 62 + r * 190 + 160
            d.rectangle((0, y + 1, 600, y + 29 if r == 0 else 449), fill=bg)
            for cc, x in enumerate([310, 20]):
                lab = labels[r * 2 + cc]
                ctext(d, x + 135, y + 6, lab, fit(d, lab, 'Bold', 19, 262), INK)
    im.save(f'{AP}/{key}EN-{n}-{mod}-{"mobile" if mobile else "desktop"}.jpg', quality=92)


def flist(key, c):
    for mob in (False, True):
        p = f'{AP}/{key}-3-feat-{"mobile" if mob else "desktop"}.jpg'
        im = Image.open(p).convert('RGB'); a = np.asarray(im)
        Wd = a.shape[1]
        bg = bgcol(a, [(Wd - 4, 3), (Wd - 4, a.shape[0] - 4), (Wd // 2 + 60, 3)])
        d = ImageDraw.Draw(im)
        if not mob:
            x = 745; d.rectangle((x, 0, Wd, 600), fill=bg)
            ltext(d, x + 20, 60, c['title'], fit(d, c['title'], 'ExtraBold', 48, 660), INK)
            y = 160 if len(c['feats']) == 4 else 185
            for t, s in c['feats']:
                d.ellipse((x + 20, y + 12, x + 34, y + 26), fill=ACC)
                ltext(d, x + 50, y, t, fit(d, t, 'Bold', 33, 610), INK)
                ltext(d, x + 50, y + 46, s, fit(d, s, 'Medium', 25, 610), SUB)
                y += 100
        else:
            x = 250; d.rectangle((x, 0, Wd, 450), fill=bg)
            d.rectangle((0, 0, Wd, 62), fill=bg)
            ctext(d, Wd // 2, 22, c['title'], fit(d, c['title'], 'ExtraBold', 28, Wd - 40), INK)
            y = 92
            for t, s in c['feats']:
                d.ellipse((x + 6, y + 9, x + 16, y + 19), fill=ACC)
                ltext(d, x + 24, y, t, fit(d, t, 'Bold', 21, 320), INK)
                ltext(d, x + 24, y + 30, s, fit(d, s, 'Medium', 15, 320), SUB)
                y += 82 if len(c['feats']) == 4 else 100
        im.save(f'{AP}/{key}EN-3-feat-{"mobile" if mob else "desktop"}.jpg', quality=92)


def main(key):
    c = json.load(open(f'{HERE}/en_copy/v2/{key}.json'))
    hero(key, c['hero'])
    for mob in (False, True):
        grid(key, 2, 'uses', c['uses']['title'], c['uses']['labels'], mob)
    if c['feat']['type'] == 'grid':
        for mob in (False, True):
            grid(key, 3, 'feat', c['feat']['title'], c['feat']['labels'], mob)
    else:
        flist(key, c['feat'])
    ims = []
    for n, mod in ((1, 'hero'), (2, 'uses'), (3, 'feat')):
        ims.append((Image.open(f'{AP}/{key}EN-{n}-{mod}-desktop.jpg'), Image.open(f'{AP}/{key}EN-{n}-{mod}-mobile.jpg')))
    sh = Image.new('RGB', (2064, 1800), 'white')
    for i, (dd, mm) in enumerate(ims):
        sh.paste(dd, (0, i * 600)); sh.paste(mm, (1464, i * 600))
    sh.resize((1032, 900)).save(f'/tmp/{key}EN.jpg', quality=80)
    print(key, 'ok')


if __name__ == '__main__':
    for k in sys.argv[1:]: main(k)
