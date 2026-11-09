import json
from gen3 import AR, SIZES
C={}; J=[]
R='https://raw.githubusercontent.com/beljumlahGithub/habbaa-product-images/main/ribbon3/'
for l in open('kids.txt').read().split('\n'):
    if not l.strip(): continue
    a,sku,s,c=l.split('|'); en,ar=SIZES[s]; car=AR[c]; k=c.replace(' ','_')
    C[a]={'en':{
     't':f'HABBAA Satin Ribbon {en} x 18 Yards, {c}, Pack of 3 Rolls in the Same Colour, Fabric Ribbon for Gift Wrapping, Hair Bows, Crafts, Sewing, Wedding and Eid Decorations',
     'b':[f'PACK OF 3 ROLLS: You receive 3 rolls of satin ribbon, all in the same {c} colour, not a single roll',
          f'SIZE: Each roll is {en} wide and 18 yards long, so the pack gives you 54 yards in total',
          'SMOOTH SATIN FINISH: Soft, shiny ribbon that ties into neat bows and adds an elegant finishing touch',
          'GIFT WRAPPING: Ideal for presents, chocolate boxes, flower bouquets, giveaways and Eid hampers',
          'CRAFTS AND DECOR: Use it for hair bows, cards, scrapbooking, sewing projects, weddings and party decorations'],
     'd':f'HABBAA {c} satin ribbon comes in a pack of 3 rolls, all in the same colour. Each roll is {en} wide and 18 yards long, giving 54 yards of ribbon in total. The smooth, shiny satin finish ties into neat bows and suits gift wrapping, chocolate boxes, flower bouquets, giveaways, hair bows, cards, sewing projects, weddings and Eid decorations. The pack contains 3 rolls of one colour, not a single roll.',
     'k':f'satin ribbon {c.lower()} ribbon gift wrapping ribbon 3 rolls ribbon pack {en.lower()} ribbon craft ribbon hair bow ribbon wedding ribbon eid decoration شريطة ساتان شرائط تغليف'},
     'ar':{
     't':f'شريطة ساتان HABBAA بعرض {ar} وطول 18 ياردة، لون {car}، عبوة 3 بكرات من نفس اللون لتغليف الهدايا والفيونكات والأشغال اليدوية وزينة الأعراس والعيد',
     'b':[f'عبوة من 3 بكرات: تحصل على 3 بكرات شريطة ساتان كلها بلون {car} نفسه، وليست بكرة واحدة',
          f'المقاس: عرض كل بكرة {ar} وطولها 18 ياردة، فيصبح مجموع العبوة 54 ياردة',
          'ملمس ساتان ناعم ولامع: شريطة ناعمة تُربط بسهولة على شكل فيونكة وتعطي لمسة أنيقة',
          'تغليف الهدايا: مناسبة للهدايا وعلب الشوكولاتة وباقات الورد والتوزيعات وسلال العيد',
          'أشغال يدوية وزينة: لفيونكات الشعر والبطاقات والخياطة وزينة الأعراس والحفلات'],
     'd':f'شريطة ساتان من HABBAA بلون {car} في عبوة من 3 بكرات كلها بنفس اللون. عرض كل بكرة {ar} وطولها 18 ياردة، أي 54 ياردة في العبوة كاملة. ملمسها الناعم واللامع يناسب تغليف الهدايا وعلب الشوكولاتة وباقات الورد والتوزيعات وفيونكات الشعر والبطاقات والخياطة وزينة الأعراس والعيد. العبوة تحتوي على 3 بكرات من لون واحد وليست بكرة واحدة.',
     'k':f'شريطة ساتان شريط ساتان {car} شرائط تغليف هدايا 3 بكرات شريطة فيونكة شريطة توزيعات زينة عيد زينة عرس satin ribbon'}}
    J.append(dict(a=a,sku=sku,imgs=[R+f'{k}_{s}_{i}.jpg' for i in (1,2,3)]))
json.dump(C,open('C3.json','w'),ensure_ascii=False,indent=1); json.dump(J,open('jobs3.json','w'),indent=1)
print(len(C))
bad=['مص','كس','لعن','بز','ثدي','علق','هور','جن','نيك','لسبو','فوهة']
for a,v in C.items():
    s=json.dumps(v['ar'],ensure_ascii=False).replace(' ','')
    h=[b for b in bad if b in s]
    if h: print(a,h)
