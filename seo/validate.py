import json,re
from final import C
fams=json.load(open('fams.json'))
allas=[a for v in fams.values() for a in v]
miss=[a for a in allas if a not in C]; extra=[a for a in C if a not in allas]
print('total',len(C),'need',len(allas),'missing',miss,'extra',extra)
bad=[]
promo=re.compile(r'\b(best|free|sale|discount|eco|biodegradable|guarantee|#1|cure|treat)\b',re.I)
for a in allas:
  if a not in C: continue
  for L in ('en','ar'):
    x=C[a][L]
    if not(60<=len(x['t'])<=200): bad.append((a,L,'title',len(x['t'])))
    if len(x['b'])!=5: bad.append((a,L,'nb',len(x['b'])))
    for b in x['b']:
      if len(b)>500 or len(b)<45: bad.append((a,L,'blen',len(b),b[:40]))
    if len(x["d"])<1000 or len(x["d"])>2000: bad.append((a,L,'dlen',len(x['d'])))
    kb=len(x['k'].encode())
    if kb>249: bad.append((a,L,'kbytes',kb))
    if 'HABBAA' not in x['t']: bad.append((a,L,'nobrand'))
    if L=='en' and promo.search(x['t']+' '.join(x['b'])+x['d']): bad.append((a,L,'promo',promo.search(x['t']+' '.join(x['b'])+x['d']).group()))
    if '  ' in x['t'] or '  ' in x['d']: bad.append((a,L,'dblspace'))
for b in bad: print(b)
print(len(bad))
import statistics
print('desc len median en', statistics.median(len(C[a]['en']['d']) for a in allas), 'ar', statistics.median(len(C[a]['ar']['d']) for a in allas))
json.dump({a:C[a] for a in allas},open('content.json','w'),ensure_ascii=False,indent=0)
