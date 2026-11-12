from PIL import Image, ImageDraw, ImageFont
import os, sys, glob
O='out2'; W=1500; G=10
def im(n): return Image.open(os.path.join(O,n)).convert('RGB')
def fw(n): i=im(n); return i.resize((W, int(i.height*W/i.width)))
def row_large_col(L, large, m1, m2):
    s=(W-G)//2; r=Image.new('RGB',(W,s),'white')
    a=im(large).resize((s,s)); b=im(m1).resize((s,(s-G)//2)); c=im(m2).resize((s,(s-G)//2))
    lx,cx=(s+G,0) if L=='ar' else (0,s+G)
    r.paste(a,(lx,0)); r.paste(b,(cx,0)); r.paste(c,(cx,(s-G)//2+G)); return r
def row_n(names, h=None):
    n=len(names); s=(W-G*(n-1))//n; hh=h or s
    r=Image.new('RGB',(W,hh),'white')
    for i,nm in enumerate(names): r.paste(im(nm).resize((s,hh)),(i*(s+G),0))
    return r
def widget(L):
    r=Image.new('RGB',(W,330),'white'); d=ImageDraw.Draw(r)
    f=ImageFont.truetype('fonts/SST-Medium.ttf',22)
    cuts=['trolley','basketball','cards','thermos','bags','umbrella']
    s=(W-60)//6
    for i,cn in enumerate(cuts):
        x=30+i*s; d.rounded_rectangle((x+6,10,x+s-6,320),12,outline='#dddddd',width=2)
        c=Image.open(f'cut/{cn}.png').convert('RGBA'); c=c.crop(c.getbbox()); c.thumbnail((s-60,170)); r.paste(c,(x+(s-c.width)//2,30),c)
        d.rounded_rectangle((x+30,250,x+s-30,290),20,fill='#FFD814')
    d.text((W//2,312),'[ Amazon best-seller widget: live products ]',font=f,fill='#888',anchor='mm')
    return r
def page(L):
    P=f'{L}_'; parts=[fw(P+'01_header_3000x600.jpg'),fw(P+'02_hero_3000x1500.jpg'),fw(P+'03_strip_day_3000x640.jpg'),
      row_large_col(L,P+'04a_t1_large_1500.jpg',P+'04b_t2_medium_1500x750.jpg',P+'04c_t3_medium_1500x750.jpg'),
      fw(P+'05_t4_majlis_shoppable_3000x1500.jpg'),
      row_n([P+'06a_t5_medium_1500x750.jpg',P+'06b_tomorrow_medium_1500x750.jpg'][::(-1 if L=='ar' else 1)],(W-G)//4),
      fw(P+'07_strip_corners_3000x460.jpg'),
      row_large_col(L,P+'08a_party_large_1500.jpg',P+'08b_pack_medium_1500x750.jpg',P+'08c_home_medium_1500x750.jpg'),
      row_n(sorted(glob.glob(f'{O}/{P}09*'))[::(-1 if L=='ar' else 1)] and [os.path.basename(x) for x in sorted(glob.glob(f'{O}/{P}09*'))][::(-1 if L=='ar' else 1)]),
      row_large_col(L,P+'10a_travel_large_1500.jpg',P+'10b_toys_medium_1500x750.jpg',P+'10c_care_medium_1500x750.jpg'),
      fw(P+'11_strip_best_3000x520.jpg'), widget(L),
      fw(P+'12_strip_occ_3000x460.jpg'),
      row_n([os.path.basename(x) for x in sorted(glob.glob(f'{O}/{P}13*'))][::(-1 if L=='ar' else 1)]),
      fw(P+'14_why_3000x760.jpg')]
    H=sum(p.height for p in parts)+G*len(parts)
    out=Image.new('RGB',(W,H),'white'); y=0
    for p in parts: out.paste(p,(0,y)); y+=p.height+G
    out.save(f'HABBAA_home_v2_{L}.jpg',quality=86); print(L,out.size)
for L in sys.argv[1:] or ['ar','en']: page(L)
