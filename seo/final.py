from content5 import C
END_EN = "Every HABBAA order is checked before shipping so it reaches you in excellent condition. If you have any question about size, quantity or use, contact us through Amazon and our team will be happy to help. HABBAA offers practical, quality everyday products for homes, offices and businesses."
END_AR = "كل طلب من هبة HABBAA نتأكد منه قبل الشحن عشان يوصلك بحالة ممتازة. وإذا عندك أي سؤال عن المقاس أو الكمية أو طريقة الاستخدام، تواصل معنا عن طريق أمازون وفريقنا يسعد يساعدك. هبة HABBAA تقدم منتجات يومية عملية وبجودة عالية للبيوت والمكاتب والأعمال."
def b2s(b, ar):
    if ':' in b:
        h, r = b.split(':', 1); r = r.strip()
        h = h.strip().title() if not ar else h.strip()
        s = f"{h}: {r}"
    else: s = b
    return s if s.endswith(('.', '،', '!')) else s + '.'
for a, v in C.items():
    for L in ('en', 'ar'):
        x = v[L]
        if x.get('_aug'): continue
        ar = L == 'ar'
        head = "أبرز المميزات:" if ar else "Key features:"
        x['d'] = x['d'].strip() + "\n\n" + head + "\n" + "\n".join("- " + b2s(b, ar) for b in x['b']) + "\n\n" + (END_AR if ar else END_EN)
        if len(x['d']) > 1990:
            x['d'] = x['d'].split("\n\n" + head)[0] + "\n\n" + (END_AR if ar else END_EN)
        x['_aug'] = 1
