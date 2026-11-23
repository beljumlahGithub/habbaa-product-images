"""Make English Pro A+ images from the approved Arabic ones: same photos/design, English text.
usage: python3 en_overlay.py <fam>  (copy in en_copy/<fam>.json) -> aplus/pro/<fam>EN-*.jpg"""
import sys, json, os, numpy as np, cv2
from PIL import Image, ImageDraw
import premlib_en as E
P = E.P; F = P.F; W, H, MW, MH = P.W, P.H, P.MW, P.MH
D = os.path.dirname(os.path.abspath(__file__)); PRO = os.path.join(D, '..', '..', 'aplus', 'pro')
rt = E._rtext; ct = E._ctext; tw = E._tw
def lt(d, x, y, t, f, fill): d.text((x, y), E._chk(t), font=f, fill=fill)
def inpaint(im, box):
    a = cv2.cvtColor(np.array(im), cv2.COLOR_RGB2BGR); m = np.zeros(a.shape[:2], np.uint8)
    x0, y0, x1, y1 = box; m[y0:y1, x0:x1] = 255
    small = cv2.resize(a, (a.shape[1] // 4, a.shape[0] // 4)); ms = cv2.resize(m, (m.shape[1] // 4, m.shape[0] // 4))
    r = cv2.inpaint(small, ms, 9, cv2.INPAINT_TELEA); r = cv2.GaussianBlur(cv2.resize(r, (a.shape[1], a.shape[0])), (31, 31), 0)
    a[m > 0] = r[m > 0]; return Image.fromarray(cv2.cvtColor(a, cv2.COLOR_BGR2RGB))
def oldpill(im, xr, y, maxw=320):
    px = im.load(); w = 0
    for x in range(xr - 4, max(0, xr - maxw), -1):
        if min(px[x, y]) > 236: w = xr - x
    return w

def hero(c, a, out):
    im = inpaint(Image.open(a + '-desktop.jpg').convert('RGB'), (620, 40, 1430, 540)); d = ImageDraw.Draw(im); xr = W - 80
    rt(d, xr, 62, 'HABBAA', F('Bold', 34), P.ACC); y = 112
    for ln in c['head']: f = P.fit(d, ln, 'ExtraBold', 86, 700); rt(d, xr, y, ln, f, P.INK); y += f.size + 14
    y += 18
    for ln in P.wrap(d, c['sub'], F('Medium', 36), 700)[:2]: rt(d, xr, y, ln, F('Medium', 36), P.SUB); y += 48
    y += 26; x = xr
    for i, ch in enumerate(list(reversed(c['chips']))[:3]): x = P.pill(d, x, y, ch, F('Bold', 30), P.WHITE if i == 0 else P.INK, P.DEEP if i == 0 else P.WHITE) - 14
    im.save(out + '-desktop.jpg', quality=93)
    m = Image.open(a + '-mobile.jpg').convert('RGB'); d = ImageDraw.Draw(m); d.rectangle((0, 252, MW, MH), fill=P.BG)
    t = ' '.join(c['head']); rt(d, MW - 28, 262, t, P.fit(d, t, 'ExtraBold', 40, MW - 56), P.INK)
    for j, ln in enumerate(P.wrap(d, c['sub'], F('Medium', 23), MW - 56)[:2]): rt(d, MW - 28, 322 + j * 32, ln, F('Medium', 23), P.SUB)
    x = MW - 28
    for i, ch in enumerate(list(reversed(c['chips']))[:3]): x = P.pill(d, x, 392, ch, F('Bold', 19), P.WHITE if i == 0 else P.INK, P.DEEP if i == 0 else P.WHITE, pad=14, h=40) - 8
    m.save(out + '-mobile.jpg', quality=93)

def feat(c, a, out):
    im = Image.open(a + '-desktop.jpg').convert('RGB'); d = ImageDraw.Draw(im); d.rectangle((470, 0, W, H), fill=P.BG); xr = W - 70
    rt(d, xr, 48, c['title'], P.fit(d, c['title'], 'ExtraBold', 60, 880), P.INK); rt(d, xr, 126, c['sub'], P.fit(d, c['sub'], 'Medium', 32, 880), P.SUB)
    fs = c['feats']; order = [fs[1], fs[0], fs[3], fs[2]]; cw, ch = 440, 170
    for i, (t, s) in enumerate(order):
        col, row = i % 2, i // 2; x2 = xr - col * (cw + 24); x1 = x2 - cw; y1 = 200 + row * (ch + 22)
        d.rounded_rectangle((x1, y1, x2, y1 + ch), 22, fill=P.WHITE); P.tick(d, x2 - 58, y1 + 52, 26)
        rt(d, x2 - 104, y1 + 26, t, P.fit(d, t, 'ExtraBold', 31, cw - 130), P.INK)
        ls = P.wrap(d, s, F('Medium', 24), cw - 130); assert len(ls) <= 2, ('feat sub too long', s)
        for j, ln in enumerate(ls): rt(d, x2 - 104, y1 + 76 + j * 34, ln, F('Medium', 24), P.SUB)
    im.save(out + '-desktop.jpg', quality=93)
    m = Image.open(a + '-mobile.jpg').convert('RGB'); d = ImageDraw.Draw(m); d.rectangle((0, 0, MW, 72), fill=P.BG); d.rectangle((222, 72, MW, MH), fill=P.BG)
    rt(d, MW - 24, 18, c['title'], P.fit(d, c['title'], 'ExtraBold', 34, MW - 48), P.INK)
    for i, (t, s) in enumerate(fs):
        y = 80 + i * 88; d.rounded_rectangle((232, y, MW - 24, y + 78), 14, fill=P.WHITE); P.tick(d, MW - 50, y + 39, 15)
        rt(d, MW - 76, y + 10, t, P.fit(d, t, 'Bold', 22, 270), P.INK); rt(d, MW - 76, y + 42, s, P.fit(d, s, 'Medium', 16, 270, mn=12), P.SUB)
    m.save(out + '-mobile.jpg', quality=93)

def steps(c, a, out):
    src = Image.open(a + '-desktop.jpg').convert('RGB'); pw, ph = 420, 330; y1 = 120
    tiles = [src.crop((W - 60 - i * (pw + 42) - pw, y1, W - 60 - i * (pw + 42), y1 + ph)) for i in range(3)]  # AR step i (rightmost=1)
    im = Image.new('RGB', (W, H), P.WHITE); d = ImageDraw.Draw(im)
    ct(d, W / 2, 30, c['title'], P.fit(d, c['title'], 'ExtraBold', 54, 1200), P.INK)
    for i, (t, s) in enumerate(c['steps'][:3]):
        x1 = 60 + i * (pw + 42); im.paste(tiles[i], (x1, y1), P.rmask((pw, ph), 24)); xr = x1 + pw
        d.ellipse((xr - 76, y1 + 16, xr - 16, y1 + 76), fill=P.DEEP); ct(d, xr - 46, y1 + 24, str(i + 1), F('ExtraBold', 38), P.WHITE)
        lt(d, x1, y1 + ph + 18, t, P.fit(d, t, 'ExtraBold', 34, pw), P.INK)
        ls = P.wrap(d, s, F('Medium', 24), pw); assert len(ls) <= 2, ('step sub too long', s)
        for j, ln in enumerate(ls): lt(d, x1, y1 + ph + 64 + j * 32, ln, F('Medium', 24), P.SUB)
        if i < 2: ax = x1 + pw + 21; ay = y1 + ph / 2; d.polygon([(ax - 8, ay - 14), (ax - 8, ay + 14), (ax + 10, ay)], fill=P.ACC)
    im.save(out + '-desktop.jpg', quality=93)
    sm = Image.open(a + '-mobile.jpg').convert('RGB'); t2, h2 = 180, 210
    tl = [sm.crop((MW - 15 - i * (t2 + 15) - t2, 70, MW - 15 - i * (t2 + 15), 70 + h2)) for i in range(3)]
    m = Image.new('RGB', (MW, MH), P.WHITE); d = ImageDraw.Draw(m); ct(d, MW / 2, 16, c['title'], P.fit(d, c['title'], 'ExtraBold', 32, MW - 40), P.INK)
    for i, (t, s) in enumerate(c['steps'][:3]):
        x1 = 15 + i * (t2 + 15); m.paste(tl[i], (x1, 70), P.rmask((t2, h2), 14)); xr = x1 + t2
        d.ellipse((xr - 44, 78, xr - 10, 112), fill=P.DEEP); ct(d, xr - 27, 81, str(i + 1), F('ExtraBold', 22), P.WHITE)
        for j, ln in enumerate(P.wrap(d, t, F('Bold', 20), t2)[:2]): lt(d, x1, 292 + j * 28, ln, F('Bold', 20), P.INK)
        for j, ln in enumerate(P.wrap(d, s, F('Medium', 15), t2)[:3]): lt(d, x1, 352 + j * 22, ln, F('Medium', 15), P.SUB)
    m.save(out + '-mobile.jpg', quality=93)

def uses(c, a, out):
    im = Image.open(a + '-desktop.jpg').convert('RGB'); d = ImageDraw.Draw(im); d.rectangle((0, 0, W, 172), fill=P.BG); d.rectangle((0, 512, W, H), fill=P.BG)
    rt(d, W - 70, 36, c['title'], P.fit(d, c['title'], 'ExtraBold', 54, 1300), P.INK); rt(d, W - 70, 108, c['sub'], P.fit(d, c['sub'], 'Medium', 30, 1300), P.SUB)
    tw_, th = 316, 330; y1 = 176
    for i, lab in enumerate(c['tiles'][:4]):  # tiles listed in AR order (rightmost first)
        xr = W - 70 - i * (tw_ + 26); ow = oldpill(im, xr - 16, y1 + th - 43)
        fl = P.fit(d, lab, 'Bold', 30, tw_ - 70); bw = max(tw(d, lab, fl)[0] + 40, ow + 2)
        d.rounded_rectangle((xr - 16 - bw, y1 + th - 70, xr - 16, y1 + th - 16), 27, fill=P.WHITE); rt(d, xr - 36, y1 + th - 63, lab, fl, P.INK)
    if c.get('note'): rt(d, W - 70, 532, c['note'], P.fit(d, c['note'], 'Medium', 26, 1300), P.SUB)
    im.save(out + '-desktop.jpg', quality=93)
    m = Image.open(a + '-mobile.jpg').convert('RGB'); d = ImageDraw.Draw(m); d.rectangle((0, 0, MW, 66), fill=P.BG)
    rt(d, MW - 24, 16, c['title'], P.fit(d, c['title'], 'ExtraBold', 32, MW - 48), P.INK); t2, h2 = 270, 172
    for i, lab in enumerate(c['tiles'][:4]):
        col, row = i % 2, i // 2; xr = MW - 20 - col * (t2 + 20); y1 = 70 + row * (h2 + 14); ow = oldpill(m, xr - 10, y1 + h2 - 26, 250)
        fl = P.fit(d, lab, 'Bold', 19, t2 - 40); bw = max(tw(d, lab, fl)[0] + 24, ow + 2)
        d.rounded_rectangle((xr - 10 - bw, y1 + h2 - 42, xr - 10, y1 + h2 - 10), 16, fill=P.WHITE); rt(d, xr - 22, y1 + h2 - 39, lab, fl, P.INK)
    m.save(out + '-mobile.jpg', quality=93)

def specs(c, a, out):
    im = Image.open(a + '-desktop.jpg').convert('RGB'); d = ImageDraw.Draw(im); d.rectangle((640, 0, W, H), fill=P.DEEP)
    x0 = 700; xr = W - 80; rows = c['rows'][:6]; lt(d, x0, 52, 'Specifications', F('ExtraBold', 58), P.WHITE); step = 66 if len(rows) >= 6 else 74
    for i, (k, v) in enumerate(rows):
        y = 150 + i * step; lt(d, x0, y, k, F('Bold', 32), P.GOLDT); rt(d, xr, y, v, P.fit(d, v, 'Medium', 32, 470), P.WHITE)
        if i < len(rows) - 1: d.line((x0, y + step - 12, xr, y + step - 12), fill=(70, 88, 96), width=2)
    im.save(out + '-desktop.jpg', quality=93)
    m = Image.new('RGB', (MW, MH), P.DEEP); d = ImageDraw.Draw(m); lt(d, 28, 20, 'Specifications', F('ExtraBold', 36), P.WHITE); st = 58 if len(rows) >= 6 else 64
    for i, (k, v) in enumerate(rows):
        y = 86 + i * st; lt(d, 28, y, k, F('Bold', 22), P.GOLDT); rt(d, MW - 28, y, v, P.fit(d, v, 'Medium', 22, 330), P.WHITE)
        if i < len(rows) - 1: d.line((28, y + st - 12, MW - 28, y + st - 12), fill=(70, 88, 96), width=1)
    m.save(out + '-mobile.jpg', quality=93)

MODS = [('1-hero', hero), ('2-feat', feat), ('3-steps', steps), ('4-uses', uses), ('5-specs', specs)]
def run(fam):
    c = json.load(open(os.path.join(D, 'en_copy', fam + '.json'))); outs = []
    for tag, fn in MODS:
        a = os.path.join(PRO, f'{fam}-{tag}'); o = os.path.join(PRO, f'{fam}EN-{tag}')
        if os.path.exists(a + '-desktop.jpg'): fn(c[tag.split('-')[1]], a, o); outs.append(o)
    P.sheet(outs, f'/tmp/{fam}EN.jpg'); return outs
if __name__ == '__main__':
    for f in sys.argv[1:]: print(f, len(run(f)))
