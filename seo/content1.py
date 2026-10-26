# -*- coding: utf-8 -*-
# HABBAA listing SEO content — part 1 (families 1-10)
# Each entry: asin -> dict(en=dict(t,b,d,k), ar=dict(t,b,d,k))
C = {}

def put(asin, t_en, t_ar, b_en, b_ar, d_en, d_ar, k_en, k_ar):
    C[asin] = dict(en=dict(t=t_en, b=b_en, d=d_en, k=k_en), ar=dict(t=t_ar, b=b_ar, d=d_ar, k=k_ar))

# ---------------- 1. Braided charging cables ----------------
CAB_B_EN = [
    "BRAIDED NYLON JACKET: The woven nylon outer layer resists tangling, fraying and daily bending, so the cable stays neat in your bag, car or desk drawer and lasts much longer than standard PVC cables",
    "FAST CHARGING AND DATA SYNC: Charges your phone or tablet quickly and transfers photos, videos and files between your device and computer at stable speed for everyday use at home or work",
    "REINFORCED CONNECTORS: Strong aluminium connector heads and flexible strain relief protect the weakest point of the cable where it usually breaks, giving reliable connection plug after plug",
    "WIDE COMPATIBILITY: Works with most Android smartphones, tablets, power banks, wireless earbuds and other devices that use this port; check your device port before ordering",
    "PRACTICAL LENGTH FOR DAILY USE: A comfortable length for charging on the bed, sofa, office desk or in the car, so you can keep using your phone while it charges",
]
CAB_B_AR = [
    "غلاف نايلون مضفر: الطبقة الخارجية المنسوجة تقاوم التشابك والتقطع والثني اليومي، فيبقى الكيبل مرتب في الشنطة أو السيارة أو درج المكتب ويدوم أطول من الكيبلات العادية",
    "شحن سريع ونقل بيانات: يشحن جوالك أو جهازك اللوحي بسرعة وينقل الصور والفيديوهات والملفات بين جهازك والكمبيوتر بسرعة ثابتة للاستخدام اليومي في البيت أو الدوام",
    "رؤوس توصيل معززة: رؤوس قوية ونقطة اتصال مرنة تحمي أضعف جزء في الكيبل اللي ينكسر عادة، فتحصل على اتصال ثابت مع كل استخدام",
    "توافق واسع: يناسب أغلب جوالات أندرويد والأجهزة اللوحية والباور بانك والسماعات اللاسلكية والأجهزة اللي تستخدم نفس المنفذ، تأكد من نوع منفذ جهازك قبل الطلب",
    "طول عملي للاستخدام اليومي: طول مريح للشحن على السرير أو الكنب أو مكتب الدوام أو في السيارة، فتقدر تستخدم جوالك وهو يشحن بدون إزعاج",
]
CAB_D_EN = ("HABBAA braided charging cables are made for people who are tired of replacing weak cables every few weeks. "
    "The nylon braided jacket protects the inner wires from bending, pulling and daily wear, while the reinforced connector heads keep a firm and stable fit in your device port. "
    "Use it to charge your phone overnight by the bed, at the office desk, in the car or with your power bank when you are travelling. "
    "Besides charging, the cable supports data transfer so you can move photos, videos and documents between your phone and laptop. "
    "The tangle free design makes it easy to roll up and carry in your bag. "
    "Compatible with most Android smartphones, tablets and accessories that use the same connector type. "
    "Package contents: 1 x HABBAA braided cable. Choose the length and connector type that suits your device and keep a spare in the car and the office.")
CAB_D_AR = ("كيبلات هبة HABBAA المضفرة مصممة للي تعب من تغيير الكيبلات الضعيفة كل كم أسبوع. "
    "الغلاف النايلون المضفر يحمي الأسلاك الداخلية من الثني والشد والاستخدام اليومي، ورؤوس التوصيل المعززة تثبت بإحكام في منفذ جهازك. "
    "استخدمه لشحن جوالك طول الليل جنب السرير أو على مكتب الدوام أو في السيارة أو مع الباور بانك وقت السفر. "
    "وغير الشحن، الكيبل يدعم نقل البيانات فتقدر تنقل الصور والفيديوهات والملفات بين جوالك واللابتوب. "
    "تصميمه ما يتشابك فيسهل لفه وحمله في الشنطة. "
    "يناسب أغلب جوالات أندرويد والأجهزة اللوحية والملحقات اللي تستخدم نفس نوع المنفذ. "
    "محتوى العبوة: كيبل مضفر واحد من هبة HABBAA. اختر الطول ونوع المنفذ المناسب لجهازك وخل واحد احتياط في السيارة والدوام.")
CAB_K_EN = "charger cord phone charging wire usb c type c android fast charge data cable car charger long cable nylon braided"
CAB_K_AR = "شاحن سلك جوال كيبل تايب سي شحن سريع اندرويد سلك شاحن طويل كيبل سيارة نقل بيانات"

cab = {
 "B0FVYHBF5T": ("HABBAA USB-A to Type-C Braided Charging Cable 1.8m, Fast Charging and Data Sync Nylon Charger Cord for Android Phones, Tablets and USB-C Devices, Grey",
                "كيبل شحن مضفر من USB-A إلى تايب سي من هبة HABBAA بطول 1.8 متر، سلك شاحن نايلون للشحن السريع ونقل البيانات لجوالات أندرويد والأجهزة اللوحية وأجهزة USB-C، رمادي",
                ("Supports up to 3A fast charging with a 1.8 metre length, ideal when the socket is far from your bed or sofa", "يدعم شحن سريع حتى 3 أمبير بطول 1.8 متر، مناسب إذا كان الفيش بعيد عن السرير أو الكنب")),
 "B0FVYHQTSF": ("HABBAA Braided Type-C USB Cable 1.2m, Fast Charging and Data Sync Anti-Bend Nylon Charger Cable for Android Phones, Tablets and USB-C Devices",
                "كيبل USB تايب سي مضفر من هبة HABBAA بطول 1.2 متر، سلك شاحن نايلون مقاوم للثني للشحن السريع ونقل البيانات لجوالات أندرويد والأجهزة اللوحية وأجهزة USB-C",
                ("A 1.2 metre anti-bend design that fits nicely on the desk, in the car and in your travel bag", "تصميم مقاوم للثني بطول 1.2 متر يناسب المكتب والسيارة وشنطة السفر")),
 "B0FVY9CGHB": ("HABBAA USB-A to Type-C Braided Charging Cable 1.2m, Fast Charge and Data Sync Nylon Cord with Reinforced Connectors for Android Phones and USB-C Devices",
                "كيبل شحن مضفر من USB-A إلى تايب سي من هبة HABBAA بطول 1.2 متر، سلك نايلون للشحن السريع ونقل البيانات برؤوس معززة لجوالات أندرويد وأجهزة USB-C",
                ("1.2 metre USB-A to Type-C cable, works with wall chargers, car chargers, laptops and power banks with a USB-A port", "كيبل من USB-A إلى تايب سي بطول 1.2 متر، يشتغل مع الشاحن الجداري وشاحن السيارة واللابتوب والباور بانك اللي فيها منفذ USB-A")),
 "B0FVYG6N43": ("HABBAA Braided Micro USB Cable 1.2m, Heavy Duty Anti-Break Nylon Charging Cable with Fast Charging and Data Sync for Android Phones, Power Banks and Speakers",
                "كيبل مايكرو USB مضفر من هبة HABBAA بطول 1.2 متر، كيبل شحن نايلون قوي مقاوم للكسر للشحن السريع ونقل البيانات لجوالات أندرويد والباور بانك والسماعات",
                ("Micro USB connector for older Android phones, power banks, Bluetooth speakers, game controllers and accessories", "منفذ مايكرو USB للجوالات الأقدم والباور بانك وسماعات البلوتوث ويدات الألعاب والملحقات")),
 "B0FVYNQPW8": ("HABBAA Type-C to USB-A Braided Cable 1.2m, Fast Charging and Data Sync Heavy Duty Nylon Charger Cable for Android Phones, Tablets and USB-C Devices",
                "كيبل مضفر من تايب سي إلى USB-A من هبة HABBAA بطول 1.2 متر، سلك شاحن نايلون قوي للشحن السريع ونقل البيانات لجوالات أندرويد والأجهزة اللوحية وأجهزة USB-C",
                ("1.2 metre cable with Type-C and USB-A ends, a reliable everyday cable for home, office and car", "كيبل بطول 1.2 متر بطرف تايب سي وطرف USB-A، كيبل يومي يعتمد عليه في البيت والدوام والسيارة")),
}
for a, (te, ta, (xe, xa)) in cab.items():
    be = CAB_B_EN[:]; ba = CAB_B_AR[:]
    be[4] = "PRACTICAL LENGTH FOR DAILY USE: " + xe
    ba[4] = "طول عملي للاستخدام اليومي: " + xa
    put(a, te, ta, be, ba, CAB_D_EN, CAB_D_AR, CAB_K_EN, CAB_K_AR)

put("B0FVY2NSVT",
    "HABBAA Type-C to 3.5mm Audio and Charging Adapter 1m Braided Cable, 2 in 1 USB-C Headphone Jack Splitter for Music, Calls and Charging at the Same Time",
    "محول تايب سي إلى سماعة 3.5 ملم مع منفذ شحن من هبة HABBAA بكيبل مضفر 1 متر، موزع USB-C اثنين في واحد للموسيقى والمكالمات والشحن في نفس الوقت",
    ["2 IN 1 ADAPTER: Listen to music or take calls with your wired 3.5mm earphones and charge your phone at the same time, perfect for phones that have only one USB-C port",
     "CLEAR SOUND: The built-in digital audio chip delivers clean, stable sound for music, videos, games and voice calls without crackling or delay",
     "CHARGE WHILE YOU LISTEN: The extra Type-C port lets you keep your phone charging during long calls, gaming sessions, road trips or flights",
     "BRAIDED 1 METRE CABLE: A durable nylon braided cable that resists tangling and bending, with enough length to keep the phone comfortable in your hand",
     "WIDE COMPATIBILITY: Works with most USB-C Android phones and tablets that do not have a 3.5mm headphone jack; please check that your phone supports USB-C audio",],
    ["محول اثنين في واحد: اسمع الموسيقى أو رد على المكالمات بسماعتك السلكية 3.5 ملم واشحن جوالك في نفس الوقت، مناسب للجوالات اللي فيها منفذ تايب سي واحد بس",
     "صوت واضح: شريحة صوت رقمية مدمجة تعطيك صوت نقي وثابت للموسيقى والفيديوهات والألعاب والمكالمات بدون تقطيع أو تأخير",
     "اشحن وأنت تسمع: منفذ تايب سي الإضافي يخلي جوالك يشحن خلال المكالمات الطويلة والألعاب والمشاوير والرحلات",
     "كيبل مضفر بطول 1 متر: كيبل نايلون مضفر متين يقاوم التشابك والثني، وطوله يخلي الجوال مريح في يدك",
     "توافق واسع: يناسب أغلب جوالات وأجهزة أندرويد اللوحية بمنفذ تايب سي اللي ما فيها مدخل سماعة 3.5 ملم، تأكد إن جوالك يدعم الصوت عبر تايب سي",],
    ("The HABBAA Type-C to 3.5mm audio and charging adapter solves a common problem with modern phones: one port for both charging and headphones. "
     "Plug the adapter into your phone, connect your favourite wired earphones to the 3.5mm jack and your charger to the Type-C port, and enjoy music, videos and calls while the battery keeps charging. "
     "The integrated digital audio chip converts the signal for clear, stable sound. "
     "The 1 metre nylon braided cable is flexible, tangle free and strong enough for daily use at home, in the office, in the car or on a flight. "
     "It is a small accessory that makes long calls, online classes, gaming and travel much easier. "
     "Compatible with most USB-C Android phones and tablets without a headphone jack. Package contents: 1 x HABBAA 2 in 1 audio and charging adapter."),
    ("محول هبة HABBAA من تايب سي إلى سماعة 3.5 ملم مع شحن يحل مشكلة الجوالات الحديثة: منفذ واحد للشحن والسماعة. "
     "ركب المحول في جوالك، ووصل سماعتك السلكية في مدخل 3.5 ملم والشاحن في منفذ تايب سي، واستمتع بالموسيقى والفيديوهات والمكالمات والبطارية تشحن. "
     "شريحة الصوت الرقمية المدمجة تحول الإشارة لصوت واضح وثابت. "
     "الكيبل النايلون المضفر بطول 1 متر مرن وما يتشابك وقوي للاستخدام اليومي في البيت والدوام والسيارة والطيارة. "
     "إكسسوار صغير يسهل عليك المكالمات الطويلة والدروس عن بعد والألعاب والسفر. "
     "يناسب أغلب جوالات وأجهزة أندرويد اللوحية بمنفذ تايب سي بدون مدخل سماعة. محتوى العبوة: محول صوت وشحن واحد من هبة HABBAA."),
    "aux adapter headphone jack converter usb c to aux earphone splitter dongle audio charging adapter type c audio",
    "محول سماعة تايب سي مدخل سماعة موزع شحن وسماعة محول اوكس سماعات سلكية دونقل")

# ---------------- 2. Home storage organizers ----------------
def under_desk(asin, col_en, col_ar):
    put(asin,
        f"HABBAA Under Desk Drawer Organizer, Self-Adhesive Hidden Storage Box for Pens, Paper Clips, Phones and Small Accessories, Space Saving Desk Organizer for Office and Home, {col_en}",
        f"منظم درج تحت المكتب من هبة HABBAA، صندوق تخزين مخفي ذاتي اللصق للأقلام ومشابك الورق والجوالات والأغراض الصغيرة، منظم مكتب يوفر المساحة للدوام والبيت، {col_ar}",
        ["HIDDEN EXTRA DRAWER: Sticks under your desk, table or shelf to add a slim sliding drawer that keeps small items out of sight but always within reach",
         "NO DRILLING NEEDED: The strong self-adhesive pad installs in seconds on any smooth flat surface without screws, tools or damage to your furniture",
         "KEEPS THE DESK CLEAR: Store pens, sticky notes, paper clips, chargers, keys, earphones and cards so your work surface stays clean and tidy",
         "DURABLE LIGHTWEIGHT PLASTIC: Made of sturdy ABS plastic with a smooth sliding tray for long daily use in offices, study rooms and dorms",
         f"MINIMAL MODERN LOOK: A simple {col_en.lower()} design that blends with home office, school and shop counters, a practical gift for students and employees",],
        ["درج إضافي مخفي: يلتصق تحت المكتب أو الطاولة أو الرف ويضيف لك درج نحيف ينسحب، يخبي الأغراض الصغيرة عن العين ويخليها قريبة منك",
         "بدون تخريم: لاصق قوي يركب في ثواني على أي سطح أملس بدون براغي أو أدوات وبدون ما يضر أثاثك",
         "مكتب مرتب دايم: خزن فيه الأقلام والأوراق اللاصقة ومشابك الورق والشواحن والمفاتيح والسماعات والبطاقات، فيبقى سطح المكتب نظيف ومرتب",
         "بلاستيك متين وخفيف: مصنوع من بلاستيك ABS قوي مع درج ينسحب بسلاسة للاستخدام اليومي في المكاتب وغرف المذاكرة والسكن",
         f"شكل عصري بسيط: تصميم بسيط باللون {col_ar} يناسب مكتب البيت والمدرسة وكاونتر المحل، وهدية عملية للطلاب والموظفين",],
        ("Turn the empty space under your desk into useful storage with the HABBAA under desk drawer organizer. "
         "Peel off the protective film, press the adhesive pad under any smooth surface and you instantly get a hidden sliding drawer for your daily small items. "
         "It is perfect for pens, pencils, erasers, sticky notes, paper clips, USB drives, chargers, earphones, keys and cards. "
         "Your desk stays clear for work and study, and the things you need are still just one pull away. "
         "Use it under office desks, study tables, kitchen cabinets, shelves, dressing tables and shop counters. "
         "Made from lightweight and durable ABS plastic with a smooth finish that is easy to wipe clean. "
         "Installation tip: clean and dry the surface before sticking and wait a few hours before filling the drawer. Package contents: 1 x HABBAA under desk drawer organizer."),
        ("حول المساحة الفاضية تحت مكتبك لتخزين مفيد مع منظم درج تحت المكتب من هبة HABBAA. "
         "شيل الغلاف الواقي، والصق القطعة اللاصقة تحت أي سطح أملس، وعلى طول يصير عندك درج مخفي ينسحب لأغراضك الصغيرة اليومية. "
         "مناسب للأقلام والمحايات والأوراق اللاصقة ومشابك الورق والفلاشات والشواحن والسماعات والمفاتيح والبطاقات. "
         "يبقى مكتبك فاضي للشغل والمذاكرة، وأغراضك اللي تحتاجها على سحبة وحدة. "
         "استخدمه تحت مكاتب الدوام وطاولات المذاكرة ودواليب المطبخ والأرفف والتسريحة وكاونتر المحل. "
         "مصنوع من بلاستيك ABS خفيف ومتين بسطح ناعم سهل التنظيف. "
         "نصيحة للتركيب: نظف السطح ونشفه قبل اللصق وانتظر كم ساعة قبل ما تعبي الدرج. محتوى العبوة: منظم درج واحد تحت المكتب من هبة HABBAA."),
        "pen holder desk drawer under table storage stick on drawer office organizer hidden drawer pencil tray",
        "منظم مكتب درج لاصق تحت الطاولة حامل اقلام تنظيم المكتب درج مخفي منظم ادوات مكتبية")

under_desk("B0FVFCGX8B", "Blue", "أزرق")
under_desk("B0FVFCFGPX", "White", "أبيض")
under_desk("B0FVF9S7VF", "Pink", "وردي")

def hooks(asin, sh_en, sh_ar):
    put(asin,
        f"HABBAA Adhesive Wall Hooks, Strong Self Adhesive Heavy Duty Hooks for Hanging Towels, Keys, Bags and Kitchen Tools, No Drilling Wall Hangers for Bathroom and Kitchen, {sh_en}",
        f"خطافات حائط لاصقة من هبة HABBAA، علاقات لاصقة قوية لتعليق المناشف والمفاتيح والشنط وأدوات المطبخ، علاقات جدار بدون تخريم للحمام والمطبخ، شكل {sh_ar}",
        ["STRONG ADHESIVE HOLD: High tack adhesive pads give a firm grip on smooth walls, tiles, glass, mirrors, wood and metal for everyday hanging needs",
         "NO DRILLING, NO TOOLS: Peel and stick in seconds without nails, screws or holes, ideal for rented homes, offices and rooms where you do not want to damage the wall",
         "ENDLESS USES: Hang bath towels, robes, keys, bags, hats, kitchen towels, utensils, cables, plants and decorations in the bathroom, kitchen, bedroom or entrance",
         f"NEAT {sh_en.upper()} DESIGN: A clean and compact {sh_en.lower()} shape that looks tidy on any wall and keeps your home organised without taking space",
         "EASY TO USE: Clean and dry the surface, press the hook firmly for 30 seconds and wait a few hours before hanging heavier items for the best result",],
        ["لاصق قوي يثبت: لاصق عالي الالتصاق يثبت بقوة على الجدران الملساء والسيراميك والزجاج والمرايا والخشب والمعدن لاحتياجات التعليق اليومية",
         "بدون تخريم وبدون أدوات: قشر والصق في ثواني بدون مسامير أو براغي أو خروم، مناسب للشقق المستأجرة والمكاتب والغرف اللي ما تبي تضر جدارها",
         "استخدامات كثيرة: علق المناشف والروب والمفاتيح والشنط والطواقي ومناشف المطبخ والأدوات والكيبلات والنباتات والزينة في الحمام والمطبخ وغرفة النوم والمدخل",
         f"تصميم {sh_ar} مرتب: شكل {sh_ar} أنيق وصغير يبان مرتب على أي جدار ويخلي بيتك منظم بدون ما ياخذ مساحة",
         "سهل الاستخدام: نظف السطح ونشفه واضغط الخطاف بقوة 30 ثانية وانتظر كم ساعة قبل تعليق الأغراض الثقيلة عشان أفضل نتيجة",],
        ("HABBAA self adhesive wall hooks are a quick and tidy way to add hanging space anywhere in your home without drilling a single hole. "
         "Each hook has a strong adhesive pad that holds firmly on smooth surfaces such as tiles, painted walls, glass, mirrors, wood, metal and cabinet doors. "
         "Use them in the bathroom for towels and robes, in the kitchen for towels, spoons and gloves, at the entrance for keys and bags, and in the bedroom for clothes, hats and accessories. "
         "They are also handy in offices, wardrobes, cars and caravans. "
         "For the strongest hold, clean the surface with a dry cloth, press the hook firmly and wait a few hours before use. "
         "Not suitable for rough, wet, dusty or wallpapered surfaces. "
         "A simple, low cost upgrade that keeps everyday items off the floor and organised."),
        ("خطافات الحائط اللاصقة من هبة HABBAA طريقة سريعة ومرتبة تضيف أماكن تعليق في أي مكان في بيتك بدون ما تخرم ولا خرم. "
         "كل خطاف فيه لاصق قوي يثبت بإحكام على الأسطح الملساء مثل السيراميك والجدار المدهون والزجاج والمرايا والخشب والمعدن وأبواب الدواليب. "
         "استخدمها في الحمام للمناشف والروب، وفي المطبخ للمناشف والملاعق والقفازات، وعند المدخل للمفاتيح والشنط، وفي غرفة النوم للملابس والطواقي والإكسسوارات. "
         "ومفيدة كمان في المكاتب والدواليب والسيارات والكرفانات. "
         "عشان أقوى تثبيت، نظف السطح بقطعة قماش ناشفة واضغط الخطاف بقوة وانتظر كم ساعة قبل الاستخدام. "
         "ما تناسب الأسطح الخشنة أو المبللة أو المغبرة أو ورق الجدران. "
         "ترقية بسيطة وبسعر مناسب تخلي أغراضك اليومية مرتبة وبعيدة عن الأرض."),
        "stick on hooks towel hook key holder bathroom hanger kitchen hanger door hook wall hanger self adhesive hanger",
        "علاقة لاصقة شماعة جدار علاقة مناشف علاقة مفاتيح خطاف حمام خطاف مطبخ علاقات لاصقة بدون مسامير")

hooks("B0GWY96ZDV", "Square", "مربع")
hooks("B0GWYH1Y8Q", "Round", "دائري")

put("B0GS2GZXN4",
    "HABBAA Felt Storage Caddy with Handles, Multi Compartment Organizer Basket for Wipes, Bottles, Cosmetics, Toys and Office Supplies, Portable Grey Home Storage Organizer",
    "منظم تخزين من اللباد بمقابض من هبة HABBAA، سلة تنظيم متعددة الأقسام للمناديل المبللة والعلب ومستحضرات التجميل والألعاب وأدوات المكتب، منظم منزلي متنقل رمادي",
    ["MULTIPLE COMPARTMENTS: Several divided pockets keep wipes, bottles, creams, brushes, toys and stationery separated and easy to find at a glance",
     "CARRY IT ROOM TO ROOM: Sturdy built-in handles let you move your essentials from the bedroom to the bathroom, kitchen, car or office in one trip",
     "SOFT DURABLE FELT: Made of thick felt fabric that is lightweight, soft to the touch and holds its shape for daily organising",
     "MANY USES AT HOME: Use it as a baby diaper caddy, makeup organizer, bathroom caddy, art supplies holder, cleaning caddy or car organizer",
     "NEAT GREY LOOK: A simple grey colour that matches modern decor and keeps your shelves, tables and counters looking tidy",],
    ["أقسام متعددة: جيوب مقسمة تفصل المناديل والعلب والكريمات والفرش والألعاب والأدوات المكتبية وتخليها سهلة الوصول من أول نظرة",
     "تنقله من غرفة لغرفة: مقابض قوية تخليك تنقل أغراضك من غرفة النوم للحمام والمطبخ والسيارة والدوام في مشوار واحد",
     "لباد ناعم ومتين: مصنوع من قماش لباد سميك خفيف وناعم ويحافظ على شكله مع الاستخدام اليومي",
     "استخدامات كثيرة في البيت: استخدمه منظم حفاضات للبيبي أو منظم مكياج أو منظم حمام أو حامل أدوات رسم أو سلة أدوات تنظيف أو منظم سيارة",
     "شكل رمادي مرتب: لون رمادي بسيط يناسب الديكور العصري ويخلي الأرفف والطاولات والكاونتر مرتبة",],
    ("Keep your daily essentials together with the HABBAA felt storage caddy. "
     "The multi compartment design gives every item its own place, from wet wipes and lotions to brushes, toys, markers and small tools. "
     "Two strong handles make it easy to carry around the house, so you can take baby care items to the living room, makeup to the dressing table or cleaning supplies from room to room. "
     "The thick felt fabric is lightweight, soft and keeps its structure, and it will not scratch your furniture. "
     "Use it on shelves, desks, counters, inside cupboards or in the car. "
     "It also makes a practical gift for new parents, students and anyone who loves an organised home. "
     "Package contents: 1 x HABBAA felt storage caddy."),
    ("خل أغراضك اليومية مع بعض في منظم اللباد من هبة HABBAA. "
     "تصميمه متعدد الأقسام يعطي كل غرض مكانه، من المناديل المبللة والكريمات للفرش والألعاب والأقلام والأدوات الصغيرة. "
     "المقبضين القويين يسهلون حمله في البيت، فتقدر تنقل أغراض البيبي للصالة، والمكياج للتسريحة، وأدوات التنظيف من غرفة لغرفة. "
     "قماش اللباد السميك خفيف وناعم ويحافظ على شكله، وما يخدش الأثاث. "
     "استخدمه على الأرفف والمكاتب والكاونتر وداخل الدواليب أو في السيارة. "
     "وهو هدية عملية للأهل الجدد والطلاب وكل اللي يحب البيت المرتب. "
     "محتوى العبوة: منظم لباد واحد من هبة HABBAA."),
    "diaper caddy baby organizer makeup organizer basket storage bin with handle nursery storage car organizer felt basket",
    "منظم حفاضات منظم مكياج سلة تخزين منظم سيارة سلة لباد منظم اغراض البيبي منظم حمام")

put("B0G546GRSG",
    "HABBAA Foldable Fabric Storage Box 33x38x33 cm, Collapsible Storage Cube Organizer for Shelves, Closets and Wardrobes, Lightweight Storage Bin for Toys, Clothes and Accessories, White",
    "صندوق تخزين قماش قابل للطي من هبة HABBAA مقاس 33×38×33 سم، مكعب تخزين لتنظيم الأرفف والدواليب والخزائن، صندوق خفيف للألعاب والملابس والإكسسوارات، أبيض",
    ["GENEROUS 33 x 38 x 33 CM SIZE: A roomy storage cube that holds clothes, towels, toys, books, bags and accessories and fits most cube shelf units",
     "FOLDS FLAT IN SECONDS: Collapse the box when it is not in use to save space in cupboards, under the bed or when moving house",
     "LIGHTWEIGHT AND STURDY: Durable fabric walls keep their shape when filled, while the box stays light and easy to pull out and carry",
     "CLEAN WHITE DESIGN: A bright white colour that matches modern bedrooms, kids rooms, living rooms and offices for a calm and tidy look",
     "ORGANISE ANY ROOM: Perfect for wardrobes, kids toys, linen cupboards, office files and seasonal items, a simple way to reduce clutter",],
    ["مقاس واسع 33×38×33 سم: مكعب تخزين واسع يشيل الملابس والمناشف والألعاب والكتب والشنط والإكسسوارات ويناسب أغلب أرفف المكعبات",
     "ينطوي في ثواني: اطويه وقت ما تحتاجه عشان توفر مساحة في الدولاب أو تحت السرير أو وقت النقل",
     "خفيف ومتين: جدران قماش قوية تحافظ على شكلها وهو مليان، والصندوق خفيف وسهل تسحبه وتشيله",
     "تصميم أبيض نظيف: لون أبيض فاتح يناسب غرف النوم وغرف الأطفال والصالات والمكاتب ويعطي شكل هادي ومرتب",
     "نظم أي غرفة: مناسب للدواليب وألعاب الأطفال ودولاب المفارش وملفات المكتب وأغراض المواسم، طريقة بسيطة تقلل الفوضى",],
    ("Bring order to your shelves with the HABBAA foldable fabric storage box. "
     "Measuring 33 x 38 x 33 cm, it offers plenty of room for clothes, towels, bedding, toys, books, shoes and household items. "
     "The cube shape slides neatly into most shelf units, wardrobes and open cabinets, and it can also stand alone on the floor or on top of a cupboard. "
     "When you do not need it, simply fold it flat and store it away. "
     "The fabric walls are light yet firm enough to hold their shape, and the bright white colour gives your room a clean modern look. "
     "Use several boxes together to sort items by person, season or category and enjoy a home that is easier to keep tidy. "
     "Package contents: 1 x HABBAA fabric storage box."),
    ("رتب أرففك مع صندوق التخزين القماش القابل للطي من هبة HABBAA. "
     "مقاسه 33×38×33 سم ويعطيك مساحة كبيرة للملابس والمناشف والمفارش والألعاب والكتب والأحذية وأغراض البيت. "
     "شكله المكعب يدخل بسهولة في أغلب الأرفف والدواليب والخزائن المفتوحة، وتقدر تحطه لحاله على الأرض أو فوق الدولاب. "
     "ولما ما تحتاجه، اطويه وخزنه. "
     "جدران القماش خفيفة وثابتة وتحافظ على شكلها، واللون الأبيض يعطي غرفتك شكل نظيف وعصري. "
     "استخدم أكثر من صندوق مع بعض عشان تفرز الأغراض حسب الشخص أو الموسم أو النوع وتستمتع ببيت أسهل في الترتيب. "
     "محتوى العبوة: صندوق تخزين قماش واحد من هبة HABBAA."),
    "storage cube bin closet organizer foldable box toy storage clothes storage shelf basket cube organizer fabric bin",
    "مكعب تخزين صندوق ملابس منظم دولاب صندوق العاب سلة تخزين منظم ارفف صندوق قماش")

put("B0CLSD6CHT",
    "HABBAA Bamboo Laundry Basket with Lid and Handles, Rectangular Wooden Laundry Hamper and Storage Basket for Clothes, Towels and Bedroom or Bathroom Organisation",
    "سلة غسيل من الخيزران بغطاء ومقابض من هبة HABBAA، سلة ملابس خشبية مستطيلة وسلة تخزين للملابس والمناشف لتنظيم غرفة النوم والحمام",
    ["NATURAL BAMBOO LOOK: Made with natural bamboo that brings a warm, calm and elegant touch to your bedroom, bathroom or laundry room",
     "LID KEEPS IT TIDY: The fitted lid hides dirty clothes from view and helps keep the room looking neat and organised",
     "EASY TO CARRY: Side handles make it simple to carry clothes to the washing machine or move the basket from room to room",
     "SPACIOUS RECTANGULAR SHAPE: A slim rectangular design that holds plenty of laundry while fitting easily in corners, behind doors and next to the wardrobe",
     "MORE THAN A LAUNDRY BASKET: Also great for storing towels, bed linen, blankets, kids toys or seasonal clothes",],
    ["شكل خيزران طبيعي: مصنوعة من الخيزران الطبيعي اللي يعطي لمسة دافئة وهادئة وأنيقة لغرفة النوم أو الحمام أو غرفة الغسيل",
     "غطاء يخليها مرتبة: الغطاء يخبي الملابس المتسخة عن النظر ويخلي الغرفة مرتبة ومنظمة",
     "سهلة الحمل: مقابض جانبية تسهل حمل الملابس للغسالة أو نقل السلة من غرفة لغرفة",
     "شكل مستطيل واسع: تصميم مستطيل نحيف يشيل كمية ملابس كبيرة ويدخل بسهولة في الزوايا وورا الأبواب وجنب الدولاب",
     "أكثر من سلة غسيل: ممتازة كمان لتخزين المناشف والمفارش والبطانيات وألعاب الأطفال وملابس المواسم",],
    ("The HABBAA bamboo laundry basket combines practical storage with a natural, stylish look. "
     "Its rectangular shape makes the most of small spaces, so it fits neatly in a bedroom corner, a bathroom, a laundry room or behind a door. "
     "The lid keeps clothes out of sight and the room looking tidy, while the handles make it easy to carry your laundry to the washing machine. "
     "Bamboo is a strong and naturally beautiful material that adds warmth to modern and classic interiors. "
     "Use it as a laundry hamper, or as storage for towels, bedding, blankets, toys and clothes. "
     "A simple upgrade that helps the whole family keep the home organised. "
     "Package contents: 1 x HABBAA bamboo laundry basket with lid."),
    ("سلة الغسيل الخيزران من هبة HABBAA تجمع بين التخزين العملي والشكل الطبيعي الأنيق. "
     "شكلها المستطيل يستغل المساحات الصغيرة، فتدخل بترتيب في زاوية غرفة النوم أو الحمام أو غرفة الغسيل أو ورا الباب. "
     "الغطاء يخبي الملابس ويخلي الغرفة مرتبة، والمقابض تسهل حمل الغسيل للغسالة. "
     "الخيزران خامة قوية وجميلة بطبيعتها وتضيف دفا للديكور العصري والكلاسيكي. "
     "استخدمها سلة غسيل أو للتخزين للمناشف والمفارش والبطانيات والألعاب والملابس. "
     "ترقية بسيطة تساعد العائلة كلها تحافظ على ترتيب البيت. "
     "محتوى العبوة: سلة غسيل خيزران واحدة بغطاء من هبة HABBAA."),
    "laundry hamper clothes basket dirty clothes basket wooden hamper bathroom basket storage basket with lid",
    "سلة ملابس متسخة سلة غسيل بغطاء سلة خشب سلة حمام سلة تخزين منظم ملابس")

# ---------------- 3. Kitchen gadgets ----------------
put("B0DBLCRNDZ",
    "HABBAA Kitchen Scissors, Stainless Steel Multipurpose Household Shears for Cutting Meat, Vegetables, Herbs, Packaging and Paper, Kitchen, Office and Craft Use, 1 Piece",
    "مقص مطبخ من هبة HABBAA، مقص منزلي ستانلس ستيل متعدد الاستخدامات لتقطيع اللحم والخضار والأعشاب والتغليف والورق، للمطبخ والمكتب والأعمال اليدوية، قطعة واحدة",
    ["SHARP STAINLESS STEEL BLADES: Strong stainless steel blades cut cleanly through vegetables, herbs, meat, chicken, packaging and paper",
     "COMFORTABLE GRIP: An easy hold handle reduces hand strain during long food preparation and gives better control while cutting",
     "ONE TOOL FOR MANY JOBS: Use it in the kitchen, office, school projects and crafts to open bags, cut tape, trim flowers or snip strings",
     "EASY TO CLEAN: Rinse with warm soapy water after use and dry well to keep the blades in good condition for longer",
     "EVERYDAY ESSENTIAL: A practical pair of scissors every home needs, also a nice small gift for new homes and students",],
    ["شفرات ستانلس ستيل حادة: شفرات ستانلس ستيل قوية تقطع بنظافة الخضار والأعشاب واللحم والدجاج والتغليف والورق",
     "مسكة مريحة: مقبض سهل المسك يخفف تعب اليد وقت التحضير الطويل ويعطيك تحكم أفضل وقت القص",
     "أداة وحدة لشغلات كثيرة: استخدمه في المطبخ والمكتب ومشاريع المدرسة والأعمال اليدوية لفتح الأكياس وقص اللاصق وتقليم الورد وقص الخيوط",
     "سهل التنظيف: اغسله بماي دافي وصابون بعد الاستخدام ونشفه زين عشان تبقى الشفرات بحالة ممتازة أطول",
     "أساسي في كل بيت: مقص عملي يحتاجه كل بيت، وهدية صغيرة حلوة للبيوت الجديدة والطلاب",],
    ("The HABBAA kitchen scissors are a reliable everyday tool for the kitchen and beyond. "
     "The stainless steel blades stay sharp and cut cleanly through herbs, vegetables, meat, chicken, pizza, packaging, tape and paper. "
     "The comfortable handle fits right and left hands and gives you a steady grip for precise cutting. "
     "Keep a pair in the kitchen drawer, another on the office desk and one with your craft supplies. "
     "Clean with warm soapy water and dry immediately after washing. "
     "Package contents: 1 x HABBAA stainless steel kitchen scissors."),
    ("مقص المطبخ من هبة HABBAA أداة يومية تعتمد عليها في المطبخ وغيره. "
     "شفرات الستانلس ستيل تبقى حادة وتقطع بنظافة الأعشاب والخضار واللحم والدجاج والبيتزا والتغليف واللاصق والورق. "
     "المقبض المريح يناسب اليد اليمين واليسار ويعطيك مسكة ثابتة لقص دقيق. "
     "خل واحد في درج المطبخ وواحد على مكتب الدوام وواحد مع أدوات الأعمال اليدوية. "
     "نظفه بماي دافي وصابون ونشفه بعد الغسيل مباشرة. "
     "محتوى العبوة: مقص مطبخ ستانلس ستيل واحد من هبة HABBAA."),
    "kitchen shears meat scissors poultry shears household scissors utility scissors herb scissors food scissors",
    "مقص لحم مقص دجاج مقص خضار مقص منزلي مقص قوي مقص اعشاب مقص اكل")

put("B0CPJFMG9F",
    "HABBAA Storage Jar 550 ml with Lid, Premium Silver Kitchen Canister for Coffee, Sugar, Tea, Spices, Nuts and Dry Food, Airtight Style Container for Pantry and Counter",
    "برطمان تخزين من هبة HABBAA سعة 550 مل بغطاء، علبة مطبخ فضية فاخرة للقهوة والسكر والشاي والبهارات والمكسرات والأطعمة الجافة، حافظة للمخزن والكاونتر",
    ["550 ML CAPACITY: A handy size for coffee beans, ground coffee, sugar, tea, cardamom, spices, nuts, dates and snacks",
     "ELEGANT SILVER FINISH: A premium silver look that makes your kitchen counter, coffee corner or majlis tray look neat and stylish",
     "KEEPS FOOD ORGANISED: The close fitting lid helps keep dry food fresh and protects it from dust in the pantry or on the counter",
     "EASY TO REFILL AND CLEAN: A wide opening makes scooping and refilling simple, and the jar is easy to wipe clean",
     "GIFT FRIENDLY: A useful and good looking gift for new homes, coffee lovers and anyone who enjoys an organised kitchen",],
    ["سعة 550 مل: حجم عملي لحبوب القهوة والقهوة المطحونة والسكر والشاي والهيل والبهارات والمكسرات والتمر والسناكات",
     "لمسة فضية أنيقة: شكل فضي فاخر يخلي كاونتر المطبخ وركن القهوة وصينية المجلس مرتبة وأنيقة",
     "يحافظ على ترتيب الأكل: الغطاء المحكم يساعد يحافظ على الأطعمة الجافة ويحميها من الغبار في المخزن أو على الكاونتر",
     "سهل التعبئة والتنظيف: الفتحة الواسعة تسهل الغرف والتعبئة، والبرطمان سهل المسح والتنظيف",
     "مناسب كهدية: هدية مفيدة وشكلها حلو للبيوت الجديدة ومحبي القهوة وكل اللي يحب المطبخ المرتب",],
    ("Store your everyday kitchen essentials in style with the HABBAA 550 ml storage jar. "
     "Its silver finish adds a premium touch to your counter, coffee station or pantry shelf. "
     "Use it for Arabic coffee, coffee beans, sugar, tea, cardamom, saffron, spices, nuts, dates or sweets. "
     "The lid closes neatly to help protect contents from dust and keep your shelves organised. "
     "Combine several jars to create a matching set for your coffee corner. "
     "Wipe clean with a damp cloth. Package contents: 1 x HABBAA 550 ml storage jar with lid."),
    ("خزن أساسيات مطبخك اليومية بشكل أنيق مع برطمان التخزين من هبة HABBAA سعة 550 مل. "
     "لونه الفضي يضيف لمسة فاخرة للكاونتر وركن القهوة ورف المخزن. "
     "استخدمه للقهوة العربية وحبوب القهوة والسكر والشاي والهيل والزعفران والبهارات والمكسرات والتمر أو الحلويات. "
     "الغطاء يقفل بترتيب ويساعد يحمي المحتوى من الغبار ويخلي أرففك منظمة. "
     "اجمع أكثر من برطمان وسو طقم متناسق لركن القهوة. "
     "ينظف بقطعة قماش مبللة. محتوى العبوة: برطمان تخزين واحد سعة 550 مل بغطاء من هبة HABBAA."),
    "canister coffee jar sugar container tea tin spice jar kitchen container food storage pantry jar",
    "علبة قهوة علبة سكر حافظة بهارات علبة شاي برطمان مطبخ علبة تخزين حافظة طعام")

put("B0DF94K1FD",
    "HABBAA Bamboo Plate Stand, Wooden Dish Rack and Plate Holder for Kitchen Counter and Cabinet, Display Stand for Plates, Lids, Cutting Boards and Books",
    "حامل أطباق من الخيزران من هبة HABBAA، رف صحون خشبي وحامل أطباق لكاونتر المطبخ والدولاب، حامل عرض للأطباق والأغطية وألواح التقطيع والكتب",
    ["NATURAL BAMBOO: Made from natural bamboo that is light, strong and adds a warm wooden touch to your kitchen",
     "KEEPS PLATES UPRIGHT: Slotted design holds plates upright and separated, saving cupboard space and making each plate easy to grab",
     "DRY OR DISPLAY: Use it to let washed plates air dry, or to display decorative plates, trays and serving dishes on the counter",
     "MULTI USE ORGANISER: Also great for pot lids, cutting boards, baking trays, books, tablets and file folders",
     "EASY CARE: Wipe with a damp cloth and dry well, avoid soaking to keep the bamboo looking beautiful for longer",],
    ["خيزران طبيعي: مصنوع من الخيزران الطبيعي الخفيف والقوي اللي يضيف لمسة خشبية دافئة لمطبخك",
     "يوقف الأطباق: تصميم بفتحات يوقف الأطباق ويفصلها عن بعض، يوفر مساحة الدولاب ويسهل أخذ أي طبق",
     "للتنشيف أو العرض: استخدمه لتنشيف الصحون بعد الغسيل، أو لعرض الأطباق والصواني وأطباق التقديم على الكاونتر",
     "منظم متعدد الاستخدامات: ممتاز كمان لأغطية القدور وألواح التقطيع وصواني الفرن والكتب والأجهزة اللوحية والملفات",
     "عناية سهلة: امسحه بقطعة قماش مبللة ونشفه زين، وتجنب نقعه بالماي عشان يبقى الخيزران جميل أطول",],
    ("The HABBAA bamboo plate stand is a simple way to organise and display your dishes. "
     "Its slotted design keeps plates standing upright and apart, so they take less space and are easy to pick up. "
     "Place it on the counter next to the sink to air dry washed plates, or inside a cupboard to keep plates neatly arranged. "
     "It also works as a stand for pot lids, cutting boards, trays, books and tablets. "
     "The natural bamboo finish suits modern and traditional kitchens and coffee corners. "
     "Clean with a damp cloth and dry well. Package contents: 1 x HABBAA bamboo plate stand."),
    ("حامل الأطباق الخيزران من هبة HABBAA طريقة بسيطة تنظم فيها صحونك وتعرضها. "
     "تصميمه بفتحات يخلي الأطباق واقفة ومفصولة، فتاخذ مساحة أقل وسهل تاخذها. "
     "حطه على الكاونتر جنب المغسلة عشان تنشف الصحون، أو داخل الدولاب عشان تبقى الأطباق مرتبة. "
     "ويشتغل كمان كحامل لأغطية القدور وألواح التقطيع والصواني والكتب والأجهزة اللوحية. "
     "لون الخيزران الطبيعي يناسب المطابخ العصرية والتقليدية وركن القهوة. "
     "ينظف بقطعة قماش مبللة وينشف زين. محتوى العبوة: حامل أطباق خيزران واحد من هبة HABBAA."),
    "dish rack plate holder plate organizer wooden rack drying rack kitchen rack lid holder plate display stand",
    "رف صحون حامل صحون منظم اطباق رف خشب حامل اغطية تنشيف صحون منظم مطبخ")

def clip(asin, n):
    put(asin,
        f"HABBAA Bag Sealing Clips with Pour Spout, Pack of {n}, Reusable Food Bag Sealer with Lid for Rice, Beans, Grains, Cereal and Snacks, Kitchen Storage Clips, Assorted Colours",
        f"مشابك إغلاق أكياس الطعام بفتحة صب من هبة HABBAA، عبوة {n} قطع، مشبك أكياس قابل لإعادة الاستخدام بغطاء للرز والفول والحبوب والكورن فليكس والسناكات، ألوان متنوعة",
        ["POUR AND SEAL IN ONE: A built-in pour spout lets you pour rice, beans, grains, cereal, sugar or snacks straight from the bag, then close the lid to seal",
         "KEEPS FOOD FRESH: The tight clip closes the open bag to help keep dry food fresh, crunchy and protected from moisture and insects",
         "NO MORE SPILLS: Controlled pouring means fewer spills on the counter and less waste when filling jars, pots and bowls",
         "REUSABLE AND EASY TO USE: Simply clip it onto the bag opening, flip the cap to pour, and reuse it again and again on new bags",
         f"COLOURFUL PACK OF {n}: Different colours help you label and organise your pantry by food type at a glance",],
        ["صب وإغلاق في قطعة وحدة: فتحة صب مدمجة تخليك تصب الرز والفول والحبوب والكورن فليكس والسكر والسناكات من الكيس مباشرة، وبعدها تقفل الغطاء",
         "يحافظ على الأكل: المشبك المحكم يقفل الكيس المفتوح ويساعد يحافظ على الأطعمة الجافة مقرمشة ومحمية من الرطوبة والحشرات",
         "بدون كب وانسكاب: الصب المتحكم فيه يعني انسكاب أقل على الكاونتر وهدر أقل وقت تعبئة البرطمانات والقدور والصحون",
         "سهل وقابل لإعادة الاستخدام: ركبه على فتحة الكيس، وافتح الغطاء للصب، واستخدمه مرة ثانية على أكياس جديدة",
         f"عبوة ملونة {n} قطع: الألوان المختلفة تساعدك تميز وتنظم مخزنك حسب نوع الأكل من أول نظرة",],
        ("HABBAA bag sealing clips with pour spout make pantry life easier. "
         "Instead of rolling bags or using rubber bands, clip the sealer onto any open food bag and you get a neat spout for clean, controlled pouring plus a lid that closes the bag. "
         "They are perfect for rice, lentils, beans, oats, flour, sugar, cereal, coffee, nuts, chips and pet food. "
         "Keeping bags sealed helps protect food from humidity and pests and keeps snacks crunchy for longer. "
         f"This pack includes {n} clips in assorted colours so you can organise the pantry by food type. "
         "Wash with warm soapy water and dry before reuse."),
        ("مشابك إغلاق الأكياس بفتحة صب من هبة HABBAA تسهل عليك ترتيب المخزن. "
         "بدل ما تلف الأكياس أو تستخدم المطاط، ركب المشبك على أي كيس أكل مفتوح، ويصير عندك فتحة صب مرتبة لصب نظيف ومتحكم فيه وغطاء يقفل الكيس. "
         "مناسبة للرز والعدس والفول والشوفان والطحين والسكر والكورن فليكس والقهوة والمكسرات والشيبس وأكل الحيوانات الأليفة. "
         "إغلاق الأكياس يساعد يحمي الأكل من الرطوبة والحشرات ويخلي السناكات مقرمشة أطول. "
         f"العبوة فيها {n} مشابك بألوان متنوعة عشان تنظم المخزن حسب نوع الأكل. "
         "اغسلها بماي دافي وصابون ونشفها قبل ما تستخدمها مرة ثانية."),
        "bag clips chip clips food clips pantry organizer bag sealer pour spout clip snack bag clip kitchen gadget",
        "ملقط اكياس مشبك شيبس قفل اكياس تنظيم المخزن مشبك رز ادوات مطبخ")

clip("B0GS2Z6JF8", 3)
clip("B0GS2QYDVV", 5)

put("B0DBMRWFRY",
    "HABBAA Multi-Function Kitchen and Garden Scissors with Bottle Opener, Stainless Steel Heavy Duty Shears for Meat, Chicken, Vegetables, Herbs and Flowers, Orange",
    "مقص متعدد الوظائف للمطبخ والحديقة مع فتاحة من هبة HABBAA، مقص ستانلس ستيل قوي للحم والدجاج والخضار والأعشاب والورد، برتقالي",
    ["MULTI FUNCTION DESIGN: One tool for cutting meat, chicken, fish, vegetables, herbs, flowers and packaging, plus a handy built-in bottle opener",
     "STRONG STAINLESS STEEL BLADES: Durable stainless steel blades keep a sharp edge for clean, easy cutting in the kitchen and the garden",
     "COMFORTABLE ORANGE HANDLE: A soft grip handle in a bright orange colour that is easy to hold and easy to find in a busy drawer",
     "KITCHEN AND GARDEN USE: Trim plants, cut flowers, open bags and boxes, and prepare food, all with the same reliable scissors",
     "SIMPLE CARE: Wash with warm soapy water and dry immediately to keep the blades clean and in top condition",],
    ["تصميم متعدد الوظائف: أداة وحدة لتقطيع اللحم والدجاج والسمك والخضار والأعشاب والورد والتغليف، ومعها فتاحة مدمجة",
     "شفرات ستانلس ستيل قوية: شفرات ستانلس ستيل متينة تحافظ على حدتها لقص نظيف وسهل في المطبخ والحديقة",
     "مقبض برتقالي مريح: مقبض ناعم بلون برتقالي واضح سهل المسك وسهل تلقاه في الدرج المزحوم",
     "للمطبخ والحديقة: قلم النباتات وقص الورد وافتح الأكياس والكراتين وحضر الأكل، كلها بنفس المقص",
     "عناية بسيطة: اغسله بماي دافي وصابون ونشفه على طول عشان تبقى الشفرات نظيفة وبحالة ممتازة",],
    ("The HABBAA multi-function scissors are built to handle many everyday jobs. "
     "Use them in the kitchen to cut meat, chicken, fish, vegetables and herbs, in the garden to trim plants and cut flowers, and around the house to open packages and boxes. "
     "The stainless steel blades are strong and sharp, and the built-in opener is ready whenever you need it. "
     "The bright orange handle is comfortable to hold and easy to spot. "
     "Clean with warm soapy water and dry immediately after use. Package contents: 1 x HABBAA multi-function scissors."),
    ("المقص متعدد الوظائف من هبة HABBAA مصمم لشغلات يومية كثيرة. "
     "استخدمه في المطبخ لتقطيع اللحم والدجاج والسمك والخضار والأعشاب، وفي الحديقة لتقليم النباتات وقص الورد، وفي البيت لفتح الأكياس والكراتين. "
     "شفرات الستانلس ستيل قوية وحادة، والفتاحة المدمجة جاهزة وقت ما تحتاجها. "
     "المقبض البرتقالي مريح للمسك وسهل تلقاه. "
     "نظفه بماي دافي وصابون ونشفه بعد الاستخدام مباشرة. محتوى العبوة: مقص متعدد الوظائف واحد من هبة HABBAA."),
    "kitchen shears poultry scissors garden scissors pruning scissors meat scissors herb scissors utility shears",
    "مقص لحم مقص دجاج مقص حديقة مقص تقليم مقص خضار مقص قوي مقص مطبخ")

put("B0CKWJ5B8M",
    "HABBAA Vegetable Chopper and Mandoline Slicer with 10 Interchangeable Blades, Multifunction Onion Dicer, Potato Cutter, Grater and Egg Separator for Salad and Cooking, Pink",
    "قطاعة خضار ومندولين من هبة HABBAA مع 10 شفرات قابلة للتبديل، قطاعة بصل متعددة الوظائف ومقطع بطاطس ومبشرة وفاصل بيض للسلطات والطبخ، وردي",
    ["10 BLADES IN ONE TOOL: Interchangeable blades let you dice, slice, julienne and grate vegetables and fruit in seconds for salads, soups and cooking",
     "SAVES PREP TIME: Chop onions, tomatoes, cucumbers, potatoes and carrots evenly without tears or a mess on the counter",
     "BUILT-IN CONTAINER: Cut food falls straight into the container, so you can measure, store or serve without extra bowls",
     "SAFE AND STABLE: A non-slip base keeps the chopper steady while you press, and the included accessories help keep your fingers away from the blades",
     "EASY TO CLEAN AND STORE: Blades come off easily for cleaning with the cleaning tool, and everything stores together in one compact set",],
    ["10 شفرات في أداة وحدة: شفرات قابلة للتبديل تخليك تقطع مكعبات وشرائح وأصابع وتبشر الخضار والفواكه في ثواني للسلطات والشوربات والطبخ",
     "يوفر وقت التحضير: قطع البصل والطماط والخيار والبطاطس والجزر بحجم متساوي بدون دموع وبدون فوضى على الكاونتر",
     "حاوية مدمجة: الأكل المقطع ينزل في الحاوية مباشرة، فتقدر تقيس أو تخزن أو تقدم بدون صحون زيادة",
     "آمنة وثابتة: قاعدة مانعة للانزلاق تثبت القطاعة وأنت تضغط، والملحقات المرفقة تساعد تبعد أصابعك عن الشفرات",
     "سهلة التنظيف والتخزين: الشفرات تنفك بسهولة للتنظيف مع أداة التنظيف، وكل القطع تتخزن مع بعض في طقم صغير",],
    ("The HABBAA vegetable chopper and mandoline slicer turns daily food preparation into a quick and tidy job. "
     "Choose from 10 interchangeable blades to dice onions, slice cucumbers, cut potatoes for fries, julienne carrots or grate cheese and vegetables. "
     "Place the food on the blade, press the lid and the evenly cut pieces drop into the container below. "
     "It is ideal for Saudi salads, fattoush, tabbouleh, soups, kabsa preparation and family meals. "
     "The non-slip base keeps it stable, and the parts come apart easily for cleaning. "
     "An egg separator is included for baking. Always handle blades with care. Colour: pink."),
    ("قطاعة الخضار والمندولين من هبة HABBAA تخلي تحضير الأكل اليومي سريع ومرتب. "
     "اختر من 10 شفرات قابلة للتبديل عشان تقطع البصل مكعبات، والخيار شرائح، والبطاطس أصابع للقلي، والجزر أعواد، أو تبشر الجبن والخضار. "
     "حط الأكل على الشفرة، واضغط الغطاء، وتنزل القطع المتساوية في الحاوية تحت. "
     "مثالية للسلطات والفتوش والتبولة والشوربات وتحضير الكبسة ووجبات العائلة. "
     "القاعدة المانعة للانزلاق تثبتها، والقطع تنفك بسهولة للتنظيف. "
     "معها فاصل بيض للخبيز. تعامل مع الشفرات بحذر دايم. اللون: وردي."),
    "onion chopper vegetable cutter dicer slicer grater salad chopper potato cutter food chopper kitchen gadget",
    "قطاعة بصل مقطع خضار مبشرة قطاعة سلطة مقطع بطاطس مندولين قطاعة يدوية ادوات مطبخ")

put("B0DF94KNDH",
    "HABBAA 9 Piece Cake Decorating Icing Set with 8 Interchangeable Stainless Steel Nozzles, Clear Piping Tool for Cupcakes, Cookies, Cakes and Desserts",
    "طقم تزيين الكيك والحلويات 9 قطع من هبة HABBAA مع 8 رؤوس تزيين ستانلس ستيل قابلة للتبديل، أداة تزيين شفافة للكب كيك والبسكويت والكيك والحلا",
    ["COMPLETE 9 PIECE SET: Includes a clear piping tool with 8 interchangeable decorating nozzles for stars, roses, leaves, petals, lines and dots",
     "SEE YOUR CREAM LEVEL: The transparent body lets you see how much cream or icing is left so you can refill at the right time",
     "STAINLESS STEEL TIPS: Durable stainless steel nozzles give clean, sharp shapes and change quickly with the coupler",
     "FOR ALL YOUR SWEETS: Decorate cakes, cupcakes, cookies, donuts, eclairs, kunafa trays and desserts for birthdays, Eid and family gatherings",
     "EASY TO CLEAN AND STORE: Parts separate easily for washing in warm soapy water and store together in a small space",],
    ["طقم كامل 9 قطع: فيه أداة تزيين شفافة مع 8 رؤوس قابلة للتبديل لأشكال النجمة والوردة والورقة والبتلة والخطوط والنقاط",
     "تشوف كمية الكريمة: الجسم الشفاف يوريك كم باقي من الكريمة أو الآيسنج عشان تعبي في الوقت المناسب",
     "رؤوس ستانلس ستيل: رؤوس تزيين ستانلس ستيل متينة تعطي أشكال نظيفة وواضحة وتتبدل بسرعة مع الوصلة",
     "لكل حلوياتك: زين الكيك والكب كيك والبسكويت والدونات والإكلير وصواني الكنافة والحلا لأعياد الميلاد والعيد وجمعات العائلة",
     "سهل التنظيف والتخزين: القطع تنفك بسهولة للغسيل بماي دافي وصابون وتتخزن مع بعض في مساحة صغيرة",],
    ("Give your homemade sweets a professional finish with the HABBAA 9 piece icing set. "
     "The clear piping tool comes with 8 interchangeable stainless steel nozzles, so you can pipe stars, swirls, roses, leaves, borders and writing with ease. "
     "Fill it with whipped cream, buttercream, cream cheese, chocolate ganache or mashed potato and press for a smooth, even flow. "
     "The transparent body shows the filling level, and the coupler lets you swap tips quickly without emptying the tool. "
     "Perfect for birthdays, Eid sweets, baby showers and weekend baking with the kids. "
     "Wash all parts with warm soapy water after use and dry well."),
    ("خل حلوياتك البيتية تطلع بشكل احترافي مع طقم التزيين 9 قطع من هبة HABBAA. "
     "أداة التزيين الشفافة معها 8 رؤوس ستانلس ستيل قابلة للتبديل، فتقدر تسوي نجوم ولفات وورود وأوراق وأطراف وكتابة بسهولة. "
     "عبيها بالكريمة المخفوقة أو الزبدة أو كريم تشيز أو الشوكولاتة أو البطاطس المهروسة واضغط لتدفق ناعم ومتساوي. "
     "الجسم الشفاف يوريك مستوى الحشوة، والوصلة تخليك تبدل الرؤوس بسرعة بدون ما تفضي الأداة. "
     "مثالي لأعياد الميلاد وحلويات العيد وحفلات المواليد وخبيز الويكند مع العيال. "
     "اغسل كل القطع بماي دافي وصابون بعد الاستخدام ونشفها زين."),
    "piping tips cake decorating kit icing nozzles cupcake decorating frosting tool baking supplies pastry tips",
    "ادوات تزيين الكيك رؤوس تزيين كريمة ادوات خبز تزيين كب كيك اداة تزيين حلويات")

put("B0GLG73KNJ",
    "HABBAA Silicone Ice Cube Tray with Storage Box and Lid, Flexible Easy Release Ice Mould, BPA Free Food Grade Silicone, Stackable Freezer Ice Container for Drinks, Juice and Coffee",
    "قالب مكعبات ثلج سيليكون مع صندوق تخزين وغطاء من هبة HABBAA، قالب ثلج مرن سهل الإخراج من سيليكون آمن للأكل خالي من BPA، حافظة ثلج قابلة للتكديس للمشروبات والعصير والقهوة",
    ["EASY RELEASE SILICONE: Flexible silicone tray lets you push out ice cubes one by one without twisting, cracking or hurting your fingers",
     "STORAGE BOX WITH LID: The ice falls into the storage box below and the lid keeps cubes clean and free from freezer smells",
     "FOOD GRADE MATERIAL: Made with BPA free food grade silicone, suitable for water, juice, coffee, milk, baby food and herbs",
     "STACKABLE AND SPACE SAVING: Compact design stacks neatly in the freezer and keeps a ready supply of ice for the whole family",
     "PERFECT FOR SAUDI SUMMERS: Always have ice ready for iced coffee, lemon mint, soft drinks, guests and gatherings",],
    ["سيليكون سهل الإخراج: قالب سيليكون مرن يخليك تطلع مكعبات الثلج وحدة وحدة بدون لف أو تكسير أو ألم في الأصابع",
     "صندوق تخزين بغطاء: الثلج ينزل في صندوق التخزين تحت والغطاء يخلي المكعبات نظيفة وبعيدة عن روائح الفريزر",
     "خامة آمنة للأكل: مصنوع من سيليكون آمن للأكل خالي من BPA، يناسب الماي والعصير والقهوة والحليب وأكل البيبي والأعشاب",
     "قابل للتكديس ويوفر مساحة: تصميم صغير يتكدس بترتيب في الفريزر ويوفر ثلج جاهز للعائلة كلها",
     "مثالي لصيف السعودية: خل الثلج جاهز دايم للقهوة المثلجة والليمون بالنعناع والمشروبات الغازية والضيوف والجمعات",],
    ("Never run out of ice again with the HABBAA silicone ice cube tray with storage box. "
     "Fill the flexible silicone tray with water, juice or coffee, cover it with the lid and freeze. "
     "When you need ice, press the cubes out into the storage container, which keeps them clean and ready to use. "
     "The food grade, BPA free silicone is soft, durable and easy to wash. "
     "The stackable design saves freezer space and is perfect for busy homes, offices and gatherings. "
     "Use it for iced coffee, mojitos, lemonade, smoothies, frozen herbs and baby food portions. "
     "Package contents: 1 x HABBAA silicone ice tray with storage box and lid."),
    ("لا عاد يخلص الثلج مع قالب مكعبات الثلج السيليكون وصندوق التخزين من هبة HABBAA. "
     "عبي القالب السيليكون المرن بالماي أو العصير أو القهوة، وغطيه، وحطه في الفريزر. "
     "ولما تحتاج ثلج، اضغط المكعبات تنزل في الحاوية اللي تحافظ عليها نظيفة وجاهزة. "
     "السيليكون الآمن للأكل والخالي من BPA ناعم ومتين وسهل الغسيل. "
     "التصميم القابل للتكديس يوفر مساحة الفريزر ومثالي للبيوت المزحومة والمكاتب والجمعات. "
     "استخدمه للقهوة المثلجة والموهيتو والليمون والسموذي والأعشاب المجمدة وحصص أكل البيبي. "
     "محتوى العبوة: قالب ثلج سيليكون واحد مع صندوق تخزين وغطاء من هبة HABBAA."),
    "ice tray ice mold ice cube maker freezer tray ice bin silicone mould iced coffee ice box",
    "قالب ثلج صينية ثلج مكعبات ثلج قالب سيليكون علبة ثلج فريزر قهوة مثلجة")

# ---------------- 4. Household gloves ----------------
VIN_B_EN = [
    "CLEAR VINYL GLOVES: Transparent disposable vinyl gloves that let you keep a natural feel while protecting your hands during everyday tasks",
    "POWDER FREE AND LATEX FREE: A comfortable choice for people who prefer to avoid latex and do not want powder residue on food or surfaces",
    "MULTIPURPOSE USE: Ideal for food preparation, cooking, cleaning, hair colouring, gardening, painting, pet care and handling messy jobs",
    "AMBIDEXTROUS FIT: Each glove fits either hand and slips on and off quickly, perfect for jobs where you change gloves often",
    "HYGIENIC SINGLE USE: Use once and throw away to keep your kitchen, salon or workplace clean, handy to keep in the car and the office",]
VIN_B_AR = [
    "قفازات فينيل شفافة: قفازات فينيل شفافة للاستعمال مرة وحدة تعطيك إحساس طبيعي وتحمي يدك وقت الشغلات اليومية",
    "بدون بودرة وبدون لاتكس: خيار مريح للي يفضل يبتعد عن اللاتكس وما يبي بقايا بودرة على الأكل أو الأسطح",
    "استخدامات متعددة: مثالية لتحضير الأكل والطبخ والتنظيف وصبغ الشعر والزراعة والدهان والعناية بالحيوانات والشغلات الوسخة",
    "تناسب اليدين: كل قفاز يناسب اليد اليمين واليسار ويتلبس ويتشال بسرعة، مثالي للشغلات اللي تبدل فيها القفازات كثير",
    "نظافة للاستعمال مرة وحدة: استخدمه مرة وارميه عشان يبقى مطبخك أو صالونك أو مكان شغلك نظيف، وعملي تخليه في السيارة والدوام",]
VIN_D_EN = ("HABBAA clear vinyl gloves are a practical everyday essential for home, kitchen, salon and work. "
    "They are powder free and latex free, giving a clean feel and a comfortable fit on either hand. "
    "Wear them when preparing salads, marinating meat, kneading dough, serving food, cleaning the bathroom, colouring hair, gardening or handling pet waste. "
    "The transparent material lets you see what you are doing while keeping your hands protected from dirt, oils and odours. "
    "Simply pull a glove from the box, use it and dispose of it after use. "
    "Store in a cool, dry place away from direct sunlight. Not intended for medical use.")
VIN_D_AR = ("قفازات الفينيل الشفافة من هبة HABBAA أساسية للاستخدام اليومي في البيت والمطبخ والصالون والشغل. "
    "بدون بودرة وبدون لاتكس، وتعطيك إحساس نظيف ومقاس مريح لأي يد. "
    "البسها وقت تحضير السلطات وتتبيل اللحم وعجن العجين وتقديم الأكل وتنظيف الحمام وصبغ الشعر والزراعة وتنظيف فضلات الحيوانات. "
    "الخامة الشفافة توريك اللي تسويه وتحمي يدك من الوسخ والزيوت والروائح. "
    "اسحب قفاز من العلبة، واستخدمه، وارمه بعد الاستخدام. "
    "تحفظ في مكان بارد وجاف بعيد عن الشمس المباشرة. غير مخصصة للاستخدام الطبي.")
put("B0FFCBM1D9",
    "HABBAA Disposable Clear Vinyl Gloves, Powder Free and Latex Free Multipurpose Gloves for Food Preparation, Cooking, Cleaning and Hair Colouring, Strong Transparent Gloves, Size XL",
    "قفازات فينيل شفافة للاستعمال مرة واحدة من هبة HABBAA، قفازات متعددة الاستخدامات بدون بودرة وبدون لاتكس لتحضير الأكل والطبخ والتنظيف وصبغ الشعر، قفازات شفافة قوية، مقاس XL",
    VIN_B_EN, VIN_B_AR, VIN_D_EN, VIN_D_AR,
    "disposable gloves plastic gloves food gloves kitchen gloves cleaning gloves hair dye gloves transparent gloves",
    "قفازات بلاستيك قفازات اكل قفازات مطبخ قفازات تنظيف قفازات صبغة قفازات شفافة جوانتي")
put("B0FFC5XNPZ",
    "HABBAA Clear Vinyl Gloves 70 Count, Powder Free Disposable Transparent Gloves for Food Handling, Cooking, Cleaning, Salon and Household Tasks, Size Large",
    "قفازات فينيل شفافة 70 قطعة من هبة HABBAA، قفازات بدون بودرة للاستعمال مرة واحدة للتعامل مع الأكل والطبخ والتنظيف والصالون وشغل البيت، مقاس لارج",
    VIN_B_EN, VIN_B_AR, VIN_D_EN, VIN_D_AR,
    "disposable gloves plastic gloves food gloves kitchen gloves cleaning gloves hair dye gloves transparent gloves",
    "قفازات بلاستيك قفازات اكل قفازات مطبخ قفازات تنظيف قفازات صبغة قفازات شفافة جوانتي")
put("B0FR562QLP",
    "HABBAA Reusable Household Rubber Gloves, Two Tone Waterproof Cleaning Gloves with Non-Slip Grip for Dishwashing, Kitchen, Bathroom and Laundry, Red and Cream",
    "قفازات تنظيف مطاطية منزلية قابلة لإعادة الاستخدام من هبة HABBAA، قفازات بلونين مقاومة للماء بمسكة مانعة للانزلاق لغسيل الصحون والمطبخ والحمام والغسيل، أحمر وكريمي",
    ["PROTECTS YOUR HANDS: Waterproof rubber gloves keep your hands dry and shielded from hot water, detergents and dirt while you clean",
     "NON-SLIP GRIP: A textured palm and fingers help you hold wet plates, glasses and pots firmly, reducing slips and breakages",
     "LONG CUFF DESIGN: The extended two tone cuff helps stop water running down your arms when washing dishes or cleaning floors",
     "REUSABLE AND DURABLE: Strong, flexible rubber that can be washed and reused many times for dishwashing, bathroom, kitchen and laundry tasks",
     "COMFORTABLE FIT: Soft flexible material that moves with your fingers, so you can work longer without tired hands",],
    ["تحمي يدك: قفازات مطاطية مقاومة للماء تخلي يدك ناشفة ومحمية من الماي الحار والمنظفات والوسخ وقت التنظيف",
     "مسكة مانعة للانزلاق: كف وأصابع بملمس خاص تساعدك تمسك الصحون والكاسات والقدور المبللة بثبات وتقلل الطيحات والكسر",
     "تصميم بكم طويل: الكم الطويل بلونين يساعد يمنع الماي ينزل على يدك وقت غسيل الصحون أو تنظيف الأرض",
     "قابلة لإعادة الاستخدام ومتينة: مطاط قوي ومرن ينغسل ويرجع ينستخدم مرات كثيرة لغسيل الصحون والحمام والمطبخ والغسيل",
     "مقاس مريح: خامة ناعمة ومرنة تتحرك مع أصابعك، فتقدر تشتغل وقت أطول بدون تعب في اليد",],
    ("HABBAA reusable household rubber gloves are made for everyday cleaning around the home. "
     "The waterproof rubber keeps your hands dry and protected from hot water, dish soap, bleach based cleaners and grime. "
     "A non-slip textured grip helps you hold wet dishes and glasses securely, and the long two tone cuff keeps water away from your wrists. "
     "Use them for washing dishes, cleaning the kitchen and bathroom, scrubbing floors, hand washing clothes, car washing and gardening. "
     "After use, rinse the gloves, turn them inside out to dry and store them in a dry place. Colour: red and cream."),
    ("قفازات التنظيف المطاطية من هبة HABBAA مصنوعة للتنظيف اليومي في البيت. "
     "المطاط المقاوم للماي يخلي يدك ناشفة ومحمية من الماي الحار وصابون الصحون والمنظفات والوسخ. "
     "المسكة المانعة للانزلاق تساعدك تمسك الصحون والكاسات المبللة بأمان، والكم الطويل بلونين يبعد الماي عن معصمك. "
     "استخدمها لغسيل الصحون وتنظيف المطبخ والحمام وفرك الأرض وغسيل الملابس باليد وغسيل السيارة والزراعة. "
     "بعد الاستخدام، اشطف القفازات واقلبها عشان تنشف وخزنها في مكان جاف. اللون: أحمر وكريمي."),
    "dishwashing gloves kitchen gloves cleaning gloves rubber gloves washing up gloves bathroom gloves long gloves",
    "قفازات غسيل صحون قفازات مطبخ قفازات تنظيف جوانتي مطاط قفازات حمام قفازات طويلة")

# ---------------- 5. Car tire care ----------------
put("B0FN4NWWK7",
    "HABBAA Tire Shine Foam Spray, 3 in 1 Tyre Cleaner with Deep Black Shine and Protection, Easy Spray and Wipe Car Tire Dressing for Cars, SUVs and Motorbikes",
    "بخاخ فوم تلميع الإطارات من هبة HABBAA، منظف كفرات 3 في 1 يعطي لمعة سوداء ويحمي الإطار، تلميع سهل بالرش والمسح للسيارات والجيبات والدبابات",
    ["3 IN 1 FORMULA: Cleans, shines and protects your tyres in one easy step, giving them a fresh deep black look",
     "RICH ACTIVE FOAM: The foam clings to the tyre wall, lifting dust and road grime so you can wipe it away easily",
     "LONG LASTING SHINE: Leaves a glossy finish that makes your car look newly washed and well cared for",
     "QUICK AND EASY: Shake well, spray evenly on a clean tyre, let the foam work, then wipe with a cloth or sponge if needed",
     "FOR ALL VEHICLES: Suitable for car, SUV, pickup and motorbike tyres, a must have in your car care kit",],
    ["تركيبة 3 في 1: تنظف وتلمع وتحمي كفراتك بخطوة وحدة سهلة وتعطيها شكل أسود لامع وجديد",
     "فوم فعال وكثيف: الفوم يلتصق على جدار الكفر ويرفع الغبار ووسخ الطريق فتمسحه بسهولة",
     "لمعة تدوم: يعطي لمعة واضحة تخلي سيارتك كأنها توها مغسولة ومعتنى فيها",
     "سريع وسهل: رج العلبة زين، رش بالتساوي على كفر نظيف، خل الفوم يشتغل، وبعدها امسح بقطعة قماش أو إسفنجة إذا احتجت",
     "لكل المركبات: مناسب لكفرات السيارات والجيبات والونيتات والدبابات، لازم يكون في عدة العناية بسيارتك",],
    ("Give your vehicle the finishing touch with HABBAA tire shine foam. "
     "The 3 in 1 foam formula cleans road dust and light dirt, adds a deep black shine and helps protect the rubber from fading caused by sun and heat. "
     "Shake the can, spray an even layer on a clean, dry tyre and let the foam spread over the sidewall. "
     "Wipe off excess foam with a cloth or sponge for a neat finish. "
     "Use it after every car wash for a showroom look. "
     "Avoid spraying on brake discs, pedals or painted surfaces and keep away from children and heat. "
     "Suitable for cars, SUVs, pickups and motorbikes."),
    ("خل سيارتك تكمل لمعتها مع فوم تلميع الإطارات من هبة HABBAA. "
     "تركيبة الفوم 3 في 1 تنظف غبار الطريق والوسخ الخفيف، وتعطي لمعة سوداء قوية، وتساعد تحمي المطاط من البهتان بسبب الشمس والحرارة. "
     "رج العلبة، ورش طبقة متساوية على كفر نظيف وناشف، وخل الفوم ينتشر على جدار الكفر. "
     "امسح الفوم الزايد بقطعة قماش أو إسفنجة عشان يطلع الشكل مرتب. "
     "استخدمه بعد كل غسلة عشان سيارتك تطلع كأنها من المعرض. "
     "تجنب الرش على الفرامل أو الدواسات أو الأسطح المصبوغة، وأبعده عن الأطفال والحرارة. "
     "مناسب للسيارات والجيبات والونيتات والدبابات."),
    "tyre shine tire cleaner tire dressing car wash foam tire polish car care spray wheel cleaner",
    "ملمع كفرات منظف كفرات تلميع اطارات بخاخ كفرات غسيل سيارات عناية بالسيارة ملمع اطارات")

put("B0FN4LPXXV",
    "HABBAA Car Jack Stands 3 Ton Capacity (6600 lbs), Heavy Duty Adjustable Safety Axle Stands with Locking Handle for Cars, SUVs and Home Garage Maintenance, 1 Pair",
    "حامل رفع سيارة 3 طن من هبة HABBAA، رافعة أمان قوية قابلة لتعديل الارتفاع بمقبض قفل للسيارات والجيبات وصيانة الكراج في البيت، زوج",
    ["3 TON CAPACITY: Heavy duty stands rated up to 3 tons (6600 lbs) to support your car safely after lifting it with a jack",
     "ADJUSTABLE HEIGHT: The ratchet bar adjusts to different working heights, and the locking handle holds it securely in place",
     "STABLE WIDE BASE: A wide base with reinforced steel plates gives a firm and stable footing on garage floors",
     "SAFER MAINTENANCE: Ideal for changing tyres, oil changes, brake work and checking under the car at home or in the workshop",
     "ESSENTIAL GARAGE TOOL: Always use the stands in pairs on flat, solid ground and never work under a car supported by a jack only",],
    ["حمولة 3 طن: حوامل قوية تتحمل حتى 3 طن (6600 رطل) عشان تسند سيارتك بأمان بعد ما ترفعها بالجك",
     "ارتفاع قابل للتعديل: العمود يتعدل لارتفاعات شغل مختلفة، ومقبض القفل يثبته بإحكام",
     "قاعدة عريضة وثابتة: قاعدة عريضة بألواح حديد معززة تعطي ثبات قوي على أرضية الكراج",
     "صيانة أكثر أمان: مثالية لتغيير الكفرات وتغيير الزيت وشغل الفرامل وفحص تحت السيارة في البيت أو الورشة",
     "أداة أساسية للكراج: استخدم الحوامل دايم زوج على أرض مستوية وقوية، ولا تشتغل تحت سيارة مرفوعة بالجك بس",],
    ("HABBAA 3 ton jack stands are designed to support your vehicle securely while you work. "
     "After lifting the car with a jack, place the stands under the recommended support points, adjust the height and lock the handle. "
     "The strong steel construction and wide base provide stable support for cars, SUVs and light trucks up to 3 tons. "
     "They are perfect for home mechanics changing tyres or oil, checking brakes, or working on suspension. "
     "For your safety, always use stands in pairs on level, hard ground, never exceed the rated capacity and follow your vehicle manual for lifting points."),
    ("حوامل الرفع 3 طن من هبة HABBAA مصممة تسند سيارتك بأمان وأنت تشتغل. "
     "بعد ما ترفع السيارة بالجك، حط الحوامل تحت نقاط الإسناد المناسبة، وعدل الارتفاع، وقفل المقبض. "
     "التصنيع الحديدي القوي والقاعدة العريضة يعطون إسناد ثابت للسيارات والجيبات والونيتات الخفيفة لحد 3 طن. "
     "مثالية للي يصلح سيارته في البيت ويغير الكفرات أو الزيت أو يفحص الفرامل أو يشتغل على المساعدات. "
     "عشان سلامتك، استخدم الحوامل دايم زوج على أرض مستوية وقوية، ولا تتجاوز الحمولة المحددة، واتبع دليل سيارتك لنقاط الرفع."),
    "jack stand axle stand car lift car stand garage tools tyre change tool vehicle support stand",
    "حامل جك رافعة سيارة جك سيارة ادوات كراج تغيير كفرات حامل سيارة عدة سيارة")

put("B0FNX5Z75G",
    "HABBAA Cordless Tyre Inflator, Portable Air Compressor 150 PSI with Digital Pressure Gauge, LED Light and Auto Shut-Off, Rechargeable Air Pump for Car, Bike, Motorcycle and Balls",
    "منفاخ كفرات لاسلكي من هبة HABBAA، كمبروسر هواء محمول 150 PSI بشاشة ضغط رقمية وإضاءة LED وإيقاف تلقائي، منفاخ قابل للشحن للسيارة والسيكل والدباب والكور",
    ["CORDLESS AND RECHARGEABLE: A built-in 6000 mAh rechargeable battery lets you inflate tyres anywhere, with no need to start the engine or find a socket",
     "DIGITAL PRESSURE GAUGE: Set your target pressure on the LCD screen in PSI, KPA, BAR or KG/CM2 and see the live reading while it inflates",
     "AUTO SHUT-OFF: The pump stops automatically when the preset pressure is reached, helping prevent over inflation",
     "BRIGHT LED LIGHT: Built-in LED light helps you check and inflate tyres at night or in dark parking areas",
     "MULTI USE WITH 4 NOZZLES: Comes with extra nozzles for car, bike and motorcycle tyres, footballs, basketballs and inflatables, includes USB cable, car power cable and bag",],
    ["لاسلكي وقابل للشحن: بطارية مدمجة 6000 مللي أمبير تخليك تنفخ الكفرات في أي مكان بدون ما تشغل السيارة أو تدور فيش",
     "شاشة ضغط رقمية: حدد الضغط اللي تبيه على شاشة LCD بوحدة PSI أو KPA أو BAR أو KG/CM2 وشوف القراءة وهو ينفخ",
     "إيقاف تلقائي: المنفاخ يوقف لحاله لما يوصل للضغط المحدد، ويساعد يمنع النفخ الزايد",
     "إضاءة LED قوية: إضاءة LED مدمجة تساعدك تفحص وتنفخ الكفرات بالليل أو في المواقف المظلمة",
     "استخدامات متعددة مع 4 رؤوس: معه رؤوس إضافية لكفرات السيارة والسيكل والدباب والكور والألعاب المنفوخة، ومعه كيبل USB وكيبل ولاعة السيارة وشنطة",],
    ("Keep your tyres at the right pressure wherever you are with the HABBAA cordless tyre inflator. "
     "This portable air compressor delivers up to 150 PSI and runs on a rechargeable battery, so you can top up your tyres at home, at work or on a desert trip without a socket. "
     "Simply connect the hose, choose your target pressure on the digital display and press start. "
     "The pump stops automatically at the set pressure, and the LED light makes night use easy. "
     "Four extra nozzles let you inflate bicycle and motorcycle tyres, balls and pool toys. "
     "In the box: inflator, air hose, 4 nozzles, USB charging cable, car power cable and storage bag. "
     "Correct tyre pressure supports safer driving, better fuel economy and longer tyre life."),
    ("خل ضغط كفراتك مضبوط وين ما كنت مع منفاخ الكفرات اللاسلكي من هبة HABBAA. "
     "الكمبروسر المحمول هذا يعطي لحد 150 PSI ويشتغل ببطارية قابلة للشحن، فتقدر تعبي كفراتك في البيت أو الدوام أو الكشتة بدون فيش. "
     "بس وصل الخرطوم، واختر الضغط اللي تبيه على الشاشة الرقمية، واضغط تشغيل. "
     "المنفاخ يوقف لحاله عند الضغط المحدد، وإضاءة LED تسهل الاستخدام بالليل. "
     "أربعة رؤوس إضافية تخليك تنفخ كفرات السيكل والدباب والكور وألعاب المسبح. "
     "في العلبة: المنفاخ وخرطوم الهواء و4 رؤوس وكيبل شحن USB وكيبل ولاعة السيارة وشنطة تخزين. "
     "الضغط الصحيح للكفرات يساعد على قيادة أكثر أمان وتوفير بنزين وعمر أطول للكفرات."),
    "air compressor tire pump car inflator portable pump air pump for car cordless pump tyre pressure pump",
    "منفاخ سيارة كمبروسر هواء منفاخ كفرات محمول مضخة هواء منفاخ لاسلكي منفاخ كور جهاز نفخ")
