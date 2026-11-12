from PIL import Image, ImageDraw, ImageFont
import os, sys, json
O = 'out5'; W = 1500; G = 12
def im(n): return Image.open(os.path.join(O, n)).convert('RGB')
def F(s, w='Medium'): return ImageFont.truetype(f'fonts/SST-{w}.ttf', s)
def fw(n): i = im(n); return i.resize((W, int(i.height * W / i.width)), Image.LANCZOS)
def rown(names):
    n = len(names); s = (W - G * (n - 1)) // n; a = im(names[0]); hh = int(a.height * s / a.width)
    r = Image.new('RGB', (W, hh), 'white')
    for i, nm in enumerate(names): r.paste(im(nm).resize((s, hh), Image.LANCZOS), (i * (s + G), 0))
    return r
def split(L, names, large_first):
    s = (W - G) // 2; r = Image.new('RGB', (W, s), 'white'); mh = (s - G) // 2
    a = im(names[0]).resize((s, s), Image.LANCZOS); b = im(names[1]).resize((s, mh), Image.LANCZOS); c = im(names[2]).resize((s, mh), Image.LANCZOS)
    lx, cx = (s + G, 0) if (L == 'ar') == large_first else (0, s + G)
    r.paste(a, (lx, 0)); r.paste(b, (cx, 0)); r.paste(c, (cx, mh + G)); return r
def widget(label):
    r = Image.new('RGB', (W, 330), '#F6F6F4'); d = ImageDraw.Draw(r); s = (W - 60) // 6
    for i in range(6):
        x = 30 + i * s; d.rounded_rectangle((x + 6, 44, x + s - 6, 316), 12, fill='white', outline='#e3e3e3', width=2)
        d.rounded_rectangle((x + 30, 60, x + s - 30, 220), 8, fill='#EFEFEF'); d.rounded_rectangle((x + 30, 266, x + s - 30, 300), 18, fill='#FFD814')
    d.text((W // 2, 22), '[ ' + label + ' ]', font=F(22), fill='#8a8a8a', anchor='mm'); return r
def gal(names):
    r = fw(names[0]); d = ImageDraw.Draw(r); n = len(names)
    for i in range(n): d.ellipse((W / 2 - n * 11 + i * 22, r.height - 34, W / 2 - n * 11 + i * 22 + 11, r.height - 23), fill='#FFD814' if i == 0 else 'white')
    return r
def nav(L, pages, cur):
    r = Image.new('RGB', (W, 70), 'white'); d = ImageDraw.Draw(r); ar = L == 'ar'
    x = W - 24 if ar else 24
    for p in pages:
        t = p['title']; f = F(21, 'Bold' if p['slug'] == cur else 'Medium')
        kw = dict(direction='rtl', language='ar') if ar else {}
        tl = d.textlength(t, font=f, **kw)
        if ar:
            d.text((x, 35), t, font=f, fill='#008080' if p['slug'] == cur else '#333', anchor='rm', **kw)
            if p['slug'] == cur: d.line((x - tl, 60, x, 60), fill='#008080', width=4)
            x -= tl + 34
        else:
            d.text((x, 35), t, font=f, fill='#008080' if p['slug'] == cur else '#333', anchor='lm')
            if p['slug'] == cur: d.line((x, 60, x + tl, 60), fill='#008080', width=4)
            x += tl + 34
    d.line((0, 69, W, 69), fill='#e5e5e5', width=2); return r
def page(L, pages, p):
    parts = []
    for i, (kind, v) in enumerate(p['rows']):
        if kind == 'fw': parts.append(fw(v[0]))
        elif kind == 'row': parts.append(rown(v))
        elif kind in ('split', 'splitr'): parts.append(split(L, v, kind == 'split'))
        elif kind == 'gallery': parts.append(gal(v))
        elif kind == 'stack':
            ss = [fw(n) for n in v]; st = Image.new('RGB', (W, sum(q.height for q in ss))); yy = 0
            for q in ss: st.paste(q, (0, yy)); yy += q.height
            parts.append(st)
        elif kind == 'widget': parts.append(widget(v))
        if i == 0: parts.append(nav(L, pages, p['slug']))
    H = sum(q.height for q in parts) + G * (len(parts) - 1)
    out = Image.new('RGB', (W, H), 'white'); y = 0
    for q in parts: out.paste(q, (0, y)); y += q.height + G
    fn = f'{O}/PAGE_{L}_{p["slug"]}.jpg'; out.save(fn, quality=82); return fn, out.size
if __name__ == '__main__':
    for L in sys.argv[1:] or ['ar', 'en']:
        pages = json.load(open(f'{O}/layout_{L}.json'))
        for p in pages: print(page(L, pages, p))
