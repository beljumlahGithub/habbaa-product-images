import json, os, re, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
src = open('/home/claude/img4/gen.py').read().split("os.makedirs('out'")[0]
src = src.replace("C = json.load(open('/home/claude/seo/content.json'))", "C = {}")
src = src.replace("low = json.load(open('low.json'))  # asin -> [count, main_id]", "")
exec(src)
D = json.load(open('data.json'))
for s, v in D.items(): C[s] = {'ar': {'t': v['t'], 'b': v['b']}}
AR.update(D.keys())
SC = {'Cups': '/home/claude/aplus4/gen/mugs-t0.png', 'DrawstringBags': 'gym', 'Notebooks': 'desk', 'BadgeReels': 'conf',
      'Brooches': 'brooch', 'Bottles': 'park', 'Pens': 'desk', 'Caps': 'field', 'Balloons': 'balloon'}
def scene(s):
    f = D[s]['f']; k = next(x for x in SC if x in f); p = SC[k]
    if not p.startswith('/'): p = f'/home/claude/img7/scene/{p}.png'
    return Image.open(p).convert('RGB')
def cover(im, S_):
    r = max(S_/im.width, S_/im.height); im = im.resize((int(im.width*r)+1, int(im.height*r)+1), Image.LANCZOS)
    x = (im.width-S_)//2; y = (im.height-S_)//2; return im.crop((x, y, x+S_, y+S_))
KW = dict(direction='rtl', language='ar')
def ctext(d, y, s, f, fill):
    tw = d.textlength(s, font=f, **KW); d.text(((S-tw)/2, y), s, font=f, fill=fill, **KW)
def lifestyle(a, im, out):
    bg = cover(scene(a), S).filter(ImageFilter.GaussianBlur(5)); c = bg.copy(); d = ImageDraw.Draw(c, 'RGBA')
    d.rectangle((0, 0, S, 300), fill=(255, 255, 255, 225)); header(d, 'في الاستخدام اليومي', True)
    d.rounded_rectangle((260, 420, S-260, 1640), 50, fill=(255, 255, 255, 245)); place(c, im, (320, 480, S-640, 1100))
    h, r = split(C[a]['ar']['b'][min(3, len(C[a]['ar']['b'])-1)])
    d.rounded_rectangle((120, 1700, S-120, 1930), 40, fill=(255, 255, 255, 235))
    y = 1730
    for line in wrap(d, h or r, F('Bold', 60), S-320, True)[:1]: txt(d, (0, y), line, F('Bold', 60), INK, True, S-170); y += 76
    for line in wrap(d, r, F('Medium', 44), S-320, True)[:2]: txt(d, (0, y), line, F('Medium', 44), SUB, True, S-170); y += 54
    c.save(out, quality=92)
MR = re.compile(r'(\d+(?:\.\d+)?\s*[×xX\*]\s*\d+(?:\.\d+)?(?:\s*[×xX\*]\s*\d+(?:\.\d+)?)?\s*(?:سم|مم)|\d+(?:\.\d+)?\s*(?:سم|مم|مل|جرام|ورقة)(?=[\s،,.]|$)|A[456])')
def dims(a):
    seen = []
    for s in [C[a]['ar']['t']] + C[a]['ar']['b']:
        for m in MR.findall(s):
            k = re.sub(r'\s+', ' ', m).replace('*', '×').replace('x', '×')
            if k not in seen: seen.append(k)
    return seen[:4]
def size(a, im, out):
    ds = dims(a); c = Image.new('RGB', (S, S), BG); d = ImageDraw.Draw(c)
    header(d, 'المقاس والمواصفات', True); d.rounded_rectangle((120, 340, S-120, 1400), 40, fill=PANEL)
    box_ = (260, 420, S-520, 900); r = min(box_[2]/im.width, box_[3]/im.height); w, h = int(im.width*r), int(im.height*r)
    x0 = box_[0]+(box_[2]-w)//2; y0 = box_[1]+(box_[3]-h)//2; c.paste(im.resize((w, h), Image.LANCZOS), (x0, y0))
    d.line((x0, y0+h+40, x0+w, y0+h+40), fill=ACC, width=6)
    for xx in (x0, x0+w): d.line((xx, y0+h+20, xx, y0+h+60), fill=ACC, width=6)
    d.line((x0-40, y0, x0-40, y0+h), fill=ACC, width=6)
    for yy in (y0, y0+h): d.line((x0-60, yy, x0-20, yy), fill=ACC, width=6)
    n = len(ds); cw = (S-240-(n-1)*40)//max(n, 1); y = 1470
    for i, v in enumerate(ds):
        xA = S-120-(i+1)*cw-i*40
        d.rounded_rectangle((xA, y, xA+cw, y+230), 30, outline=ACC, width=5)
        f = F('ExtraBold', 86 if len(v) < 9 else 64 if len(v) < 14 else 50)
        tw = d.textlength(v, font=f, **KW); d.text((xA+(cw-tw)/2, y+65), v, font=f, fill=INK, **KW)
    txt(d, (0, 1780), 'المقاسات كما هي مذكورة في وصف المنتج', F('Medium', 40), SUB, True, S-140)
    c.save(out, quality=92)
def box(a, im, out):
    c = Image.new('RGB', (S, S), BG); d = ImageDraw.Draw(c); header(d, 'محتويات العبوة', True)
    d.rounded_rectangle((120, 340, S-120, 1500), 40, fill=PANEL); place(c, im, (220, 420, S-440, 1000))
    allb = ' '.join(C[a]['ar']['b']); m = re.search(r'محتوى العبوة\s*:\s*([^.\n]+)', allb)
    y = 1560
    if m:
        q = m.group(1).strip(); f = F('ExtraBold', 80)
        tw = d.textlength(q, font=f, **KW)
        if tw > S-400: f = F('ExtraBold', 60); tw = d.textlength(q, font=f, **KW)
        d.rounded_rectangle(((S-tw)/2-60, y, (S+tw)/2+60, y+150), 75, fill=ACC)
        d.text(((S-tw)/2, y+25), q, font=f, fill=(255, 255, 255), **KW); y += 200
    t = re.sub(r'^HABBAA\s*', '', C[a]['ar']['t']).split('،')[0]
    for line in wrap(d, t, F('Bold', 58), S-280, True)[:2]: ctext(d, y, line, F('Bold', 58), INK); y += 74
    c.save(out, quality=92)
def brand(a, im, out):
    c = Image.new('RGB', (S, S), (250, 247, 242)); d = ImageDraw.Draw(c)
    f = F('ExtraBold', 170); tw = d.textlength('HABBAA', font=f); d.text(((S-tw)/2, 150), 'HABBAA', font=f, fill=INK)
    d.rectangle((S/2-120, 380, S/2+120, 388), fill=ACC); ctext(d, 430, 'منتجات عملية لحياتك اليومية', F('Medium', 64), SUB)
    d.rounded_rectangle((420, 600, S-420, 1360), 50, fill=(255, 255, 255)); place(c, im, (480, 650, S-960, 660))
    y = 1450
    for p in ['وصف واضح وصادق للمنتج', 'تغليف مرتب وآمن', 'خدمة عملاء عبر رسائل أمازون']:
        f3 = F('Bold', 56); tw = d.textlength(p, font=f3, **KW)
        d.rounded_rectangle(((S-tw)/2-60, y, (S+tw)/2+60, y+120), 60, outline=ACC, width=4)
        d.text(((S-tw)/2, y+28), p, font=f3, fill=INK, **KW); y += 160
    c.save(out, quality=92)
if __name__ == '__main__':
    os.makedirs('out', exist_ok=True); plan = {}
    for s in (sys.argv[1:] or list(D)):
        im = prod(D[s]['local'])
        fns = [lifestyle] + ([size] if dims(s) else []) + [box, brand, features, uses, details]
        files = []
        for fn in fns[:6]:
            o = f'out/{s}-{fn.__name__}.jpg'; fn(s, im, o); files.append(o)
        plan[s] = files
    json.dump(plan, open('plan8.json', 'w'), indent=0)
    print(sum(len(x) for x in plan.values()), 'imgs', len(plan))
