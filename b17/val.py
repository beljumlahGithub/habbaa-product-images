import json, re, sys, collections, importlib
mods = sys.argv[1:] or ['c1']
C = {}
for m in mods:
    C.update(importlib.import_module(m).C)
EMO = re.compile('[\U0001F000-\U0001FFFF☀-➿⬀-⯿️]')
promo = re.compile(r'\b(best|free|sale|discount|eco[- ]?friendly|biodegradable|guarantee|warranty|#1|cure|treat|100%|top quality|premium quality|certified|approved|compostable|recyclable|bpa|leak[- ]?proof|healthy)\b', re.I)
arpromo = re.compile(r'(ضمان|الأفضل|مجاني|خصم|معتمد|شهادة|100%|رقم 1|صديق للبيئة|صديقة للبيئة|للتحلل|التدوير|صحي\b|ميلاد)')
bad = []
for a, v in C.items():
    for L in ('en', 'ar'):
        x = v[L]
        if not (60 <= len(x['t']) <= 200): bad.append((a, L, 'title', len(x['t'])))
        if len(x['b']) != 5: bad.append((a, L, 'nb', len(x['b'])))
        for b in x['b']:
            if len(b) > 480 or len(b) < 40: bad.append((a, L, 'blen', len(b), b[:30]))
        if not ((700 if L=='en' else 500) <= len(x['d']) <= 2000): bad.append((a, L, 'dlen', len(x['d'])))
        kb = len(x['k'].encode())
        if kb > 249: bad.append((a, L, 'kbytes', kb))
        if not x['t'].startswith('HABBAA'): bad.append((a, L, 'nobrand'))
        alltxt = x['t'] + ' ' + ' '.join(x['b']) + ' ' + x['d']
        if EMO.search(alltxt + x['k']): bad.append((a, L, 'emoji'))
        m = (promo if L == 'en' else arpromo).search(alltxt)
        if m: bad.append((a, L, 'promo', m.group()))
        if '  ' in alltxt: bad.append((a, L, 'dblspace'))
        w = collections.Counter(re.findall(r'\w+', x['t'].lower()))
        rep = [k for k, n in w.items() if n > 2 and len(k) > 1]
        if rep: bad.append((a, L, 'titlerep', rep))
        if re.search(r'[<>]', alltxt): bad.append((a, L, 'html'))
        if L == 'ar':
            flat = re.sub(r'[\u064B-\u0652\s\u060C.,:;()\-]', '', alltxt + x['k'])
            for z in ['مص','كس','لعن','بز','ثدي','علق','هور','جن','نيك','لسبو','فوهة']:
                if z in flat: bad.append((a, L, 'arfilter', z))
for b in bad: print(b)
print('products', len(C), 'issues', len(bad))
