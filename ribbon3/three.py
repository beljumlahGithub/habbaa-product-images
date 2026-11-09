from PIL import Image, ImageDraw, ImageFilter, ImageChops
import numpy as np, sys, os
from scipy import ndimage
def cut(path):
    im=Image.open(path).convert('RGB'); a=np.asarray(im).astype(int)
    nw=(a.min(axis=2)<238)|((a.max(axis=2)-a.min(axis=2))>12)
    # background = near-white connected to border
    bg=~nw
    lab,n=ndimage.label(bg)
    border=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))-{0}
    bgm=np.isin(lab,list(border))
    fg=~bgm
    fg=ndimage.binary_opening(fg,iterations=2); fg=ndimage.binary_fill_holes(fg)
    m=Image.fromarray((fg*255).astype('uint8')).filter(ImageFilter.GaussianBlur(1.2))
    rgba=im.copy(); rgba.putalpha(m)
    return rgba.crop(rgba.getbbox())
def three(c,out,S=2000):
    r=cut(f'col/{c.replace(" ","_")}.png' if c!='Dark Brown' else 'src/517e7CT75OL.jpg')
    w=int(S*0.58); r=r.resize((w,int(r.height*w/r.width)),Image.LANCZOS)
    cv=Image.new('RGB',(S,S),'white')
    sh=Image.new('L',(S,S),0)
    pos=[(int(S*0.07),int(S*0.20)),(int(S*0.35),int(S*0.20)),(int(S*0.21),int(S*0.47))]
    for (x,y) in pos:
        d=ImageDraw.Draw(sh); d.ellipse((x+20,y+r.height-40,x+r.width-20,y+r.height+40),fill=60)
    sh=sh.filter(ImageFilter.GaussianBlur(30))
    cv=Image.composite(Image.new('RGB',(S,S),(205,205,205)),cv,sh)
    for (x,y) in pos: cv.paste(r,(x,y),r)
    bb=ImageChops.difference(cv,Image.new('RGB',(S,S),'white')).getbbox()
    cv=cv.crop(bb); W=max(cv.size); f=Image.new('RGB',(int(W*1.28),int(W*1.28)),'white'); f.paste(cv,((f.width-cv.width)//2,(f.height-cv.height)//2))
    f.resize((S,S),Image.LANCZOS).save(out,quality=92)
if __name__=='__main__':
    for c in sys.argv[1:]: three(c,f'three/{c.replace(" ","_")}.jpg')
