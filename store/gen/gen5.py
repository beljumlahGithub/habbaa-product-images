#!/usr/bin/env python3
"""HABBAA store v5 — adds the 4-banner continuous 'gust cascade', video tile, shop-the-scene, varied sub-page layouts."""
import os, sys, json
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen3 as g, gen4 as v4
from gen4 import (x, X, tile, sec, banner, mbanner, wtile, Page, CAT, raw, fit, shade, block, grain, font, kw, tw, cta,
                  INK, TEAL, GOLD, CREAM, B, AN, gust)
OUT = os.path.join(B, 'out5'); os.makedirs(OUT, exist_ok=True); v4.OUT = OUT

X.update({
 'c0': ('هبّة تمرّ على يومك', 'One gust, through your whole day'), 'c0s': ('أربع محطات تكمّل بعضها', 'Four stops that flow into each other'),
 'c1': ('تبدأ بفرحة', 'It starts with a pop.'), 'c1s': ('قصاصات، أشرطة وأكياس هدايا', 'Confetti, ribbons and gift bags'), 'c1c': ('تسوّق الحفلات', 'Shop party'),
 'c2': ('تكمّل بفنجال', 'Then, a cup of coffee.'), 'c2s': ('ترامس وأكواب لضيافتك', 'Flasks and cups for your guests'), 'c2c': ('تسوّق الضيافة', 'Shop hosting'),
 'c3': ('تنجز شغلك', 'You get things done.'), 'c3s': ('ورق A4، أقلام ومستلزمات مكتبك', 'A4 paper, pencils and desk essentials'), 'c3c': ('تسوّق المكتب', 'Shop office'),
 'c4': ('وتختم بسفرة طازجة', 'And end with something fresh.'), 'c4s': ('حافظات طعام تحفظ أكلك', 'Food containers that keep it fresh'), 'c4c': ('تسوّق المطبخ', 'Shop kitchen'),
 'vid_t': ('القهوة على حرارتها', 'Coffee, kept warm.'), 'vid_s': ('ترامس أنيقة لكل مجلس وكل مكتب', 'Elegant flasks for every majlis and every desk'),
 'vid_c': ('تسوّق الترامس', 'Shop flasks'),
 'ss': ('تسوّق المشهد', 'Shop the scene'), 'sss': ('اضغط على أي منتج في الصورة', 'Tap any product in the picture'),
 'ss1': ('كشتة البر', 'Desert outing'), 'ss2': ('حفلة الميلاد', 'Birthday party'), 'tap': ('اضغط للتسوق', 'Tap to shop'),
 'more2': ('وباقي يومك', 'And the rest of your day'),
})

def cascade(L):
    src = Image.open(os.path.join(B, 'v3', 'raw', 'casc_hq.jpg')).convert('RGB')
    src = src.resize((3000, int(src.height * 3000 / src.width)), Image.LANCZOS); H = src.height // 4; out = []
    for i in range(4):
        im = src.crop((0, i * H, 3000, (i + 1) * H)).convert('RGBA'); side = 'left' if i % 2 == 0 else 'right'
        im = shade(im, side, 0.5, 0.30, (0, 0, 0)); ar = L == 'ar'; zone = 3000 * 0.33
        if side == 'left': xx = 190 + zone if ar else 190
        else: xx = 3000 - 190 if ar else 3000 - 190 - zone
        k = f'c{i + 1}'
        block(im, L, xx, int(H * 0.26), AN(L, f'{i + 1:02d}'), x(k, L), x(k + 's', L), x(k + 'c', L), tsize=175, maxw=zone, eye_col=GOLD)
        out.append(im)
    return out

def card(L, title, sub, button, W=1500, H=750):
    im = Image.new('RGBA', (W, H), CREAM); d = ImageDraw.Draw(im); ar = L == 'ar'
    gust(d, W, H * 0.75, 'left' if ar else 'right', [TEAL, GOLD, '#60A591'])
    im = grain(im, 5).convert('RGBA')
    block(im, L, W - 110 if ar else 110, 190, None, title, sub, button, tsize=112, fg=INK, btn_bg=TEAL, btn_fg='white', maxw=W * 0.62)
    return im

def video_poster(L, W=1500, H=750):
    im = fit(raw('thermos_poster'), (W, H), (0.5, 0.45)).convert('RGBA'); d = ImageDraw.Draw(im)
    cx, cy, r = W - 150, H - 150, 62   # play badge (the real tile shows Amazon's own play control)
    if L == 'ar': cx = 150
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 255, 255, 235))
    d.polygon([(cx - 18, cy - 28), (cx + 30, cy), (cx - 18, cy + 28)], fill=INK)
    return im

def scene_tile(L, scene, focus, title, size=(1500, 1500)):
    im = tile(L, scene, focus, title, size, link=x('tap', L)); d = ImageDraw.Draw(im); W = size[0]; ar = L == 'ar'
    t = x('ss', L) + '  +'; fs = 44; bw = tw(d, t, L, 'b', fs) + 70; bx = 90 if ar else W - 90 - bw
    d.rounded_rectangle((bx, 90, bx + bw, 90 + 92), 46, fill=(255, 255, 255, 240))
    d.text((bx + bw / 2, 90 + 48), t, font=font(L, 'b', fs), fill=INK, anchor='mm', **kw(L))
    return im

def home(L):
    P = Page(L, 'main', x('homep', L))
    P.fw(g.header(L), 'header_3000x600')
    P.fw(g.hero(L), 'hero_bgvideo_3000x1500', mobile=g.hero(L, mobile=True))
    P.fw(sec(L, 1, x('c0', L), x('c0s', L)), 'sec_cascade')
    P.n += 1; P.rows.append(('stack', [P._save(im, 'abcd'[i] + '_cascade_3000x1343') for i, im in enumerate(cascade(L))]))
    P.row([tile(L, *CAT['home']['m'], x('home', L), (1500, 750)), tile(L, *CAT['play']['m'], x('play', L), (1500, 750))], 'cats_medium')
    P.fw(sec(L, 2, x('s2', L), x('s2s', L)), 'sec_best')
    P.fw(banner(L, 'podium', (0.5, 0.5), x('bs_eye', L), x('bs_t', L), x('bs_s', L), x('bs_c', L), H=1200, strength=0.0,
                ext=True, zone=0.40, y=300, tsize=180), 'best_banner_3000x1200',
         mobile=mbanner(L, 'podium', 0.72, x('bs_eye', L), x('bs_t', L), x('bs_s', L), x('bs_c', L), strength=0))
    P.widget('Best Sellers widget (Amazon, live)')
    P.fw(sec(L, 3, x('s3', L), x('s3s', L)), 'sec_picks')
    vp, cd = video_poster(L), card(L, x('vid_t', L), x('vid_s', L), x('vid_c', L))
    P.row([cd, vp] if L == 'ar' else [vp, cd], 'picks_video_and_card')
    P.row([wtile(L, 'trolley_sq', 'trolley_sq', x('p_tr_w', L), x('p_tr', L), x('p_tr_c', L), cy=0.5, wsize=520),
           wtile(L, 'a4_b', 'a4', 'A4', x('t_a4', L), x('shop', L), wsize=900)], 'picks_large')
    P.row([tile(L, 'cups_sq', (0.5, 0.5), x('p_cu', L)), tile(L, 'bags_sq', (0.5, 0.5), x('p_ba', L)),
           tile(L, 'peeler_sq', (0.5, 0.5), x('p_pe', L)), tile(L, 'pencils_sq', (0.5, 0.5), x('p_pn', L))], 'picks_small')
    P.widget('Product grid: hand-picked ASINs')
    P.fw(sec(L, 4, x('ss', L), x('sss', L)), 'sec_scene')
    P.fw(banner(L, 'majlis_a', (0.5, 0.5), None, x('sh_t', L), x('sss', L), None, shade_col=(30, 18, 6), strength=0.62, y=560),
         'majlis_shoppable_3000x1500')
    P.row([scene_tile(L, 'kashta', (0.78, 0.7), x('ss1', L)), scene_tile(L, 'bday', (0.66, 0.5), x('ss2', L))], 'shoppable_large')
    P.fw(sec(L, 5, x('s4', L), x('s4s', L)), 'sec_gallery')
    picks = [('kitchen', (0.8, 0.7)), ('ram_b', (0.6, 0.55)), ('crafts', (0.7, 0.6)), ('gift_b', (0.7, 0.5)),
             ('fan_a', (0.5, 0.45)), ('homehero', (0.7, 0.85)), ('trolley_b', (0.7, 0.5)), ('school_a', (0.6, 0.6))]
    P.gallery([fit(raw(n), (1500, 750), f) for n, f in picks], 'gallery_1500x750')
    P.fw(g.kite_story(L), 'story_bgvideo_3000x1500', mobile=g.kite_story(L, mobile=True))
    P.fw(sec(L, 6, x('s5', L), x('s5s', L)), 'sec_deals')
    P.widget('Featured Deals widget (Amazon, live)')
    P.fw(banner(L, 'allprod', (0.5, 0.5), x('all_eye', L), x('all_t', L), x('all_s', L), x('all_c', L), H=1100, strength=0,
                fg=INK, eye_col=TEAL, btn_bg=TEAL, btn_fg='white', zone=0.28, y=290, tsize=170, ext=True), 'all_banner_3000x1100',
         mobile=mbanner(L, 'allprod', 0.62, x('all_eye', L), x('all_t', L), x('all_s', L), x('all_c', L), fg=INK, eye_col=TEAL,
                        btn_bg=TEAL, btn_fg='white', strength=0))
    P.fw(banner(L, 'ram_a', (0.5, 0.5), x('rm_eye', L), x('rm_t', L), x('rm_s', L), x('rm_c', L), shade_col=(6, 10, 30),
                strength=0.55, y=420), 'ramadan_3000x1500')
    P.fw(g.why(L), 'why_3000x560')
    return P.done()

SHOP = {'party': ('gift_a', (0.5, 0.5)), 'host': ('ram_b', (0.5, 0.5)), 'office': ('crafts', (0.5, 0.5)), 'home': ('homehero', (0.5, 0.5))}
def vary(L, p, idx):
    """Give each department page its own rhythm + a shop-the-scene banner where a second scene exists."""
    rows = p['rows']; k = p['slug']
    if k in SHOP:
        s, f = SHOP[k]
        im = banner(L, s, f, x('ss', L), x('sss', L), None, None, shade_col=(20, 20, 20), strength=0.45, y=560, tsize=150, eye_col='white')
        fn = f'{L}_{k}_90_shoppable_3000x1500.jpg'; im.convert('RGB').save(os.path.join(OUT, fn), quality=90, optimize=True)
        rows.insert(5, ('fw', [fn]))
    if idx % 2 == 1:   # variant B: feature split first, then the type tiles
        rows[2:5] = [rows[4], rows[2], rows[3]]
    return p

def pages(L):
    ps = v4.pages(L); ps[0] = home(L)
    import glob
    for f in glob.glob(os.path.join(OUT, f'{L}_main_*')):   # drop v4 home files that the new home did not rewrite
        if not any(os.path.basename(f) in r[1] for r in ps[0]['rows'] if r[0] != 'widget') and '_mobile' not in f: os.remove(f)
    for i in range(1, 7): ps[i] = vary(L, ps[i], i)
    return ps

if __name__ == '__main__':
    for L in (sys.argv[1:] or ['ar', 'en']):
        json.dump(pages(L), open(os.path.join(OUT, f'layout_{L}.json'), 'w'), ensure_ascii=False, indent=1)
    print('ok', len(os.listdir(OUT)))
