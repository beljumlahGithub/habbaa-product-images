import sys,subprocess,os
from PIL import Image
D=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','aplus','pro')
BOX={'hero':(600,40,1430,360),'feat':(470,0,1464,600),'steps':(0,440,1464,600),'uses':(0,0,1464,600),'specs':(640,0,1464,600)}
def o(im):
    im=im.convert('L');im=im.resize((im.width*2,im.height*2));im.save('/tmp/o.png')
    return ' '.join(subprocess.run(['tesseract','/tmp/o.png','-','-l','ara','--psm','6'],capture_output=True,text=True).stdout.split())
for f in sys.argv[1:]:
    print('##',f)
    for i,k in enumerate(['hero','feat','steps','uses','specs']):
        p=f'{D}/{f}-{i+1}-{k}-desktop.jpg'
        if os.path.exists(p): print(k.upper(),o(Image.open(p).crop(BOX[k]))[:300])
