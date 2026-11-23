import sys,subprocess,os
from PIL import Image
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','aplus','pro')
def o(im,psm='6'):
    im=im.convert('L');im=im.resize((im.width*2,im.height*2));im.save('/tmp/o.png')
    return ' '.join(subprocess.run(['tesseract','/tmp/o.png','-','-l','ara','--psm',psm],capture_output=True,text=True).stdout.split())
W=1464
for f in sys.argv[1:]:
    p=lambda k:Image.open(f'{D}/{f}-{k}-desktop.jpg')
    out=['##'+f]
    try: out.append('H: '+o(p('1-hero').crop((640,40,1420,540))))
    except: pass
    try: im=p('2-feat');out.append('F: '+o(im.crop((480,30,1420,190)))+' || '+' | '.join(o(im.crop((W-70-c*464-440,200+r*192,W-70-c*464-90,200+r*192+170))) for r in range(2) for c in range(2)))
    except: pass
    try: im=p('3-steps');out.append('S: '+o(im.crop((100,20,1364,110)))+' || '+' | '.join(o(im.crop((W-60-i*462-420,450,W-60-i*462,600))) for i in range(3)))
    except: pass
    try: im=p('4-uses');out.append('U: '+o(im.crop((100,20,1400,170)))+' || '+' | '.join(o(im.crop((W-70-i*342-300,176+330-70,W-70-i*342-16,176+330-16)),'7') for i in range(4))+' || '+o(im.crop((100,515,1400,580))))
    except: pass
    try: out.append('P: '+o(p('5-specs').crop((660,130,1420,600))))
    except: pass
    print('\n'.join(s[:330] for s in out))
