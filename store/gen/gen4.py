#!/usr/bin/env python3
"""HABBAA brand store v4 — full store: home + 9 sub-pages, AR + EN.
Concept 'هبّة / Catch the gust' kept; adds section system, best sellers, picks, all products, deals."""
import os, sys, json
from PIL import Image, ImageDraw, ImageFilter, ImageOps
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen3 as g
from gen3 import (raw, cut, fit, grain, shade, layered, block, left_block, extend_left, mobile_canvas, word_tile,
                  font, kw, tw, cta, logo, INK, TEAL, TEAL_D, GOLD, CREAM, B)
from gen2 import AN

OUT = os.path.join(B, 'out4'); os.makedirs(OUT, exist_ok=True)
SAND = '#EFE6D6'; GREY = '#5E6B69'

X = {
 # categories
 'party': ('الحفلات والهدايا', 'Party & Gifts'), 'host': ('الضيافة', 'Cups & Hosting'),
 'office': ('المكتب والمدرسة', 'Office & School'), 'kitchen': ('المطبخ والتخزين', 'Kitchen & Storage'),
 'home': ('البيت والتنظيم', 'Home & Organisation'), 'play': ('اللعب والرحلات', 'Play & Outdoor'),
 'best': ('الأكثر مبيعاً', 'Best Sellers'), 'all': ('جميع المنتجات', 'All Products'),
 'picks': ('مختارات هبّة', 'HABBAA Picks'), 'deals': ('العروض', 'Deals'), 'ram': ('رمضان والعيد', 'Ramadan & Eid'),
 'homep': ('الرئيسية', 'Home'),
 'shop': ('تسوّق الآن', 'Shop now'), 'disc': ('اكتشف', 'Explore'),
 # home sections
 's1': ('تسوّق حسب القسم', 'Shop by category'), 's1s': ('ستة أقسام تغطي يومك كله', 'Six departments for your whole day'),
 's2': ('الأكثر مبيعاً', 'Best sellers'), 's2s': ('المنتجات اللي يرجع لها عملاؤنا', 'The products our customers come back for'),
 's3': ('مختارات هبّة', 'HABBAA picks'), 's3s': ('اخترناها لك بعناية من كل قسم', 'Hand-picked for you from every department'),
 's4': ('هبّة في كل بيت', 'A gust in every home'), 's4s': ('لحظات من يومك مع منتجاتنا', 'Moments from your day with our products'),
 's5': ('عروض اليوم', 'Today\'s deals'), 's5s': ('خصومات على منتجات مختارة', 'Savings on selected products'),
 's6': ('كل منتجات القسم', 'All products in this department'), 's6s': ('تصفّح القسم كامل', 'Browse the full range'),
 's7': ('أقسام أخرى', 'More departments'), 's7s': ('كمّل جولتك في المتجر', 'Keep exploring the store'),
 's8': ('تسوّق حسب النوع', 'Shop by type'), 's8s': ('اختر اللي تدوّر عليه', 'Pick what you are looking for'),
 'bs_eye': ('الأكثر مبيعاً', 'BEST SELLERS'), 'bs_t': ('نجوم هبّة', 'The crowd favourites.'),
 'bs_s': ('المنتجات الأكثر مبيعاً في متجرنا', 'The best-selling products in our store'), 'bs_c': ('تسوّق الأكثر مبيعاً', 'Shop best sellers'),
 'all_eye': ('جميع المنتجات', 'ALL PRODUCTS'), 'all_t': ('كل شي ليومك', 'Everything for your day.'),
 'all_s': ('تصفّح كل منتجات هبّة في مكان واحد', 'Browse every HABBAA product in one place'), 'all_c': ('تصفّح الكل', 'Browse all'),
 # picks
 'p_th': ('القهوة على حرارتها', 'Coffee, kept warm.'), 'p_th_w': ('قهوة', 'COFFEE'), 'p_th_c': ('تسوّق الترامس', 'Shop flasks'),
 'p_tr': ('مشوار السوق صار أخف', 'Errands, lighter.'), 'p_tr_w': ('مشوار', 'EASY'), 'p_tr_c': ('تسوّق العربات', 'Shop trolleys'),
 'p_cu': ('أكواب ورقية', 'Paper cups'), 'p_ba': ('أكياس هدايا', 'Gift bags'), 'p_pe': ('قشّارة عملية', 'Handy peeler'), 'p_pn': ('أقلام رصاص', 'Pencils'),
 # page heroes
 'party_eye': ('هبّة الحفلات', 'THE PARTY GUST'), 'party_t': ('كل حفلة تبدأ من هنا', 'Every party starts here.'),
 'party_s': ('زينة، قصاصات، أكياس هدايا وأشرطة تغليف', 'Banners, confetti, gift bags and ribbons'),
 'host_eye': ('هبّة الضيافة', 'THE HOSTING GUST'), 'host_t': ('ضيافة على أصولها', 'Hosting, done right.'),
 'host_s': ('ترامس، أكواب وصواني لكل مجلس', 'Flasks, cups and trays for every gathering'),
 'office_eye': ('هبّة المكتب والمدرسة', 'THE DESK GUST'), 'office_t': ('تحت الضوء', 'In the spotlight.'),
 'office_s': ('ورق A4، مقصات، أقلام رصاص وأصابع غراء', 'A4 paper, scissors, pencils and glue sticks'),
 'kitchen_eye': ('هبّة المطبخ', 'THE KITCHEN GUST'), 'kitchen_t': ('مطبخ مرتّب، أكل طازج', 'Tidy kitchen, fresh food.'),
 'kitchen_s': ('حافظات طعام وأدوات مطبخ عملية', 'Food containers and practical kitchen tools'),
 'home_eye': ('هبّة البيت', 'THE HOME GUST'), 'home_t': ('مشوار السوق صار أخف', 'Errands, lighter.'),
 'home_s': ('عربات تسوق، سلال غسيل وأغراض تنظّم بيتك', 'Shopping trolleys, laundry baskets and home organisers'),
 'play_eye': ('هبّة الطلعات', 'THE OUTDOOR GUST'), 'play_t': ('كشتة ولعب وهوا', 'Out you go.'),
 'play_s': ('طائرات ورقية، كرات، ورق لعب ومظلات', 'Kites, balls, playing cards and umbrellas'),
 # sub tiles
 't_banner': ('زينة الحفلات', 'Party decor'), 't_conf': ('قصاصات الاحتفال', 'Confetti poppers'), 't_bags': ('أكياس الهدايا', 'Gift bags'),
 't_ribbon': ('أشرطة التغليف', 'Ribbons & wrap'), 't_fans': ('توزيعات الأعراس', 'Wedding favours'), 'w_gift': ('هدايا', 'GIFTS'),
 't_flask': ('ترامس', 'Flasks'), 't_pcups': ('أكواب ورقية', 'Paper cups'), 't_plcups': ('أكواب بلاستيك', 'Plastic cups'),
 't_tray': ('صواني التقديم', 'Serving trays'), 'w_host': ('ضيافة', 'SERVE'), 't_majlis': ('مجلسك جاهز', 'Your majlis, ready'), 't_night': ('سهرة رمضانية', 'Ramadan nights'),
 't_a4': ('ورق A4', 'A4 paper'), 't_pen': ('أقلام رصاص', 'Pencils'), 't_sci': ('مقصات وأشغال', 'Scissors & crafts'), 't_glue': ('أصابع الغراء', 'Glue sticks'),
 'w_write': ('اكتب', 'WRITE'), 't_craft': ('ركن الأشغال', 'Craft corner'), 't_desk': ('مكتب جاهز', 'Desk, ready'),
 't_cont': ('حافظات الطعام', 'Food containers'), 't_peel': ('أدوات المطبخ', 'Kitchen tools'), 't_glass': ('حافظات زجاج', 'Glass containers'),
 't_prep': ('تحضير أسهل', 'Easier prep'), 'w_fresh': ('طازج', 'FRESH'), 't_fresh': ('خلّ أكلك طازج', 'Keep it fresh'), 't_counter': ('مطبخ مرتّب', 'A tidy counter'),
 't_trol': ('عربات التسوق', 'Shopping trolleys'), 't_bask': ('سلال الغسيل', 'Laundry baskets'), 't_glov': ('قفازات قطنية', 'Cotton gloves'),
 't_entry': ('مدخل مرتّب', 'A tidy entryway'), 't_corner': ('ركن مرتّب', 'A tidy corner'),
 't_kite': ('طائرات ورقية', 'Kites'), 't_ball': ('كرات', 'Balls'), 't_cards': ('ورق اللعب', 'Playing cards'), 't_umb': ('مظلات', 'Umbrellas'),
 'w_game': ('سهرة', 'GAME ON'), 't_game': ('ورق لعب لسهرة الشلة', 'Cards for game night'), 't_kashta': ('طلعة البر', 'Desert outing'), 't_sky': ('خلّها تطير', 'Let it fly'), 't_court': ('العب برّا', 'Play outside'),
 'kt_eye': g.C['kt_eye'], 'kt_t': g.C['kt_t'], 'kt_s': g.C['kt_s'], 'kt_c': g.C['kt_c'],
 'sh_t': g.C['sh_t'], 'sh_s': g.C['sh_s'],
 'rm_eye': g.C['rm_eye'], 'rm_t': g.C['rm_t'], 'rm_s': g.C['rm_s'], 'rm_c': g.C['rm_c'],
}
def x(k, L): return X[k][0] if L == 'ar' else X[k][1]

# category visuals: small-tile, medium-tile, large-tile (scene, focus)
CAT = {
 'party':   {'s': ('party_a', (0.6, 0.5)), 'm': ('bday', (0.6, 0.5)), 'l': ('bday', (0.66, 0.5))},
 'host':    {'s': ('majlis_a', (0.68, 0.6)), 'm': ('majlis_b', (0.75, 0.6)), 'l': ('majlis_a', (0.7, 0.6))},
 'office':  {'s': ('school_a', (0.7, 0.85)), 'm': ('crafts', (0.75, 0.6)), 'l': ('school_b', (0.6, 0.6))},
 'kitchen': {'s': ('cont_b', (0.5, 0.5)), 'm': ('kitchen', (0.85, 0.7)), 'l': ('cont_a', (0.5, 0.5))},
 'home':    {'s': ('basket_a', (0.5, 0.6)), 'm': ('basket_a', (0.5, 0.62)), 'l': ('trolley_sq', (0.5, 0.5))},
 'play':    {'s': ('ball_sa', (0.5, 0.6)), 'm': ('kashta', (0.8, 0.75)), 'l': ('kashta', (0.72, 0.7))},
 'best':    {'s': ('podium', (0.72, 0.5))}, 'all': {'s': ('allprod', (0.62, 0.5))},
}
ORDER = ['party', 'host', 'office', 'kitchen', 'home', 'play']

# ---------- components ----------
def tile(L, scene, focus, title, size=(750, 750), link=None, word=None, badge=None):
    """Photo tile. word=(cutname, word, cy, wsize, alpha, fill) puts a giant word behind the product."""
    W, H = size
    if word:
        im = layered(scene, word[0], size, focus, word[1], L, word[2], word[3], alpha=word[4],
                     fill=word[5] if len(word) > 5 else (255, 255, 255))
    else:
        im = fit(raw(scene), size, focus).convert('RGBA')
    im = shade(im, 'bottom', 0.5, 0.78, (8, 18, 18)); d = ImageDraw.Draw(im); ar = L == 'ar'
    pad = int(W * 0.06) if W <= 750 else 90; xx = W - pad if ar else pad
    ts = {750: 74, 1500: 96}[W] if H < 1500 else 120
    while tw(d, title, L, 'b', ts) > W - 2 * pad: ts -= 4
    base = H - int(ts * 1.75)
    d.text((xx, base), title, font=font(L, 'b', ts), fill='white', anchor=('rs' if ar else 'ls'), **kw(L))
    fs = int(ts * 0.44); t = link or x('disc', L)
    d.text((xx, base + fs * 1.75), t, font=font(L, 'm', fs), fill=GOLD, anchor=('rs' if ar else 'ls'), **kw(L))
    tl = tw(d, t, L, 'm', fs); ax = xx - tl - fs * 0.8 if ar else xx + tl + fs * 0.8; cy = base + fs * 1.42; a = fs * 0.28
    pts = [(ax + a, cy - a), (ax, cy), (ax + a, cy + a)] if ar else [(ax - a, cy - a), (ax, cy), (ax - a, cy + a)]
    d.line(pts, fill=GOLD, width=max(4, fs // 7), joint='curve')
    if badge:
        bs = 34 if W <= 750 else 44; bw = tw(d, badge, L, 'b', bs) + bs * 1.6; bh = bs * 2
        bx = pad if ar else W - pad - bw
        d.rounded_rectangle((bx, pad, bx + bw, pad + bh), bh / 2, fill=GOLD)
        d.text((bx + bw / 2, pad + bh / 2 + 2), badge, font=font(L, 'b', bs), fill=INK, anchor='mm', **kw(L))
    return im

def gust(d, W, H, side, cols):
    """Concentric sweeping arcs from the far bottom corner: the brand 'gust' gesture."""
    cx = 120 if side == 'left' else W - 120; cy = H * 1.9
    for i, col in enumerate(cols):
        r = H * (1.25 + i * 0.3)
        d.arc((cx - r, cy - r, cx + r, cy + r), 180, 360, fill=col, width=10)

def sec(L, num, title, sub, W=3000, H=380, bg=CREAM):
    im = Image.new('RGBA', (W, H), bg); d = ImageDraw.Draw(im); ar = L == 'ar'
    gust(d, W, H, 'left' if ar else 'right', [TEAL, GOLD, '#60A591'])
    im = grain(im, 5).convert('RGBA'); d = ImageDraw.Draw(im)
    xx = W - 170 if ar else 170; anc = 'r' if ar else 'l'; k = H / 380
    ns = int(58 * k ** 0.5); tsz = int(118 * k ** 0.6); y0 = int(H * 0.17)
    n = AN(L, f'{num:02d}')
    d.text((xx, y0), n, font=font(L, 'b', ns), fill=TEAL, anchor=anc + 'a', **kw(L))
    nl = tw(d, n, L, 'b', ns); lx = xx - nl - 30 if ar else xx + nl + 30; ly = y0 + ns * 0.62
    d.line((lx - 150, ly, lx, ly) if ar else (lx, ly, lx + 150, ly), fill=GOLD, width=7)
    ty = y0 + ns * 1.25
    d.text((xx, ty), title, font=font(L, 'b', tsz), fill=INK, anchor=anc + 'a', **kw(L))
    tl = tw(d, title, L, 'b', tsz); sx_ = xx - tl - 70 if ar else xx + tl + 70
    d.text((sx_, ty + tsz * 0.72), sub, font=font(L, 'r', int(50 * k ** 0.5)), fill=GREY, anchor=anc + 'm', **kw(L))
    return im

def banner(L, scene, focus, eye, title, sub, button, W=3000, H=1500, shade_col=(0, 0, 0), strength=0.5, fg='white',
           ext=False, push=0, zone=0.36, tsize=190, y=None, frac=0.6, eye_col=GOLD, btn_bg='white', btn_fg=INK):
    im = (extend_left(raw(scene), (W, H), push=push) if ext else fit(raw(scene), (W, H), focus)).convert('RGBA')
    if strength: im = shade(im, 'left', frac, strength, shade_col)
    left_block(im, L, 170, y or int(H * 0.27), zone, eye=eye, title=title, sub=sub, button=button, tsize=tsize,
               fg=fg, eye_col=eye_col, btn_bg=btn_bg, btn_fg=btn_fg)
    return im

def mbanner(L, scene, fx, eye, title, sub, button, shade_col=(0, 0, 0), fg='white', eye_col=GOLD, btn_bg='white', btn_fg=INK, strength=0.45):
    im = mobile_canvas(scene, fx)
    if strength: im = shade(im, 'top', 0.4, strength, shade_col)
    block(im, L, 1400 if L == 'ar' else 100, 90, eye, title, sub, button, tsize=120, maxw=1300, fg=fg, eye_col=eye_col,
          btn_bg=btn_bg, btn_fg=btn_fg)
    return im

def phead(L, scene, focus, title, shade_col=(6, 40, 42), strength=0.8, ext=False, W=3000, H=600):
    im = (extend_left(raw(scene), (W, H)) if ext else fit(raw(scene), (W, H), focus)).convert('RGBA'); im = shade(im, 'left', 0.72, strength, shade_col)
    d = ImageDraw.Draw(im); lg = logo('white', 210); ts = 150
    tl = int(tw(d, title, L, 'b', ts)); gap = 70; x0 = 170
    if L == 'ar':
        d.text((x0 + tl, H / 2 + 6), title, font=font(L, 'b', ts), fill='white', anchor='rm', **kw(L))
        lx = x0 + tl + gap; d.line((lx, H / 2 - 110, lx, H / 2 + 110), fill=GOLD, width=6)
        im.alpha_composite(lg, (lx + gap, int(H / 2 - lg.height / 2)))
    else:
        im.alpha_composite(lg, (x0, int(H / 2 - lg.height / 2)))
        lx = x0 + lg.width + gap; d.line((lx, H / 2 - 110, lx, H / 2 + 110), fill=GOLD, width=6)
        d.text((lx + gap, H / 2 + 6), title, font=font(L, 'b', ts), fill='white', anchor='lm', **kw(L))
    return im

def wtile(L, bg, ct, word, title, button, cy=0.5, wsize=600, alpha=230, fill=(255, 255, 255), focus=(0.5, 0.5), eye=None):
    return word_tile(L, bg, ct, word, eye, title, button, focus=focus, cy=cy, wsize=wsize, alpha=alpha, fill=fill)

# ---------- page collector ----------
class Page:
    def __init__(self, L, slug, title):
        self.L, self.slug, self.title, self.rows, self.n = L, slug, title, [], 0
    def _save(self, im, tag):
        fn = f'{self.L}_{self.slug}_{self.n:02d}{tag}.jpg'; p = os.path.join(OUT, fn)
        im.convert('RGB').save(p, quality=90, optimize=True)
        if os.path.getsize(p) > 4_800_000: im.convert('RGB').save(p, quality=82, optimize=True)
        return fn
    def fw(self, im, tag, mobile=None):
        self.n += 1; self.rows.append(('fw', [self._save(im, '_' + tag)]))
        if mobile is not None: self._save(mobile, 'm_' + tag + '_mobile')
    def row(self, ims, tag):
        self.n += 1; self.rows.append(('row', [self._save(im, 'abcdefgh'[i] + '_' + tag) for i, im in enumerate(ims)]))
    def split(self, large, m1, m2, tag, large_first=True):
        self.n += 1
        self.rows.append(('split' if large_first else 'splitr', [self._save(large, 'a_' + tag + '_large'),
                          self._save(m1, 'b_' + tag + '_medium'), self._save(m2, 'c_' + tag + '_medium')]))
    def gallery(self, ims, tag):
        self.n += 1; self.rows.append(('gallery', [self._save(im, 'abcdefgh'[i] + '_' + tag) for i, im in enumerate(ims)]))
    def widget(self, label): self.rows.append(('widget', label))
    def done(self): return {'slug': self.slug, 'title': self.title, 'rows': self.rows}

def cat_small(L, k): s, f = CAT[k]['s']; return tile(L, s, f, x(k, L))
def cross(L, P, skip):
    P.fw(sec(L, 3, x('s7', L), x('s7s', L), H=300), 'sec_more')
    ks = [k for k in ORDER if k != skip][:3] + ['best']
    P.row([cat_small(L, k) for k in ks], 'more_small')

# ---------- HOME ----------
def home(L):
    P = Page(L, 'main', x('homep', L))
    P.fw(g.header(L), 'header_3000x600')
    P.fw(g.hero(L), 'hero_3000x1500', mobile=g.hero(L, mobile=True))
    P.fw(sec(L, 1, x('s1', L), x('s1s', L)), 'sec_categories')
    P.split(tile(L, *CAT['party']['l'], x('party', L), (1500, 1500)), tile(L, *CAT['host']['m'], x('host', L), (1500, 750)),
            tile(L, *CAT['office']['m'], x('office', L), (1500, 750)), 'cats1')
    P.split(tile(L, *CAT['play']['l'], x('play', L), (1500, 1500)), tile(L, *CAT['kitchen']['m'], x('kitchen', L), (1500, 750)),
            tile(L, *CAT['home']['m'], x('home', L), (1500, 750)), 'cats2', large_first=False)
    P.fw(sec(L, 2, x('s2', L), x('s2s', L)), 'sec_best')
    P.fw(banner(L, 'podium', (0.5, 0.5), x('bs_eye', L), x('bs_t', L), x('bs_s', L), x('bs_c', L), H=1200, strength=0.0,
                ext=True, zone=0.40, y=300, tsize=180), 'best_banner_3000x1200',
         mobile=mbanner(L, 'podium', 0.72, x('bs_eye', L), x('bs_t', L), x('bs_s', L), x('bs_c', L), strength=0))
    P.widget('Best Sellers widget (Amazon, live)')
    P.fw(sec(L, 3, x('s3', L), x('s3s', L)), 'sec_picks')
    P.row([wtile(L, 'thermos_a', 'thermos', x('p_th_w', L), x('p_th', L), x('p_th_c', L), cy=0.52, wsize=560),
           wtile(L, 'trolley_sq', 'trolley_sq', x('p_tr_w', L), x('p_tr', L), x('p_tr_c', L), cy=0.5, wsize=520)],
          'picks_large')
    P.row([tile(L, 'cups_sq', (0.5, 0.5), x('p_cu', L)), tile(L, 'bags_sq', (0.5, 0.5), x('p_ba', L)),
           tile(L, 'peeler_sq', (0.5, 0.5), x('p_pe', L)), tile(L, 'pencils_sq', (0.5, 0.5), x('p_pn', L))], 'picks_small')
    P.widget('Product grid: hand-picked ASINs')
    P.fw(banner(L, 'majlis_a', (0.5, 0.5), None, x('sh_t', L), x('sh_s', L), None, shade_col=(30, 18, 6), strength=0.62, y=560),
         'majlis_shoppable_3000x1500')
    P.fw(sec(L, 4, x('s4', L), x('s4s', L)), 'sec_gallery')
    picks = [('bday', (0.6, 0.5)), ('ram_b', (0.6, 0.55)), ('kashta', (0.75, 0.7)), ('kitchen', (0.8, 0.7)),
             ('gift_b', (0.7, 0.5)), ('crafts', (0.7, 0.6)), ('fan_a', (0.5, 0.45)), ('homehero', (0.7, 0.85))]
    P.gallery([fit(raw(n), (1500, 750), f) for n, f in picks], 'gallery_1500x750')
    P.fw(g.kite_story(L), 'story_3000x1500', mobile=g.kite_story(L, mobile=True))
    P.fw(sec(L, 5, x('s5', L), x('s5s', L)), 'sec_deals')
    P.widget('Featured Deals widget (Amazon, live)')
    P.fw(banner(L, 'allprod', (0.5, 0.5), x('all_eye', L), x('all_t', L), x('all_s', L), x('all_c', L), H=1100, strength=0,
                fg=INK, eye_col=TEAL, btn_bg=TEAL, btn_fg='white', zone=0.28, y=290, tsize=170, ext=True),
         'all_banner_3000x1100',
         mobile=mbanner(L, 'allprod', 0.62, x('all_eye', L), x('all_t', L), x('all_s', L), x('all_c', L), fg=INK, eye_col=TEAL,
                        btn_bg=TEAL, btn_fg='white', strength=0))
    P.fw(banner(L, 'ram_a', (0.5, 0.5), x('rm_eye', L), x('rm_t', L), x('rm_s', L), x('rm_c', L), shade_col=(6, 10, 30),
                strength=0.55, y=420), 'ramadan_3000x1500')
    P.fw(g.why(L), 'why_3000x560')
    return P.done()

# ---------- SUB PAGES ----------
def subpage(L, k, head, hero, tiles, feat, extra=None):
    P = Page(L, k, x(k, L))
    P.fw(phead(L, head[0], head[1], x(k, L), *(head[2:] or [])), 'header_3000x600')
    hk = dict(hero[3]) if len(hero) > 3 else {}
    mk = {kk: v for kk, v in hk.items() if kk in ('shade_col', 'fg', 'eye_col', 'btn_bg', 'btn_fg')}
    P.fw(banner(L, hero[0], hero[1], x(k + '_eye', L), x(k + '_t', L), x(k + '_s', L), x('shop', L), **hk), 'hero_3000x1500',
         mobile=mbanner(L, hero[0], hero[2], x(k + '_eye', L), x(k + '_t', L), x(k + '_s', L), x('shop', L), **mk))
    P.fw(sec(L, 1, x('s8', L), x('s8s', L), H=300), 'sec_types')
    P.row([tile(L, s, f, x(t, L), word=w) for (s, f, t, w) in tiles], 'types_small')
    lg, m1, m2, first = feat
    P.split(wtile(L, **{**lg, 'word': x(lg['word'], L), 'title': x(lg['title'], L), 'button': x('shop', L)}),
            tile(L, m1[0], m1[1], x(m1[2], L), (1500, 750)), tile(L, m2[0], m2[1], x(m2[2], L), (1500, 750)), 'feature', first)
    if extra: extra(P)
    P.fw(sec(L, 2, x('s6', L), x('s6s', L), H=300), 'sec_all')
    P.widget('Product grid: all ASINs of this department')
    cross(L, P, k)
    return P.done()

def pages(L):
    out = [home(L)]
    out.append(subpage(L, 'party', ('header_a', (0.5, 0.5)),
        ('bday', (0.5, 0.5), 0.62, dict(shade_col=(60, 30, 40), strength=0.6, zone=0.30, y=400, tsize=170, eye_col='white')),
        [('bday', (0.62, 0.35), 't_banner', None), ('party_a', (0.6, 0.5), 't_conf', None),
         ('bags_sq', (0.5, 0.5), 't_bags', None), ('gift_a', (0.72, 0.6), 't_ribbon', None)],
        (dict(bg='bags_sq', ct='bags_sq', word='w_gift', title='t_bags', cy=0.5, wsize=560), ('gift_b', (0.75, 0.5), 't_ribbon'),
         ('fan_b', (0.5, 0.4), 't_fans'), True),
        extra=lambda P: P.fw(banner(L, 'party_b', (0.5, 0.5), g.c('h_eye', L), g.c('h_t', L), g.c('h_s', L), x('shop', L),
                                    shade_col=(4, 40, 42), strength=0.55, ext=True, zone=0.30, y=400, tsize=230), 'gust_3000x1500')))
    out.append(subpage(L, 'host', ('majlis_b', (0.6, 0.62), (40, 22, 8), 0.8),
        ('majlis_a', (0.5, 0.5), 0.72, dict(shade_col=(30, 18, 6), strength=0.62, y=400, eye_col='white')),
        [('thermos_a', (0.5, 0.5), 't_flask', None), ('cups_sq', (0.5, 0.5), 't_pcups', None),
         ('pcup_sq', (0.5, 0.5), 't_plcups', None), ('ram_a', (0.72, 0.72), 't_tray', None)],
        (dict(bg='cups_sq', ct='cups_sq', word='w_host', title='t_pcups', cy=0.48, wsize=560), ('majlis_b', (0.75, 0.6), 't_majlis'),
         ('ram_b', (0.62, 0.55), 't_night'), False)))
    out.append(subpage(L, 'office', ('school_a', (0.6, 0.72), (8, 10, 14), 0.75),
        ('school_b', (0.5, 0.5), 0.62, dict(strength=0.35, ext=True, push=330, zone=0.30, y=400)),
        [('a4_b', (0.5, 0.5), 't_a4', None), ('pencils_sq', (0.5, 0.5), 't_pen', None),
         ('crafts', (0.62, 0.7), 't_sci', None), ('school_b', (0.45, 0.9), 't_glue', None)],
        (dict(bg='pencils_sq', ct='pencils_sq', word='w_write', title='t_pen', cy=0.5, wsize=560), ('crafts', (0.75, 0.6), 't_craft'),
         ('school_a', (0.7, 0.7), 't_desk'), True)))
    out.append(subpage(L, 'kitchen', ('kitchen', (0.8, 0.72), (20, 30, 26), 0.75),
        ('kitchen', (0.5, 0.5), 0.75, dict(shade_col=(20, 30, 26), strength=0.62, y=400, tsize=170, eye_col='white')),
        [('cont_a', (0.5, 0.5), 't_cont', None), ('peeler_sq', (0.5, 0.5), 't_peel', None),
         ('pantry', (0.5, 0.5), 't_glass', None), ('kitchen', (0.92, 0.9), 't_prep', None)],
        (dict(bg='cont_a', ct='cont', word='w_fresh', title='t_fresh', cy=0.5, wsize=600, alpha=0), ('kitchen', (0.85, 0.7), 't_counter'),
         ('pantry', (0.5, 0.55), 't_glass'), False)))
    out.append(subpage(L, 'home', ('homehero', (0.7, 0.82), (40, 30, 20), 0.7),
        ('trolley_a', (0.5, 0.5), 0.75, dict(shade_col=(70, 40, 10), strength=0.5, y=400, tsize=170, eye_col='white')),
        [('trolley_sq', (0.5, 0.5), 't_trol', None), ('basket_a', (0.5, 0.6), 't_bask', None),
         ('gloves', (0.6, 0.7), 't_glov', None), ('homehero', (0.62, 0.9), 't_entry', None)],
        (dict(bg='trolley_sq', ct='trolley_sq', word='p_tr_w', title='t_trol', cy=0.5, wsize=520),
         ('gloves', (0.6, 0.72), 't_glov'), ('basket_b', (0.6, 0.6), 't_corner'), True)))
    out.append(subpage(L, 'play', ('kite_b', (0.6, 0.5), (90, 45, 10), 0.6),
        ('kashta', (0.5, 0.5), 0.75, dict(shade_col=(70, 35, 5), strength=0.5, y=380, eye_col='white')),
        [('kite_a', (0.72, 0.45), 't_kite', None), ('ball_sa', (0.5, 0.6), 't_ball', None),
         ('cards_b', (0.5, 0.5), 't_cards', None), ('umb_b', (0.5, 0.5), 't_umb', None)],
        (dict(bg='cards_b', ct='cards', word='w_game', title='t_game', cy=0.5, wsize=600, alpha=210, fill=(255, 214, 214)),
         ('kashta', (0.8, 0.75), 't_kashta'), ('kite_b', (0.7, 0.5), 't_sky'), False)))
    # Best sellers page
    P = Page(L, 'best', x('best', L))
    P.fw(phead(L, 'podium', (0.6, 0.6), x('best', L), (4, 30, 34), 0.0, True), 'header_3000x600')
    P.fw(banner(L, 'podium', (0.5, 0.5), x('bs_eye', L), x('bs_t', L), x('bs_s', L), None, H=1200, strength=0, ext=True,
                zone=0.40, y=340, tsize=180), 'hero_3000x1200',
         mobile=mbanner(L, 'podium', 0.72, x('bs_eye', L), x('bs_t', L), x('bs_s', L), None, strength=0))
    P.widget('Best Sellers widget (Amazon, live)')
    P.row([wtile(L, 'trolley_sq', 'trolley_sq', x('p_tr_w', L), x('t_trol', L), x('shop', L), wsize=520),
           wtile(L, 'a4_b', 'a4', 'A4', x('t_a4', L), x('shop', L), wsize=900)], 'stars_large')
    P.row([tile(L, 'party_a', (0.6, 0.5), x('t_conf', L)), tile(L, 'cups_sq', (0.5, 0.5), x('t_pcups', L)),
           tile(L, 'bags_sq', (0.5, 0.5), x('t_bags', L)), tile(L, 'thermos_a', (0.5, 0.5), x('t_flask', L))], 'stars_small')
    P.fw(sec(L, 2, x('s1', L), x('s1s', L), H=300), 'sec_categories')
    P.row([cat_small(L, k) for k in ORDER[:4]], 'cats_small')
    out.append(P.done())
    # All products page
    P = Page(L, 'all', x('all', L))
    P.fw(phead(L, 'allprod', (0.62, 0.5), x('all', L), (90, 60, 30), 0.7, True), 'header_3000x600')
    P.fw(sec(L, 1, x('s1', L), x('s1s', L), H=300), 'sec_categories')
    P.row([tile(L, *CAT[k]['m'], x(k, L), (1500, 750)) for k in ORDER[:2]], 'cats_m1')
    P.row([tile(L, *CAT[k]['m'], x(k, L), (1500, 750)) for k in ORDER[2:4]], 'cats_m2')
    P.row([tile(L, *CAT[k]['m'], x(k, L), (1500, 750)) for k in ORDER[4:6]], 'cats_m3')
    P.fw(sec(L, 2, x('all', L), x('all_s', L), H=300), 'sec_all')
    P.widget('Product grid: full catalogue (all eligible ASINs)')
    P.row([cat_small(L, 'best'), tile(L, 'thermos_a', (0.5, 0.5), x('picks', L)), tile(L, 'ram_b', (0.62, 0.6), x('ram', L)),
           tile(L, 'party_a', (0.6, 0.5), x('deals', L))], 'quick_small')
    out.append(P.done())
    # Ramadan & Eid (reuse v3 builder look, collected here)
    P = Page(L, 'ramadan', x('ram', L)); r = g.r
    P.fw(phead(L, 'ram_b', (0.6, 0.45), x('ram', L), (6, 10, 30), 0.8), 'header_3000x600')
    P.fw(banner(L, 'ram_b', (0.5, 0.5), r('r1_eye', L), r('r1_t', L), r('r1_s', L), r('r1_c', L), shade_col=(6, 10, 30), strength=0.6, y=420),
         'hero_3000x1500', mobile=mbanner(L, 'ram_b', 0.72, r('r1_eye', L), r('r1_t', L), r('r1_s', L), r('r1_c', L), shade_col=(6, 10, 30)))
    P.split(wtile(L, 'thermos_a', 'thermos', x('p_th_w', L), r('r2_t', L), r('r2_c', L), cy=0.52, wsize=560),
            tile(L, 'ram_a', (0.72, 0.6), r('r3_t', L), (1500, 750)), tile(L, 'majlis_a', (0.68, 0.62), r('r4_t', L), (1500, 750)), 'hosting')
    P.fw(banner(L, 'party_a', (0.5, 0.5), r('e1_eye', L), r('e1_t', L), r('e1_s', L), r('e1_c', L), shade_col=(4, 40, 42),
                strength=0.55, y=420, ext=True, push=200, zone=0.32), 'eid_3000x1500')
    P.row([tile(L, 'gift_b', (0.8, 0.5), r('e2_t', L), (1500, 750)), tile(L, 'fan_b', (0.5, 0.4), r('e3_t', L), (1500, 750))], 'eid_medium')
    P.widget('Product grid: Ramadan & Eid ASINs')
    out.append(P.done())
    return out

if __name__ == '__main__':
    for L in (sys.argv[1:] or ['ar', 'en']):
        json.dump(pages(L), open(os.path.join(OUT, f'layout_{L}.json'), 'w'), ensure_ascii=False, indent=1)
    print('ok', len(os.listdir(OUT)))
