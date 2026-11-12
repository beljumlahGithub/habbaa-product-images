from PIL import Image, ImageDraw, ImageFont
import os, sys
O = 'out3'; W = 1500; G = 12
def im(n): return Image.open(os.path.join(O, n)).convert('RGB')
def fw(n): i = im(n); return i.resize((W, int(i.height * W / i.width)), Image.LANCZOS)
def row_large_col(L, large, m1, m2, large_first=True):
    s = (W - G) // 2; r = Image.new('RGB', (W, s), 'white')
    a = im(large).resize((s, s)); b = im(m1).resize((s, (s - G) // 2)); c = im(m2).resize((s, (s - G) // 2))
    lx, cx = (s + G, 0) if (L == 'ar') == large_first else (0, s + G)
    r.paste(a, (lx, 0)); r.paste(b, (cx, 0)); r.paste(c, (cx, (s - G) // 2 + G)); return r
def row_n(names, h=None):
    n = len(names); s = (W - G * (n - 1)) // n; hh = h or s
    r = Image.new('RGB', (W, hh), 'white')
    for i, nm in enumerate(names): r.paste(im(nm).resize((s, hh)), (i * (s + G), 0))
    return r
def title(L, t_ar, t_en):
    r = Image.new('RGB', (W, 120), 'white'); d = ImageDraw.Draw(r)
    if L == 'ar':
        d.text((W - 20, 60), t_ar, font=ImageFont.truetype('fonts/SST-Bold.ttf', 44), fill='#10201F', anchor='rm', direction='rtl', language='ar')
    else:
        d.text((20, 60), t_en, font=ImageFont.truetype('fonts/SST-Bold.ttf', 44), fill='#10201F', anchor='lm')
    return r
def widget(L, label):
    r = Image.new('RGB', (W, 300), '#F7F7F7'); d = ImageDraw.Draw(r)
    s = (W - 60) // 6
    for i in range(6):
        x = 30 + i * s; d.rounded_rectangle((x + 6, 14, x + s - 6, 286), 12, fill='white', outline='#e3e3e3', width=2)
        d.rounded_rectangle((x + 30, 30, x + s - 30, 190), 8, fill='#EFEFEF')
        d.rounded_rectangle((x + 30, 236, x + s - 30, 270), 18, fill='#FFD814')
    d.text((W // 2, 112), label, font=ImageFont.truetype('fonts/SST-Medium.ttf', 24), fill='#999', anchor='mm')
    return r
def gal(L):
    a = im(f'{L}_09a_gallery_1500x750.jpg'); r = Image.new('RGB', (W, 760), 'white')
    r.paste(a.resize((W, 750)), (0, 0)); d = ImageDraw.Draw(r)
    for i in range(8): d.ellipse((W / 2 - 80 + i * 22, 720, W / 2 - 70 + i * 22, 730), fill='white' if i else '#FFD814')
    return r
def page(L):
    P = f'{L}_'
    ar = L == 'ar'
    parts = [fw(P + '00_header_3000x600.jpg'), fw(P + '01_hero_fullwidth_3000x1500.jpg'),
             title(L, 'تسوّق حسب الهبّة', 'Shop by gust'),
             row_n([P + f'02{x}_cat_small_750.jpg' for x in 'abcd']),
             row_large_col(L, P + '03a_thermos_large_1500.jpg', P + '03b_majlis_medium_1500x750.jpg', P + '03c_cups_card_medium_1500x750.jpg'),
             fw(P + '04_majlis_shoppable_3000x1500.jpg'),
             widget(L, '[ أفضل المبيعات - ويدجت أمازون ]' if False else '[ Amazon Best Sellers widget ]'),
             fw(P + '05_spotlight_office_3000x1300.jpg'),
             row_n([P + '06a_a4_large_1500.jpg', P + '06b_cards_large_1500.jpg']),
             fw(P + '07_trolley_fullwidth_3000x1500.jpg'),
             row_large_col(L, P + '08a_containers_large_1500.jpg', P + '08b_basket_medium_1500x750.jpg', P + '08c_gift_medium_1500x750.jpg', large_first=False),
             title(L, 'هبّة في كل بيت', 'A gust in every home'), gal(L),
             fw(P + '10_story_kite_3000x1500.jpg'),
             row_n([P + f'11{x}_{n}_small_750.jpg' for x, n in zip('abcd', ['umbrella', 'ball', 'fan', 'basket'])]),
             widget(L, '[ Amazon Recommended for you widget ]'),
             fw(P + '12_ramadan_teaser_3000x1500.jpg'), fw(P + '13_why_3000x560.jpg')]
    H = sum(p.height for p in parts) + G * (len(parts) - 1)
    out = Image.new('RGB', (W, H), 'white'); y = 0
    for p in parts: out.paste(p, (0, y)); y += p.height + G
    out.save(f'HABBAA_home_v3_{L}.jpg', quality=82)
    return out
if __name__ == '__main__':
    for L in sys.argv[1:] or ['ar', 'en']:
        o = page(L); print(L, o.size)
