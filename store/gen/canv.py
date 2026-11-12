from PIL import Image
import os, json
CUT='cut'
CROPS={'peeler':(0.62,0,1,1),'gloves':(0,0,0.42,0.48),'fan':(0,0,1,0.62)}
def load(n):
    im=Image.open(f'{CUT}/{n}.png').convert('RGBA')
    if n in CROPS:
        w,h=im.size;c=CROPS[n];im=im.crop((int(c[0]*w),int(c[1]*h),int(c[2]*w),int(c[3]*h)))
    return im.crop(im.getbbox())
def canvas(W,H,items):
    cv=Image.new('RGBA',(W,H),(255,255,255,255))
    for n,cx,by,hh in items:   # fractions: centre x, base y, height
        im=load(n);h=int(hh*H);w=int(im.width*h/im.height)
        cv.alpha_composite(im.resize((w,h),Image.LANCZOS),(int(cx*W-w/2),int(by*H-h)))
    return cv.convert('RGB')
S={
 'hero':(2560,1280,[('trolley',.36,.93,.62),('umbrella',.62,.93,.55),('basketball',.50,.95,.22),('thermos',.27,.95,.34),('cupstack',.73,.95,.22),('bags',.82,.93,.30)]),
 't1_morning':(1600,1600,[('thermos',.30,.80,.42),('glass',.58,.82,.16),('container',.78,.80,.18),('peeler',.55,.92,.17)]),
 't2_study':(1600,1600,[('a4',.40,.78,.20),('pencils',.70,.80,.40),('scissors',.55,.90,.22),('gluesticks',.25,.92,.15)]),
 't3_outing':(1600,1600,[('umbrella',.42,.86,.45),('fan',.70,.90,.16)]),
 't4_majlis':(2560,1280,[('tray',.50,.84,.13),('thermos',.40,.80,.33),('papercup',.50,.73,.12),('papercup',.55,.74,.12),('cupstack',.66,.86,.26)]),
 't5_night':(1600,1600,[('basket',.66,.88,.50)]),
 'c_party':(1600,1600,[('banner',.50,.30,.18),('cannon',.38,.88,.50),('ribbon',.66,.88,.20),('bags',.70,.70,.25)]),
 'c_pack':(2560,1280,[('bags',.62,.84,.55),('ribbon',.84,.90,.22)]),
 'c_cups':(1600,1600,[('cupstack',.44,.86,.40),('papercup',.70,.86,.28),('plasticcup',.82,.88,.15)]),
 'c_kitchen':(1600,1600,[('glass',.40,.82,.18),('container',.66,.80,.22),('peeler',.50,.92,.20)]),
 'c_home':(2560,1280,[('trolley',.58,.92,.70),('basket',.78,.92,.52)]),
 'c_clean':(1600,1600,[('gloves',.52,.84,.45)]),
 'c_station':(1600,1600,[('a4',.42,.82,.20),('pencils',.70,.84,.42),('scissors',.30,.90,.22)]),
 'c_toys':(2560,1280,[('basketball',.62,.92,.36),('kite',.84,.60,.50)]),
 'c_travel':(1600,1600,[('umbrella',.46,.88,.62),('fan',.78,.92,.22)]),
 'c_colors':(2560,1280,[('bags',.50,.92,.86)]),
}
if __name__=='__main__':
    os.makedirs('canv',exist_ok=True)
    for k,(W,H,it) in S.items(): canvas(W,H,it).save(f'canv/{k}.jpg',quality=93)
    print(len(S))
