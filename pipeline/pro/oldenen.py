"""EN banners for the old text-free photo families (bags, pens, caps, brooches, bottles, balloons).
usage: python3 oldenen.py  (reads en_copy/old.json: {key: [{src, head:[2], lines:[..]}]})
out: aplus/<key>EN-<n>-mod-{desktop,mobile}.jpg  (n = 1..k) and /tmp/<key>EN.jpg sheet
"""
import os, json
import numpy as np
from PIL import Image, ImageDraw
from v2en import F, W, fit, ltext, ctext, wrap, AP, INK, SUB, ACC

HERE = os.path.dirname(os.path.abspath(__file__))
BG = (247, 245, 241)


def fade_paste(canvas, photo, x0, w_fade, left=True):
    """paste photo at x0 with a horizontal fade on its left edge"""
    ph = photo.convert('RGB')
    a = np.zeros((ph.height, ph.width), np.uint8) + 255
    ramp = np.linspace(0, 255, w_fade).astype(np.uint8)
    a[:, :w_fade] = ramp[None, :]
    canvas.paste(ph, (x0, 0), Image.fromarray(a))


def desk(src, head, lines):
    im = Image.open(f'{AP}/{src}-desktop.jpg').convert('RGB').resize((1464, 600))
    cv = Image.new('RGB', (1464, 600), BG)
    crop = im.crop((230, 0, 230 + 944, 600))
    fade_paste(cv, crop, 520, 120)
    d = ImageDraw.Draw(cv)
    x = 70
    ltext(d, x, 95, 'HABBAA', F('ExtraBold', 26), ACC)
    y = 145
    for h in head:
        ltext(d, x, y, h, fit(d, h, 'ExtraBold', 50, 470), INK); y += 66
    y += 18
    for ln in lines:
        d.ellipse((x, y + 10, x + 10, y + 20), fill=ACC)
        f = fit(d, ln, 'Medium', 25, 440)
        ltext(d, x + 22, y, ln, f, SUB); y += 44
    d.rectangle((x, y + 18, x + 80, y + 23), fill=ACC)
    return cv


def mob(src, head, lines):
    p = f'{AP}/{src}-mobile.jpg'
    im = Image.open(p).convert('RGB')
    im = im.resize((600, int(im.height * 600 / im.width)))
    cv = Image.new('RGB', (600, 450), BG)
    top = max(0, (im.height - 250) // 2)
    cv.paste(im.crop((0, top, 600, top + 250)), (0, 0))
    d = ImageDraw.Draw(cv)
    t = ' '.join(head)
    ltext(d, 28, 268, t, fit(d, t, 'ExtraBold', 30, 544), INK)
    y = 316
    for ln in lines[:3]:
        d.ellipse((28, y + 7, 36, y + 15), fill=ACC)
        ltext(d, 46, y, ln, fit(d, ln, 'Medium', 19, 526), SUB); y += 34
    return cv


def main():
    C = json.load(open(f'{HERE}/en_copy/old.json'))
    for key, mods in C.items():
        sheet = Image.new('RGB', (2064, 600 * len(mods)), 'white')
        for i, m in enumerate(mods, 1):
            dd = desk(m['src'], m['head'], m['lines']); mm = mob(m['src'], m['head'], m['lines'])
            dd.save(f'{AP}/{key}EN-{i}-mod-desktop.jpg', quality=92)
            mm.save(f'{AP}/{key}EN-{i}-mod-mobile.jpg', quality=92)
            sheet.paste(dd, (0, (i - 1) * 600)); sheet.paste(mm, (1464, (i - 1) * 600))
        sheet.resize((1032, 300 * len(mods))).save(f'/tmp/{key}EN.jpg', quality=75)
        print(key, len(mods))


if __name__ == '__main__':
    main()
