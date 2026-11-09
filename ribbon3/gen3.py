from PIL import Image, ImageDraw, ImageFont
import os, json
from three import three
F=lambda w,s: ImageFont.truetype(f'/home/claude/fonts/Tajawal-{w}.ttf', s)
S=2000; INK=(30,33,38); SUB=(98,102,110); ACC=(176,141,87); BG=(247,245,241)
COL=['Dark Brown','White','Ivory','Black','Red','Burgundy','Pink','Light Pink','Fuchsia','Purple','Lavender','Navy Blue','Royal Blue','Light Blue','Turquoise','Emerald Green','Mint Green','Gold','Silver','Champagne']
AR={'Dark Brown':'بني غامق','White':'أبيض','Ivory':'عاجي','Black':'أسود','Red':'أحمر','Burgundy':'عنابي','Pink':'وردي','Light Pink':'وردي فاتح','Fuchsia':'فوشي','Purple':'بنفسجي','Lavender':'لافندر','Navy Blue':'كحلي','Royal Blue':'أزرق ملكي','Light Blue':'أزرق فاتح','Turquoise':'تركوازي','Emerald Green':'أخضر زمردي','Mint Green':'أخضر نعناعي','Gold':'ذهبي','Silver':'فضي','Champagne':'شامبين'}
SIZES={'12':('1/2 Inch','نصف إنش'),'34':('3/4 Inch','ثلاثة أرباع إنش')}
def fit(im,bw,bh):
    im=im.copy(); im.thumbnail((bw,bh),Image.LANCZOS); return im
def ctext(d,y,t,f,fill):
    d.text(((S-d.textlength(t,font=f))/2,y),t,font=f,fill=fill)
def pack(c,sz,out):
    cv=Image.new('RGB',(S,S),BG); d=ImageDraw.Draw(cv)
    ctext(d,90,'HABBAA',F('Bold',46),ACC)
    ctext(d,160,'3 بكرات من نفس اللون',F('ExtraBold',110),INK)
    ctext(d,310,'Pack of 3 Rolls, Same Colour',F('Bold',64),SUB)
    d.rounded_rectangle((120,440,1880,1500),40,fill='white')
    r=fit(Image.open(f'three/{c.replace(" ","_")}.jpg'),1000,1000); cv.paste(r,((S-r.width)//2,470))
    # three badges
    for i,(n,a,e) in enumerate([('1','بكرة','Roll'),('2','بكرة','Roll'),('3','بكرة','Roll')]):
        x=300+i*500; d.ellipse((x,1560,x+180,1740),fill=ACC); ctext_x=x+90
        f=F('ExtraBold',100); w=d.textlength(n,font=f); d.text((x+90-w/2,1572),n,font=f,fill='white')
    t=f'{AR[c]} - {sz[1]} - 18 ياردة لكل بكرة'; ctext(d,1780,t,F('Bold',62),INK)
    t2=f'{c} - {sz[0]} - 18 Yards per Roll'; ctext(d,1870,t2,F('Medium',50),SUB)
    cv.save(out,quality=92)
def feats(c,sz,out):
    cv=Image.new('RGB',(S,S),BG); d=ImageDraw.Draw(cv)
    ctext(d,90,'HABBAA',F('Bold',46),ACC)
    ctext(d,160,'المميزات',F('ExtraBold',100),INK)
    ctext(d,295,f'شريطة ساتان {AR[c]}، 3 بكرات',F('Medium',56),SUB)
    d.rounded_rectangle((120,420,1880,1100),40,fill='white')
    r=fit(Image.open(f'three/{c.replace(" ","_")}.jpg'),900,660); cv.paste(r,((S-r.width)//2,760-r.height//2))
    items=[('3 بكرات','من نفس اللون في العبوة'),(f'{sz[1]}',' 18 ياردة لكل بكرة'),('تغليف الهدايا','الهدايا والورد وعلب الشوكولاتة'),('أشغال يدوية','فيونكات الشعر والبطاقات والخياطة')]
    for i,(a,b) in enumerate(items):
        x=1000-(i%2)*900+0; x=1020 if i%2==0 else 120; y=1180+(i//2)*370
        d.rounded_rectangle((x,y,x+860,y+330),30,fill='white')
        d.rectangle((x+800,y+60,x+810,y+125),fill=ACC)
        f=F('ExtraBold',62); d.text((x+770-d.textlength(a,font=f),y+50),a,font=f,fill=INK)
        f2=F('Medium',46); d.text((x+770-d.textlength(b,font=f2),y+160),b,font=f2,fill=SUB)
    cv.save(out,quality=92)
if __name__=='__main__':
    os.makedirs('out3',exist_ok=True); plan={}
    for c in COL:
        k=c.replace(' ','_')
        if not os.path.exists(f'three/{k}.jpg'): three(c,f'three/{k}.jpg')
        for s,sz in SIZES.items():
            fs=[f'out3/{k}_{s}_1.jpg',f'out3/{k}_{s}_2.jpg',f'out3/{k}_{s}_3.jpg']
            Image.open(f'three/{k}.jpg').save(fs[0],quality=92); pack(c,sz,fs[1]); feats(c,sz,fs[2])
            plan[f'{c}|{sz[0]}']=[os.path.basename(f) for f in fs]
    json.dump(plan,open('plan3.json','w'),indent=0); print(len(plan))
