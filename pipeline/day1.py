import os, sys, json
sys.path.insert(0, os.path.dirname(__file__))
os.environ.setdefault('HB_FONTS', '/home/claude/fonts')
import aplus_lib as L
from PIL import Image

S = '/home/claude/aplus2/src/'
O = '/home/claude/aplus2/final/'
os.makedirs(O, exist_ok=True)

# square tile cut from a hero (for cups iced-coffee tile)
h = Image.open(S + 'cup-hero2.png').convert('RGB')
h.crop((0, 0, 672, 672)).save(S + 'cup-iced.png')

FAM = {
 'balloons': dict(
   hero=(S + 'bal-hero4.png', ['احتفالك يستاهل', 'لمعة ذهبية'],
         ['بالونات حروف وأرقام ذهبية بأحجام كبيرة', 'تكتب فيها الاسم أو العمر وتزيّن صورك']),
   uses=('لكل مناسبة حلوة', [(S + 'bal-bday.png', 'أعياد الميلاد'), (S + 'bal-grad.png', 'حفلات التخرج'),
                             (S + 'bal-love1.png', 'الملكة والخطوبة'), (S + 'bal-pump.png', 'تنفخها بسهولة')]),
   feat=(S + 'balloon-letter.jpg', 'تفاصيل تفرق في صورك',
         [('فويل معدني لامع', 'لون ذهبي موحّد يلمع في الصور'), ('حروف وأرقام', 'اختر الحرف أو الرقم اللي تبيه'),
          ('أحجام كبيرة', 'متوفرة بمقاسات 16 و32 و40 إنش'), ('هواء أو هيليوم', 'تنفخها بمنفاخ يدوي بكل سهولة')]),
   alt=['بالونات أرقام ذهبية كبيرة من HABBAA في صالة احتفال', 'استخدامات بالونات HABBAA الذهبية في المناسبات',
        'مميزات بالونات الحروف والأرقام الذهبية من HABBAA']),
 'cups': dict(
   hero=(S + 'cup-hero1.png', ['مشروبك البارد', 'بشكل أفخم'],
         ['أكواب بلاستيك بلون مدخّن نصف أسود', 'مع غطاء قبة يثبت بإحكام ويقلل الانسكاب']),
   uses=('يناسب كل مشروب بارد', [(S + 'cup-iced.png', 'القهوة المثلجة'), (S + 'cup-juice.png', 'العصيرات الطازجة'),
                                 (S + 'cup-smoothie.png', 'السموذي والميلك شيك'), (S + 'cup-cafe2.png', 'المقاهي والمحلات')]),
   feat=(S + 'cup2.jpg', 'جودة تليق بمشروبك',
         [('لون مدخّن أنيق', 'يبيّن المشروب بمظهر فخم'), ('غطاء قبة', 'مساحة للكريمة والإضافات فوق المشروب'),
          ('بلاستيك متين', 'مناسب للتقديم اليومي والمناسبات'), ('إغلاق محكم', 'الغطاء يثبت ويقلل الانسكاب أثناء النقل')]),
   alt=['أكواب HABBAA البلاستيكية نصف السوداء مع قهوة مثلجة', 'استخدامات أكواب HABBAA للمشروبات الباردة',
        'مميزات أكواب HABBAA المدخنة بغطاء قبة']),
 'towels': dict(
   hero=(S + 'tow-hero2.png', ['نعومة القطن', 'بعد كل استحمام'],
         ['مناشف حمّام بيضاء من القطن 100%', 'تمتص الرطوبة بسرعة وتجف أسرع']),
   uses=('لكل يوم ولكل ضيف', [(S + 'tow-rail.png', 'الحمّام اليومي'), (S + 'tow-bed.png', 'غرف الضيوف'),
                              (S + 'tow-gym.png', 'النادي والرياضة'), (S + 'tow-soft.png', 'نعومة تحسّها')]),
   feat=(S + 'tow-soft.png', 'قطن يدوم غسلة بعد غسلة',
         [('قطن 100%', 'ناعم على البشرة ومريح'), ('امتصاص سريع', 'ينشّف الرطوبة بسرعة'),
          ('يجف بسرعة', 'أسرع من المناشف التقليدية'), ('أبيض كلاسيكي', 'بحافة بسيطة تناسب أي حمّام')]),
   photo=True,
   alt=['مناشف HABBAA القطنية البيضاء على رف الحمام', 'استخدامات مناشف HABBAA في البيت والنادي',
        'مميزات مناشف HABBAA القطن سريعة الجفاف']),
 'candles': dict(
   hero=(S + 'can-hero2.png', ['شموع أرقام ذهبية', 'تكمّل فرحتك'],
         ['من 0 إلى 9 تركّب فيها أي عمر', 'بدون دخان ولا يسيل منها شمع على الكيكة']),
   uses=('شمعة لكل مناسبة', [(S + 'can-baby.png', 'يوم الميلاد الأول'), (S + 'can-cupcake.png', 'أعياد الميلاد'),
                             (S + 'can-grad.png', 'التخرج'), (S + 'can-anniv.png', 'ذكرى الزواج')]),
   feat=(S + 'candle-main.jpg', 'تفاصيل صغيرة تفرق',
         [('ذهبي لامع', 'لون فخم يبان في الصور'), ('بدون دخان', 'ولا يسيل منها شمع على الكيكة'),
          ('مقاس مناسب', 'ارتفاع الرقم 6 سم تقريبًا'), ('تغليف فردي', 'تصل سليمة وسهلة التخزين')]),
   alt=['شموع أرقام ذهبية من HABBAA على كيكة عيد ميلاد', 'استخدامات شموع الأرقام الذهبية من HABBAA',
        'مميزات شموع أرقام HABBAA الذهبية']),
}

BLOCK = ['مص', 'كس', 'لعن', 'بز']

def texts(cfg):
    t = cfg['hero'][1] + cfg['hero'][2] + [cfg['uses'][0]] + [l for _, l in cfg['uses'][1]] + [cfg['feat'][1]]
    for a, b in cfg['feat'][2]:
        t += [a, b]
    return t + cfg['alt']

bad = []
for k, c in FAM.items():
    for t in texts(c):
        for b in BLOCK:
            if b in t.replace(' ', ''):
                bad.append((k, b, t))
if bad:
    print('BLOCKED', bad); sys.exit(1)

if __name__ == '__main__':
    only = sys.argv[1:] or list(FAM)
    for k in only:
        c = FAM[k]
        L.hero(c['hero'][0], c['hero'][1], c['hero'][2], O + f'{k}-1-hero')
        L.uses(c['uses'][1], c['uses'][0], O + f'{k}-2-uses')
        L.features(c['feat'][0], c['feat'][1], c['feat'][2], O + f'{k}-3-feat', photo=c.get('photo', False))
        print('done', k)
    json.dump({k: v['alt'] for k, v in FAM.items()}, open(O + 'alts.json', 'w'), ensure_ascii=False)
