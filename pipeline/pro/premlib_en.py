"""English (LTR) variant of the HABBAA Pro A+ template. Pass lists in RTL order for chips/feats/tiles:
chips reversed, feats [B,A,D,C], tiles reversed (see en_conv in README)."""
import os, re
os.environ.setdefault('HB_FONTS', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fonts') + '/')
from PIL import Image, ImageDraw
import premlib as P
P.FD = os.environ['HB_FONTS']

def _tw(d, t, f):
    b = d.textbbox((0, 0), t, font=f); return b[2] - b[0], b
def _chk(t):
    assert not re.search(r'[؀-ۿ]', t), ('arabic in EN', t); return t
def _rtext(d, xr, y, t, f, fill):
    _chk(t); w, b = _tw(d, t, f); d.text((xr - w - b[0], y), t, font=f, fill=fill); return w
def _ctext(d, xc, y, t, f, fill):
    _chk(t); w, b = _tw(d, t, f); d.text((xc - w / 2 - b[0], y), t, font=f, fill=fill); return w
P.tw = _tw; P.rtext = _rtext; P.ctext = _ctext

def specs(c, out):
    W, H, MW, MH = P.W, P.H, P.MW, P.MH; F = P.F
    im = Image.new('RGB', (W, H), P.DEEP); d = ImageDraw.Draw(im)
    rt = P.cover(Image.open(c['img']), 640, H, c.get('ax', 0.1), c.get('ay', 0.5)); im.paste(rt, (0, 0), P.hmask(640, H, 420, 640, rev=True))
    x0 = 700; xr = W - 80; rows = c['rows'][:6]
    d.text((x0, 52), _chk(c.get('title', 'Specifications')), font=F('ExtraBold', 58), fill=P.WHITE)
    step = 66 if len(rows) >= 6 else 74
    for i, (k, v) in enumerate(rows):
        y = 150 + i * step
        d.text((x0, y), _chk(k), font=F('Bold', 32), fill=P.GOLDT)
        _rtext(d, xr, y, v, P.fit(d, v, 'Medium', 32, 470), P.WHITE)
        if i < len(rows) - 1: d.line((x0, y + step - 12, xr, y + step - 12), fill=(70, 88, 96), width=2)
    im.save(out + '-desktop.jpg', quality=93)
    m = Image.new('RGB', (MW, MH), P.DEEP); d = ImageDraw.Draw(m)
    d.text((28, 20), c.get('title', 'Specifications'), font=F('ExtraBold', 36), fill=P.WHITE)
    st = 58 if len(rows) >= 6 else 64
    for i, (k, v) in enumerate(rows):
        y = 86 + i * st
        d.text((28, y), k, font=F('Bold', 22), fill=P.GOLDT)
        _rtext(d, MW - 28, y, v, P.fit(d, v, 'Medium', 22, 330), P.WHITE)
        if i < len(rows) - 1: d.line((28, y + st - 12, MW - 28, y + st - 12), fill=(70, 88, 96), width=1)
    m.save(out + '-mobile.jpg', quality=93)

def steps(c, out):
    W, H, MW, MH = P.W, P.H, P.MW, P.MH; F = P.F; fit = P.fit
    im = Image.new('RGB', (W, H), P.WHITE); d = ImageDraw.Draw(im)
    _ctext(d, W / 2, 30, c['title'], fit(d, c['title'], 'ExtraBold', 54, 1200), P.INK)
    pw, ph = 420, 330
    for i, (f, t, s) in enumerate(c['steps'][:3]):
        x1 = 60 + i * (pw + 42); y1 = 120
        p = P.cover(Image.open(f), pw, ph); im.paste(p, (x1, y1), P.rmask(p.size, 24))
        d.ellipse((x1 + 16, y1 + 16, x1 + 76, y1 + 76), fill=P.DEEP); _ctext(d, x1 + 46, y1 + 24, str(i + 1), F('ExtraBold', 38), P.WHITE)
        d.text((x1, y1 + ph + 18), _chk(t), font=fit(d, t, 'ExtraBold', 34, pw), fill=P.INK)
        ls = P.wrap(d, s, F('Medium', 24), pw); assert len(ls) <= 2, ('step sub too long', s)
        for j, ln in enumerate(ls): d.text((x1, y1 + ph + 64 + j * 32), ln, font=F('Medium', 24), fill=P.SUB)
        if i < 2:
            ax = x1 + pw + 21; ay = y1 + ph / 2; d.polygon([(ax - 8, ay - 14), (ax - 8, ay + 14), (ax + 10, ay)], fill=P.ACC)
    im.save(out + '-desktop.jpg', quality=93)
    m = Image.new('RGB', (MW, MH), P.WHITE); d = ImageDraw.Draw(m)
    _ctext(d, MW / 2, 16, c['title'], fit(d, c['title'], 'ExtraBold', 32, MW - 40), P.INK)
    tw_, th_ = 180, 210
    for i, (f, t, s) in enumerate(c['steps'][:3]):
        x1 = 15 + i * (tw_ + 15)
        p = P.cover(Image.open(f), tw_, th_); m.paste(p, (x1, 70), P.rmask(p.size, 14))
        d.ellipse((x1 + 10, 78, x1 + 44, 112), fill=P.DEEP); _ctext(d, x1 + 27, 81, str(i + 1), F('ExtraBold', 22), P.WHITE)
        for j, ln in enumerate(P.wrap(d, t, F('Bold', 20), tw_)[:2]): d.text((x1, 292 + j * 28), ln, font=F('Bold', 20), fill=P.INK)
        for j, ln in enumerate(P.wrap(d, s, F('Medium', 15), tw_)[:3]): d.text((x1, 352 + j * 22), ln, font=F('Medium', 15), fill=P.SUB)
    m.save(out + '-mobile.jpg', quality=93)
P.specs = specs; P.steps = steps
build = P.build; sheet = P.sheet
