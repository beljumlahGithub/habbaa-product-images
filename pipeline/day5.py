import os, sys, json, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('HB_FONTS', '/home/claude/habbaa-product-images/pipeline/fonts')
import aplus_lib as L
G='/home/claude/aplus5/gen/'; S='/home/claude/habbaa-product-images/store/src/'; O='/home/claude/aplus5/final/'
os.makedirs(O, exist_ok=True)
g=lambda n: G+n+'.png'; s=lambda n: S+n+'.jpg'
FAM={
 'd19-ribbon': dict(
   hero=(g('rib-hero1'), ['شرائط ساتان', 'تكمّل هديتك'], ['شريط ساتان رفيع بعرض ربع إنش بألوان متعددة', 'عبوة 9 ألوان أو 3 بكرات من نفس اللون']),
   uses=('لمسة أنيقة لكل مناسبة', [(g('rib-t0'),'تغليف الهدايا'),(g('rib-t1'),'باقات الورد'),(g('rib-t2'),'البطاقات والحرف اليدوية'),(g('rib-t3'),'توزيعات الأعراس والعيد')]),
   feat=(s('rib9_1'), 'ساتان ناعم ولامع', [('عرض ربع إنش','شريط رفيع للفيونكات الصغيرة والتفاصيل'),('9 ألوان في عبوة','أبيض وفضي وأسود وذهبي وأحمر وغيرها'),('3 بكرات بنفس اللون','لمن يحتاج كمية من لون واحد'),('ملمس ساتان لامع','يربط فيونكات أنيقة بسهولة')]),
   photo='pad', panel=True,
   alt=['شرائط ساتان HABBAA بجانب علب هدايا مغلفة','استخدامات شرائط الساتان من HABBAA للهدايا والحرف','مميزات شرائط الساتان من HABBAA بعرض ربع إنش']),
 'd19-home': dict(
   hero=(g('home-hero1'), ['أدوات صغيرة', 'تسهّل يومك'], ['مج ستيل بغطاء شفاف وبخاخ زيت للطبخ وعجلات لاصقة', 'وأعواد قطن ومنظف إلكترونيات للبيت والمكتب']),
   uses=('لكل ركن في البيت', [(s('cast2'),'عجلات لاصقة دوّارة'),(s('peel1'),'تقشير الخضار والفواكه'),(s('cc4'),'تنظيف الإلكترونيات'),(s('glv1'),'قفازات قطن للشغل')]),
   feat=(s('mug3'), 'مج ستيل للقهوة', [('ستانلس ستيل','أخف وأطول عمر من الزجاج'),('غطاء شفاف محكم','يقلل الانسكاب أثناء الحركة'),('سعة 360 و380 مل','لكوب القهوة أو الشاي اليومي'),('قاعدة خشب','تحمي الأسطح في الموديل الكحلي')]),
   photo='pad',
   alt=['مج HABBAA الستيل على رف المطبخ','استخدامات أدوات HABBAA المنزلية','مميزات مج HABBAA الستيل بغطاء شفاف']),
 'd19-party': dict(
   hero=(g('party-hero1'), ['فوانيس سماء', 'تضيء لحظتك'], ['فوانيس ورق أرز بيضاء قابلة للتحلل، عبوة 10 قطع', 'وبالونات مطاط أوف وايت ومنفاخ يدوي للزينة']),
   uses=('لمناسباتكم السعيدة', [(g('party-t1'),'حفلات الأعراس'),(s('lant1'),'فوانيس بيضاء'),(g('party-t0'),'أقواس البالونات'),(s('pump1'),'منفاخ يدوي')]),
   feat=(s('lant1'), 'فانوس ورقي بتوهج دافئ', [('ورق أرز','خفيف وقابل للتحلل'),('عبوة 10 قطع','تكفي لحظة جماعية'),('تجميع وإضاءة بسيطة','يطفو لعدة دقائق في السماء'),('اتبع إرشادات السلامة','والأنظمة المحلية قبل الإطلاق')]),
   photo='pad', panel=True,
   alt=['فوانيس سماء HABBAA البيضاء في سماء المساء','استخدامات فوانيس وبالونات HABBAA للمناسبات','مميزات فوانيس HABBAA الورقية']),
}
BLOCK=['مص','كس','لعن','بز','ثدي','علق','هور','جن','نيك','لسبو','فوهة']
def texts(c):
    t=c['hero'][1]+c['hero'][2]+[c['uses'][0]]+[l for _,l in c['uses'][1]]+[c['feat'][1]]
    for a,b in c['feat'][2]: t+=[a,b]
    return t+c['alt']
bad=[(k,b,t) for k,c in FAM.items() for t in texts(c) for b in BLOCK if b in re.sub(r'[\sً-ْ]','',t)]
if bad: print('BLOCKED',bad); sys.exit(1)
for k in sys.argv[1:] or list(FAM):
    c=FAM[k]
    L.hero(c['hero'][0],c['hero'][1],c['hero'][2],O+f'{k}-1-hero',panel=c.get('panel',False))
    L.uses(c['uses'][1],c['uses'][0],O+f'{k}-2-uses')
    L.features(c['feat'][0],c['feat'][1],c['feat'][2],O+f'{k}-3-feat',photo=c.get('photo',False))
    print('done',k)
json.dump({k:v['alt'] for k,v in FAM.items()},open(O+'alts.json','w'),ensure_ascii=False)
