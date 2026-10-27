import json, os, re, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
src = open('/home/claude/img4/gen.py').read().split("os.makedirs('out'")[0]
src = src.replace("low = json.load(open('low.json'))  # asin -> [count, main_id]", "")
exec(src)
L = json.load(open('low.json'))
_prod = prod
def prod(path):
    im = _prod(path); a_ = np.asarray(im).copy(); m = a_.min(axis=2) >= 238; a_[m] = 255
    if m.mean() < 0.02:  # photo background: keep as is
        return im
    return Image.fromarray(a_)
F3 = json.load(open('/home/claude/aplus4/asins3.json'))
FAM = {a: f for f, v in F3.items() for a in v}
for a in L:
    t = C[a]['en']['t']
    if a in FAM: continue
    if 'Shoe Horn' in t: FAM[a] = 'shoe'
    elif 'Spoon' in t: FAM[a] = 'spoon'
    elif 'Ramadan' in t: FAM[a] = 'ramadan'
    elif 'Fans' in t: FAM[a] = 'fan'
    elif 'Candle' in t: FAM[a] = 'candle'
    elif 'Brooch' in t: FAM[a] = 'brooch'
    elif 'Balloon' in t: FAM[a] = 'balloon'
    elif 'Cups' in t: FAM[a] = 'dispo'
def scene(f):
    p = f'scene/{f}.png'
    if os.path.exists(p): return Image.open(p).convert('RGB')
    return Image.open(f'/home/claude/aplus4/gen/{f}-t0.png').convert('RGB')

def short(a, L_):
    t = C[a][L_]['t']; t = re.sub(r'^(HABBAA|هبة HABBAA)\s*', '', t)
    return t.split(',')[0].strip()

def cover(im, S_):
    r = max(S_/im.width, S_/im.height); im = im.resize((int(im.width*r)+1, int(im.height*r)+1), Image.LANCZOS)
    x = (im.width-S_)//2; y = (im.height-S_)//2; return im.crop((x, y, x+S_, y+S_))

def lifestyle(a, im, out):
    rtl = a in AR; L_ = 'ar' if rtl else 'en'
    bg = cover(scene(FAM[a]), S).filter(ImageFilter.GaussianBlur(5))
    c = bg.copy(); d = ImageDraw.Draw(c, 'RGBA')
    d.rectangle((0, 0, S, 300), fill=(255, 255, 255, 225))
    header(d, 'في الاستخدام اليومي' if rtl else 'EVERYDAY USE', rtl)
    # product card
    d.rounded_rectangle((260, 420, S-260, 1640), 50, fill=(255, 255, 255, 245))
    place(c, im, (320, 480, S-640, 1100))
    # caption: bullet 4 header + text
    h, r = split(C[a][L_]['b'][3])
    d.rounded_rectangle((120, 1700, S-120, 1930), 40, fill=(255, 255, 255, 235))
    f = F('Bold', 60); y = 1730
    for line in wrap(d, (h.title() if not rtl else h) or r, f, S-320, rtl)[:1]:
        txt(d, (170, y), line, f, INK, rtl, S-170); y += 76
    for line in wrap(d, r, F('Medium', 44), S-320, rtl)[:2]:
        txt(d, (170, y), line, F('Medium', 44), SUB, rtl, S-170); y += 54
    c.save(out, quality=92)

MR = re.compile(r'(\d+(?:\.\d+)?\s*[xX×]\s*\d+(?:\.\d+)?(?:\s*[xX×]\s*\d+(?:\.\d+)?)?\s*(?:mm|cm|m|inch)\b|\d+(?:\.\d+)?\s*(?:mm|cm|ml|ML|oz|Inch|inch|m|GSM)\b)')
def dims(a):
    e = C[a]['en']; seen = []; 
    for s in [e['t']] + e['b']:
        for m in MR.findall(s):
            k = re.sub(r'\s+', ' ', m).replace('ML', 'ml').replace('Inch', 'inch')
            if k.lower() not in [x.lower() for x in seen]: seen.append(k)
    return seen[:4]

def size(a, im, out):
    rtl = a in AR; ds = dims(a)
    c = Image.new('RGB', (S, S), BG); d = ImageDraw.Draw(c)
    header(d, 'المقاس والمواصفات' if rtl else 'SIZE & SPECS', rtl)
    d.rounded_rectangle((120, 340, S-120, 1400), 40, fill=PANEL)
    box = (260, 420, S-520, 900)
    r = min(box[2]/im.width, box[3]/im.height); w, h = int(im.width*r), int(im.height*r)
    x0 = box[0]+(box[2]-w)//2; y0 = box[1]+(box[3]-h)//2
    c.paste(im.resize((w, h), Image.LANCZOS), (x0, y0))
    # guide lines (no numbers on them: numbers listed below exactly as stated)
    d.line((x0, y0+h+40, x0+w, y0+h+40), fill=ACC, width=6)
    for xx in (x0, x0+w): d.line((xx, y0+h+20, xx, y0+h+60), fill=ACC, width=6)
    d.line((x0-40, y0, x0-40, y0+h), fill=ACC, width=6)
    for yy in (y0, y0+h): d.line((x0-60, yy, x0-20, yy), fill=ACC, width=6)
    n = len(ds); cw = (S-240-(n-1)*40)//max(n, 1); y = 1470
    for i, v in enumerate(ds):
        xA = 120 + i*(cw+40)
        d.rounded_rectangle((xA, y, xA+cw, y+230), 30, outline=ACC, width=5)
        f = F('ExtraBold', 86 if len(v) < 9 else 64 if len(v) < 14 else 50)
        tw = d.textlength(v, font=f); d.text((xA+(cw-tw)/2, y+65), v, font=f, fill=INK)
    note = 'المقاسات كما هي مذكورة في وصف المنتج' if rtl else 'Measurements as stated in the product details'
    f = F('Medium', 40)
    if rtl: txt(d, (0, 1780), note, f, SUB, True, S-140)
    else: d.text((140, 1780), note, font=f, fill=SUB)
    c.save(out, quality=92)

QR = re.compile(r'(Pack of \d+|\d+\s*(?:Pcs|Pieces|Sheets|Pairs|Pack|Count|Rolls|Bags))', re.I)
def box(a, im, out):
    rtl = a in AR; L_ = 'ar' if rtl else 'en'
    q = QR.findall(C[a]['en']['t'])
    c = Image.new('RGB', (S, S), BG); d = ImageDraw.Draw(c)
    header(d, 'محتويات العبوة' if rtl else "WHAT'S IN THE BOX", rtl)
    d.rounded_rectangle((120, 340, S-120, 1500), 40, fill=PANEL)
    place(c, im, (220, 420, S-440, 1000))
    if q:
        b = q[0].upper()
        f = F('ExtraBold', 90); tw = d.textlength(b, font=f)
        d.rounded_rectangle(((S-tw)/2-60, 1560, (S+tw)/2+60, 1720), 80, fill=ACC)
        d.text(((S-tw)/2, 1585), b, font=f, fill=(255, 255, 255))
        y = 1770
    else: y = 1580
    f = F('Bold', 60)
    for line in wrap(d, short(a, L_), f, S-280, rtl)[:2]:
        tw = d.textlength(line, font=f, **(dict(direction='rtl', language='ar') if rtl else {}))
        d.text(((S-tw)/2, y), line, font=f, fill=INK, **(dict(direction='rtl', language='ar') if rtl else {})); y += 76
    c.save(out, quality=92)

def brand(a, im, out):
    rtl = a in AR
    c = Image.new('RGB', (S, S), (250, 247, 242)); d = ImageDraw.Draw(c)
    f = F('ExtraBold', 170); t = 'HABBAA'; tw = d.textlength(t, font=f)
    d.text(((S-tw)/2, 150), t, font=f, fill=INK)
    d.rectangle((S/2-120, 380, S/2+120, 388), fill=ACC)
    sub = 'منتجات عملية لحياتك اليومية' if rtl else 'Practical essentials for everyday life'
    kw = dict(direction='rtl', language='ar') if rtl else {}
    f2 = F('Medium', 64); tw = d.textlength(sub, font=f2, **kw); d.text(((S-tw)/2, 430), sub, font=f2, fill=SUB, **kw)
    d.rounded_rectangle((420, 600, S-420, 1360), 50, fill=(255, 255, 255))
    place(c, im, (480, 650, S-960, 660))
    pills = (['وصف واضح وصادق للمنتج', 'تغليف مرتب وآمن', 'خدمة عملاء عبر رسائل أمازون'] if rtl else
             ['Clear, honest product details', 'Neat, protective packing', 'Support via Amazon buyer messages'])
    y = 1450; f3 = F('Bold', 56)
    for p in pills:
        tw = d.textlength(p, font=f3, **kw)
        d.rounded_rectangle(((S-tw)/2-60, y, (S+tw)/2+60, y+120), 60, outline=ACC, width=4)
        d.text(((S-tw)/2, y+28), p, font=f3, fill=INK, **kw); y += 160
    c.save(out, quality=92)

def mainimg(path, out):
    im = prod(path); w, h = im.size; side = int(max(w, h)/0.88)
    c = Image.new('RGB', (side, side), (255, 255, 255))
    a_ = np.asarray(im).astype(int); m = a_.min(axis=2) >= 240
    arr = np.asarray(im).copy(); arr[m] = 255; im = Image.fromarray(arr)
    c.paste(im, ((side-w)//2, (side-h)//2)); c = c.resize((2000, 2000), Image.LANCZOS); c.save(out, quality=95)

if __name__ == '__main__':
    os.makedirs('out', exist_ok=True); plan = {}
    only = sys.argv[1:] or list(L)
    for a in only:
        v = L[a]; n = v['n']
        mid = v['main'] if v['main'] != '-' else '51ZLlwezrFL'
        im = prod(f'src/{mid}.jpg')
        if min(im.size) < 600:
            r = 900/min(im.size); im = im.resize((int(im.width*r), int(im.height*r)), Image.LANCZOS)
        files = []
        if n == 0:
            o = f'out/{a}-main.jpg'; mainimg(f'src/{mid}.jpg', o); files.append(o); n = 1
        fns = [lifestyle] + ([size] if dims(a) else []) + [box, brand, features, uses, details]
        for fn in fns[:max(0, 7-n)]:
            o = f'out/{a}-{fn.__name__}.jpg'; fn(a, im, o); files.append(o)
        plan[a] = files
    json.dump(plan, open('plan7.json', 'w'), indent=0)
    print(sum(len(x) for x in plan.values()), 'imgs', len(plan))
