import json,re
D=json.load(open('data.json'))
COL={'كحلي':'Navy','أبيض':'White','أزرق':'Blue','أسود':'Black','أحمر':'Red','أخضر':'Green','بيج':'Beige','موف':'Mauve','فضي':'Silver','عنابي':'Burgundy','جملي':'Camel','بني':'Brown','بني داكن':'Dark Brown','بني فاتح':'Light Brown','بيج كرافت':'Kraft Beige','بيج وفلين':'Beige and Cork','فلين وأبيض':'Cork and White','بيج لامع':'Shiny Beige','بيج مع فلين':'Beige with Cork','أبيض بحافة كحلي':'White with Navy Brim','أبيض بحافة زرقاء':'White with Blue Brim','أبيض بحافة عنابي':'White with Burgundy Brim'}
def color(s):
    last=D[s]['t'].split('،')[-1].strip().replace('بلمسة ','')
    return COL.get(last,'')
def pack(s):
    m=re.search(r'محتوى العبوة\s*:\s*([^.]+)',' '.join(D[s]['b'])); q=m.group(1).strip() if m else ''
    n=re.search(r'(\d+)',q); return int(n.group(1)) if n else 1
GIFT='Great for corporate gifts, events, schools and giveaways; the plain surface can be printed with your logo'
E={}
def put(s,t,b,d,k): E[s]={'t':t[:199],'b':b,'d':d,'k':k[:240]}
for s in D:
    c=color(s); n=pack(s)
    mm=re.search(r'-(\d)PC$',s)
    if mm: n=int(mm.group(1))
    if s.startswith('HABBAA-CAP-'):
        put(s,f'HABBAA Plain Baseball Cap for Men and Women, Cotton 6 Panel Cap with Air Vents and Adjustable Strap, {c}',
         ['SOFT BREATHABLE COTTON: Plain cotton baseball cap that lets air through, comfortable for everyday wear and hot summer days',
          '6 PANEL STRUCTURED DESIGN: Keeps its shape, with a matching top button and neat double stitching',
          'EMBROIDERED AIR VENTS: Help air flow and reduce sweat while walking, running and doing sports',
          'CURVED FRONT BRIM: Shades the eyes and face from the sun and gives a sporty look',
          'ONE ADJUSTABLE SIZE: Fits most men and women; no logo, ideal for embroidery or printing for companies, teams and events. Package: 1 cap'],
         f'The HABBAA plain baseball cap is made of soft cotton with a classic 6 panel build that holds its shape. Embroidered vents keep air moving, the curved brim blocks the sun, and the adjustable back fits most head sizes. With no logo, it is easy to match with casual and sports outfits and ready for embroidery or printing for companies, teams and events. Colour: {c}. Package contents: 1 cap.',
         'hat cap baseball cotton plain blank men women sports summer sun running gym golf travel embroidery printing logo team uniform')
    elif s.startswith('HABBAA-CAP2'):
        put(s,f'HABBAA White Satin Baseball Cap with Coloured Brim for Men and Women, Adjustable Hook and Loop Sports Cap, Printable, {c}',
         ['TWO TONE DESIGN: White satin crown with a coloured front brim for a sporty, eye catching look',
          'SOFT SATIN FABRIC: Smooth feel with a light sheen, lightweight and comfortable for daily wear and summer',
          'ADJUSTABLE BACK CLOSURE: Hook and loop strap fits most head sizes for men and women',
          'CURVED FRONT BRIM: Protects the eyes and face from the sun while walking, playing sports and travelling',
          'MADE FOR PRINTING: The white front panel is ideal for printing logos for companies, teams, schools and events. Package: 1 cap'],
         f'HABBAA two tone baseball cap with a white satin crown and a {c.split("with ")[-1].lower()} front brim. Light and soft, with an adjustable hook and loop back that fits most men and women. The plain white front is ready for printing company, team and event logos. Package contents: 1 cap.',
         'cap hat baseball satin two tone white sports snapback adjustable men women summer printing logo event team school uniform')
    elif s.startswith('HABBAA-PIN') or s.startswith('HABBAA-BADGE'):
        t=D[s]['t']; sz=(re.search(r'([\d.]+(?:×[\d.]+)?) سم',t) or [None,''])[1].replace('×','x')
        if 'BADGE' in s:
            put(s,f'HABBAA Blank Round Magnetic Badge {sz} cm, White Stainless Steel Name Badge, Printable for Logo or Employee Name',
             [f'READY TO CUSTOMISE: Plain white round face, {sz} cm diameter, for printing a company logo, employee name or event design',
              'MAGNETIC BACK, NO PIN: Holds on shirts, thobes and abayas with a magnet, without making holes in the fabric',
              'STAINLESS STEEL: Rust resistant metal body with a smooth, clean finish',
              'FOR STAFF AND EVENTS: Name badges for companies, conferences, exhibitions, schools and campaigns',
              'Package: 1 magnetic badge'],
             f'HABBAA blank round badge with a plain white face, {sz} cm in diameter, made of stainless steel with a magnetic back. No pin and no holes in your shirt, thobe or abaya. The blank face is ready for printing, making it a practical choice for staff name badges, conferences, exhibitions, school events and corporate promotions. Package contents: 1 badge.',
             'name badge magnetic blank round white printable logo employee staff conference exhibition event button pin brooch')
            continue
        kind={'MAP':'Saudi Map','FLAG':'Saudi Flag','RECT':'Rectangle Flag','2FLAG':'Double Flag','2FLAGB':'Double Flag'}[s.split('-')[2]]
        if 'MAP-WHT' in s: col='White with Gold Frame'
        elif 'FLAG-SLV' in s: col='Green with Silver Frame'
        elif s.endswith('BRN'): col='Brown with Gold Frame'
        elif s.endswith('2FLAGB-GLD'): col='Gold'
        else: col='Green with Gold Frame'
        frame='silver' if 'Silver' in col else 'gold'
        put(s,f'HABBAA {kind} Magnetic Brooch, {col} {sz} cm, Lapel Pin for Thobe, Shemagh and Abaya, National Day Gift',
         [f'ELEGANT NATIONAL DESIGN: {kind} brooch in {col.lower()}, a proud and classic touch for your thobe, jacket or abaya',
          'MAGNET, NO PIN: Strong magnetic back keeps your thobe, shemagh and abaya free of holes; easy to put on and take off',
          f'DURABLE METAL: Iron body with glossy enamel and a polished {frame} frame, about {sz} cm',
          'LIGHT AND COMFORTABLE: Only about 3 g, suitable for daily wear, formal occasions and national events',
          'GREAT GIFT: For Saudi National Day, Founding Day, graduations and events, for men and women. Package: 1 brooch'],
         f'HABBAA {kind.lower()} brooch, {col.lower()}, made of iron with glossy enamel and a polished metal frame, about {sz} cm. The strong magnet back holds it on a thobe, shemagh, jacket, abaya or bag without piercing the fabric. Light enough for everyday wear and a fitting gift for National Day, Founding Day, graduations and formal events. Package contents: 1 brooch.',
         'saudi national day brooch pin badge magnet flag map lapel thobe shemagh abaya founding day gift men women green gold patriotic')
    elif re.match(r'HABBAA-(M|T)\d',s):
        t=D[s]['t']; ml=re.search(r'(\d+) مل',t).group(1)
        f=s.split('-')[1]
        name={'M360WB':'Steel Mug with Wooden Base and Clear Lid','M360S':'Steel Mug with Steel Base and Lid','M350':'Steel Mug with Lid','M450':'Steel Mug with Lid','M380':'Steel Mug with Clear Lid','M420':'Steel Mug with Slide Lid','M430C':'Steel Tumbler with Cork Base and Clear Lid','T600':'Steel Tumbler with Steel Base and Lid','M360W':'Glossy Steel Mug with Wooden Base and Clear Lid','M300S':'Steel Mug with Straw, Wooden Base and Clear Lid','T600C':'Steel Tumbler with Cork Base and Clear Lid'}[f]
        b4={'M360WB':'WOODEN BASE: Protects surfaces and adds a natural touch; plain modern design for men and women','M360W':'WOODEN BASE: Protects surfaces and adds a natural touch; plain modern design for men and women','M300S':'WOODEN BASE: Protects surfaces and adds a natural touch; plain modern design for men and women','M360S':'SHINY STEEL BASE: Adds a premium look and extra durability; plain modern design for men and women','T600':'SHINY STEEL BASE: Adds a premium look and extra durability; plain modern design for men and women','M430C':'NATURAL CORK BASE: Non slip and protects the table; plain modern design for men and women','T600C':'NATURAL CORK BASE: Non slip and protects the table; plain modern design for men and women'}.get(f,'PLAIN MODERN DESIGN: A clean solid colour for men and women that suits any desk or car')
        b3='CLEAR LID WITH STEEL STRAW: Reduces spills on the move and makes drinking cold and hot drinks easy' if f=='M300S' else 'TIGHT, EASY OPEN LID: Reduces spills on the move and keeps your drink clean in the car and at work'
        put(s,f'HABBAA {name} {ml}ml, Travel Coffee Mug for Office and Car, Hot and Cold Drinks, {c}',
         [f'{ml} ML CAPACITY: The right size for your daily coffee or tea at home, in the office or in the car',
          'DURABLE STAINLESS STEEL: Rust resistant, break resistant metal body, lighter and longer lasting than glass or ceramic',
          b3,b4,
          'PRINTABLE GIFT: '+GIFT+'. Hand wash only, not for microwave. Package: 1 mug with lid'],
         f'HABBAA {name.lower()}, {ml} ml, made of rust resistant stainless steel with a lid that reduces spills on the go. A plain modern design for daily use at home, at the office, in the car or at university, for coffee, tea, juice and cold drinks. A good choice for staff and client gifts, and the plain surface can be printed with a company logo. Hand wash recommended; do not microwave. Colour: {c}. Package contents: 1 mug with lid.',
         f'coffee mug travel tumbler thermos stainless steel insulated cup lid office car {ml}ml tea hot cold drinks gift corporate printable logo reusable')
    elif re.match(r'HABBAA-B\d',s):
        t=D[s]['t']; ml=re.search(r'(\d+) مل',t).group(1); f=s.split('-')[1]
        name={'B400H':'Steel Water Bottle with Wooden Lid and Handle','B600C':'Steel Water Bottle with Wooden Lid and Carabiner','B500S':'Steel Water Bottle with Metal Lid and Steel Base','B500W':'Steel Water Bottle with Wooden Lid, Handle and Wooden Base'}[f]
        b3={'B400H':'WOODEN LID WITH HANDLE: Natural looking lid with a comfortable carry handle','B500W':'WOODEN LID WITH HANDLE: Natural looking lid with a comfortable carry handle','B600C':'WOODEN LID WITH CARABINER: Metal carabiner clip to hang it on a bag or belt','B500S':'STEEL SCREW LID AND STEEL BASE: A premium shiny look with extra durability'}[f]
        put(s,f'HABBAA {name} {ml}ml, Sports Water Bottle for Gym, School and Trips, {c}',
         [f'{ml} ML CAPACITY: A practical size for drinking water all day at the gym, school, work and on trips',
          'DURABLE STAINLESS STEEL: Rust and break resistant metal body, stronger and longer lasting than plastic bottles',b3,
          'PLAIN MODERN DESIGN: A smart solid colour for men, women and students, easy to carry in a bag or car',
          'PRINTABLE GIFT: '+GIFT+'. Package: 1 bottle'],
         f'HABBAA {name.lower()}, {ml} ml, made of durable stainless steel for daily water at the gym, school, office and on trips. Plain modern design for men, women and students. A good corporate and event gift, and the plain surface can be printed with a logo. Colour: {c}. Package contents: 1 bottle.',
         f'water bottle stainless steel sports gym school travel {ml}ml reusable metal flask kids adults gift corporate printable logo hiking')
    elif 'REEL-HOLDER' in s:
        put(s,f'HABBAA Hard Plastic ID Card Holder 10.5 x 6.3 cm, Vertical Badge Holder with Lanyard Slot and Thumb Push Slot, {c}',
         ['PROTECTS YOUR CARD: Rigid plastic case keeps staff and ID cards safe from bending, scratches and daily wear',
          '10.5 x 6.3 CM: Fits standard credit card size IDs, vertical layout keeps photo and name visible',
          'THUMB PUSH SLOT: Push the card out with your finger to tap it on an access reader without removing the holder',
          'TOP HANGING SLOT: Works with retractable badge reels, neck lanyards and snap clips',
          'FOR OFFICES, SCHOOLS AND EVENTS: Practical for staff, students, visitors and conferences. Package: 1 card holder'],
         f'HABBAA vertical ID card holder made of hard plastic, 10.5 x 6.3 cm, for standard size cards. A thumb slot on the back pushes the card out for access readers, and a top slot fits badge reels and lanyards. Practical for companies, schools, hospitals and events. Colour: {c}. Package contents: 1 card holder.',
         'id card holder badge holder hard plastic vertical employee staff card case lanyard reel office school hospital access card protector')
    elif 'REEL' in s:
        shape='Round' if 'ROUND' in s else 'Square'
        put(s,f'HABBAA {shape} Retractable Badge Reel with 100 cm Pull Cord, ID Card Holder Clip for Offices, Hospitals and Schools, {c}',
         ['RETRACTABLE CORD: Pull the card to tap it on an access reader and it returns on its own, up to 100 cm long',
          f'SMALL {shape.upper()} REEL (3.2 CM): Light and neat, clips onto a belt, pocket or bag strap',
          'SNAP STRAP: Clear strap with a metal snap holds the card firmly and opens easily to change cards',
          'FOR DAILY WORK: For staff, nurses, doctors, students, supervisors, security teams and exhibitions',
          'FOR COMPANIES AND GIVEAWAYS: A practical choice for staff cards, events and conferences. Package: 1 badge reel'],
         f'HABBAA {shape.lower()} retractable badge reel with a pull cord of up to 100 cm and a clear snap strap for ID cards. The small 3.2 cm reel clips to a belt, pocket or bag strap. Made for offices, hospitals, schools and events. Colour: {c}. Package contents: 1 badge reel.',
         'badge reel retractable id card holder clip lanyard yoyo employee nurse doctor staff office hospital school access card pull cord')
    elif 'PEN-' in s:
        click='CLICK' in s; sz='147 x 11 mm' if click else '140 x 11 mm'
        put(s,f'HABBAA {"Click" if click else "Twist"} Ballpoint Pen, White with {c} Accent, Blue Ink {sz}, Promotional Pen for Office and School, Printable Logo',
         ['SMOOTH BLUE INK: Clear, easy writing for notes, signatures and daily use',
          'CLICK DESIGN: One click opens and closes the pen, no cap to lose, with a coloured pocket clip' if click else 'TWIST DESIGN: Twist the top to extend or retract the tip, with a pocket clip and shiny metal tip',
          f'{sz.upper()}: Light and comfortable to hold for long writing',
          'PRINTABLE WHITE BARREL: Ideal for printing a company logo or event name by screen or UV printing',
          'FOR OFFICES AND GIVEAWAYS: For companies, hotels, exhibitions, conferences and schools. Package: 1 pen'],
         f'HABBAA white {"click" if click else "twist"} ballpoint pen with blue ink and a {c.lower()} accent, {sz}. Light, comfortable and ready for logo printing on the white barrel. A practical promotional pen for offices, hotels, exhibitions and schools. Package contents: 1 pen.',
         'ballpoint pen promotional pen blue ink white printable logo office school hotel conference giveaway click pen twist pen stationery')
    elif 'BALLOON' in s:
        put(s,'HABBAA Plain White Balloons, 120 Pack Latex Balloons for Party, Graduation, Wedding, Baby Shower and Birthday Decorations',
         ['120 BALLOONS: Enough to decorate parties, halls, balloon arches and walkways',
          'CLASSIC PLAIN WHITE: Matches any colour scheme, great for weddings, graduations and baby showers',
          'FLEXIBLE LATEX: About 2.8 g per balloon, easy to inflate by mouth or pump',
          'PRINTABLE: The plain white surface can be printed with a logo or message for companies and events',
          'WARNING: Not suitable for children under 8; uninflated or broken balloons can cause choking. Use with adult supervision. Package: 120 balloons'],
         'HABBAA plain white latex balloons, pack of 120, for decorating birthdays, weddings, graduations, baby showers and corporate events. Easy to inflate and suitable for balloon arches and garlands. Warning: choking hazard, not for children under 8. Package contents: 120 balloons.',
         'balloons white latex party decoration birthday wedding graduation baby shower arch garland helium bulk 120 pack event')
    elif 'BAG-' in s:
        t=D[s]['t']; dims='38 x 41 cm' if 'CRK' in s else '31 x 40 cm'
        mat='Cotton Canvas Drawstring Bag with Cork Base' if 'CRK' in s else ('Shiny Polyester Drawstring Bag with Reinforced Corners' if 'BEGS' in s else 'Polyester Drawstring Bag with Reinforced Corners' if ('RED' in s or '-BEG-' in s) else 'Shiny Polyester Drawstring Bag' if 'WHT' in s else 'Polyester Drawstring Bag')
        pk=f', Pack of {n}' if n>1 else ''
        put(s,f'HABBAA {mat} {dims}{pk}, Gym, Sports, Shoe and School Bag for Men and Women, {c}',
         ['LIGHT AND PRACTICAL: Light, durable fabric that folds flat and carries on your back with two cords that also close it' if 'CRK' not in s else 'LIGHT AND PRACTICAL: Sturdy cotton canvas with a natural cork base, carried on your back with two cords that also close it',
          f'{dims.upper()}: Fits gym clothes, a towel, shoes and a water bottle for everyday use',
          'QUICK DRAWSTRING CLOSE: Pull both cords to close the bag and keep your things from falling out',
          'MANY USES: Gym, swimming, school, trips, beach and camping, and for organising shoes and clothes when travelling',
          f'FOR GIVEAWAYS AND PRINTING: An affordable gift for events, companies and schools; the plain surface takes a logo. Package: {n} bag{"s" if n>1 else ""}'],
         f'HABBAA {mat.lower()}, {dims}, with two drawstring cords for carrying on the back and quick closing. Light and foldable, it holds gym clothes, a towel, shoes and a water bottle. Suitable for the gym, swimming, school, trips, beach and travel, and an affordable printable giveaway for events, companies and schools. Colour: {c}. Package contents: {n} bag{"s" if n>1 else ""}.',
         'drawstring bag gym bag backpack sports bag shoe bag string bag swimming school travel beach polyester bulk giveaway printable logo event')
    elif 'NB-' in s:
        t=D[s]['t']; sh=(re.search(r'(\d+) ورقة',t) or [0,'100'])[1]
        f=s.split('-')[2]
        name={'A5PU':'A5 Notebook with PU Leather Cover, Elastic Band and Pen Holder','A5PU2T':'A5 Notebook with Two Tone PU Leather Cover, Elastic Band and Pen Holder','A5KR':'A5 Notebook with Textured Kraft PU Leather Cover and Elastic Band','ECO':'Eco Friendly Spiral Notebook with Pen and Sticky Notes','SPK':'Eco Friendly Kraft Cover Spiral Notebook with Pen and Sticky Notes','A6':'A6 Pocket Notebook with Elastic Band and Pen Holder','SET':'A5 Notebook Gift Set with Linen and Cork Cover and Pen in Gift Box','CORKT':'A5 Notebook with Natural Cork Cover and Elastic Band','CORKB':'A5 Notebook with PU Leather and Natural Cork Cover and Elastic Band'}[f]
        size={'A6':'A6 (14.8 x 10.5 cm)','ECO':'18 x 15 cm','SPK':'18 x 15 cm'}.get(f,'A5 (21 x 14.8 cm)')
        b3=D[s]['b'][2]
        feat={'A5PU':'PREMIUM PU LEATHER COVER: Soft touch hard cover that protects the pages, with an elastic band and side pen holder','A5PU2T':'TWO TONE PU LEATHER COVER: Textured premium hard cover with an elastic band and side pen holder','A5KR':'TEXTURED KRAFT PU COVER: Simple, elegant look with an elastic band, pen holder and personal info page','ECO':'STICKY NOTES AND PEN: Includes coloured sticky notes and page flags, with a pen attached to the side','SPK':'ECO KRAFT COVER WITH PEN: Recycling symbol cover, attached pen, coloured sticky notes and page flags','A6':'POCKET SIZE: Small and light, fits a thobe or jacket pocket, with an elastic band and pen holder','SET':'READY GIFT SET: A5 notebook in linen and cork with a cork pen, in an elegant kraft gift box','CORKT':'NATURAL CORK DESIGN: Cork top and PU bottom, with an elastic band, pen holder and personal info page','CORKB':'NATURAL CORK DESIGN: Cork bottom and beige PU leather top, with an elastic band, pen holder and personal info page'}[f]
        pkg='1 notebook with pen' if f in ('ECO','SPK','SET') else '1 notebook'
        put(s,f'HABBAA {name}, {sh} Sheets 70 gsm, Notepad for Office, University and School, {c}',
         [f'{sh} SHEETS, 70 GSM: Smooth, thick paper that limits ink bleed, for notes, ideas and daily tasks',
          f'SIZE {size.upper()}: Easy to carry in a bag to the office, university and meetings',feat,
          'MANY USES: Notes, meetings, lectures, journaling and planning',
          f'PRINTABLE GIFT: Great for staff, client and graduation gifts; the cover can be printed or engraved with a logo. Package: {pkg}'],
         f'HABBAA {name.lower()}, {sh} sheets of 70 gsm paper, size {size}. Made for everyday notes at the office, university, school and in meetings, and a smart gift for staff, clients and graduates, with a cover that can be printed or engraved with a company logo. Colour: {c}. Package contents: {pkg}.',
         'notebook notepad journal diary planner a5 a6 office university school stationery gift corporate printable logo writing pad ruled')
miss=[s for s in D if s not in E]; print('missing',miss)
for s,v in E.items():
    assert len(v['t'])<=200 and all(len(x)<=500 for x in v['b']),s
json.dump(E,open('en.json','w'),ensure_ascii=False,indent=0)
for s in ['HABBAA-CAP2-19000-063','HABBAA-PIN-2FLAGB-GLD','HABBAA-BAG-BEGS-2PC','HABBAA-NB-SPK-19050-115','HABBAA-B600C-19030-150']: print(E[s]['t'])
