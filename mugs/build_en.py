import openpyxl,json,re
import sys
PT=sys.argv[1]
SRC=f'/home/claude/habbaa-product-images/seo/AR-SEO-{PT}.xlsm'
BAN=r'(ترمس|ثرمس|ثيرموس|ترموس|thermos)'
def cl(s):
    if s is None: return s
    s=re.sub(r'،\s*مج سفر وترمس قهوة','',s)
    s=re.sub(r'\s*و?'+BAN+r'\s*(قهوة)?',' ',s,flags=re.I)
    return re.sub(r'[ \t]{2,}',' ',s).strip()
C8=json.load(open('/home/claude/habbaa-product-images/seo/C8.json'))
CJ=json.load(open('/home/claude/habbaa-product-images/seo/content.json'))
rows={r['sku']:r for r in json.load(open('rows.json'))}
_w=openpyxl.load_workbook(SRC,read_only=True)['النموذج']
_h=[c for c in next(_w.iter_rows(min_row=5,max_row=5,values_only=True))]
_I={h:i for i,h in enumerate(_h) if h}
_A='[marketplace_id=A17E79C6D8DWNP][language_tag=ar_AE]#'
TPL={}
for row in _w.iter_rows(min_row=7,values_only=True):
    if row[0]: TPL[row[0]]=dict(pt=row[1],t=row[_I['item_name'+_A+'1.value']],d=row[_I['product_description'+_A+'1.value']],k=row[_I['generic_keyword'+_A+'1.value']],b=[row[_I[f'bullet_point{_A}{i}.value']] for i in range(1,6)])
items=[]
for a,v in C8.items():
    if re.search(BAN,json.dumps(v,ensure_ascii=False),re.I): items.append((a,v['sku'],v))
for a,sku in [('B0HP6SLZZ8','33-GGQA-GL64'),('B0HP6SSPQJ','WW-S1S1-XWKM'),('B0HP6S2DQK','0H-QUGM-6U9H'),('B0HP6S2DQK','FR-WZL5-ROIV'),('B0HP6R36YH','1O-OMMS-G7E4'),('B0HP6V6Z4F','5U-JH55-4AHR'),('B0FF3GZP1G','4P-5CWG-UNS5')]:
    items.append((a,sku,CJ[a]))
items.append(('B0HP6YH3P3','NY-XQAO-590O',C8['B0HP6YH3P3']))
out=[]
for a,sku,v in items:
    e=v['en']; en=dict(t=cl(e['t']),d=cl(e['d']),k=cl(e['k']),b=[cl(x) for x in e['b']])
    if PT=='BOTTLE' and sku not in TPL: continue
    if PT!='BOTTLE' and 'Water Bottle' in v['en']['t']: continue
    r=rows.get(sku); tp=TPL.get(sku)
    ar=dict(t=r['t'],d=r['d'],k=r['k'],b=r['b']) if r else dict(t=cl(tp['t']),d=cl(tp['d']),k=cl(tp['k']),b=[cl(x) for x in tp['b'] if x]) if tp else dict(t=cl(v['ar']['t']),d=cl(v['ar']['d']),k=cl(v['ar']['k']),b=[cl(x) for x in v['ar']['b']])
    out.append(dict(asin=a,sku=sku,en=en,ar=ar))
s=json.dumps(out,ensure_ascii=False)
assert not re.search(BAN,s,re.I), re.findall('.{20}'+BAN+'.{20}',s,re.I)[:3]
wb=openpyxl.load_workbook(SRC,keep_vba=True); ws=wb['النموذج']
hdr=[c.value for c in ws[5]]; I={h:i+1 for i,h in enumerate(hdr) if h}
def col(k): return I[k]
AR='[marketplace_id=A17E79C6D8DWNP][language_tag=ar_AE]#1.value'
keys={'t':'item_name','d':'product_description','k':'generic_keyword'}
# add en_AE columns at the end, cloning ar_AE label
nc=ws.max_column
ENC={}
def addcol(base,idx=1):
    global nc
    nc+=1
    k=f'{base}[marketplace_id=A17E79C6D8DWNP][language_tag=en_AE]#{idx}.value'
    ark=k.replace('en_AE','ar_AE')
    ws.cell(4,nc).value=(ws.cell(4,I[ark]).value or base)+' (EN)'
    ws.cell(5,nc).value=k
    return nc
for f,b in keys.items(): ENC[f]=addcol(b)
ENB=[addcol('bullet_point',i) for i in range(1,6)]
for r in range(7,ws.max_row+1):
    for c in range(1,ws.max_column+1): ws.cell(r,c).value=None
for n,o in enumerate(out):
    r=7+n
    ws.cell(r,1).value=o['sku']; ws.cell(r,2).value=PT; ws.cell(r,3).value='تحرير (تحديث جزئي)'
    for f,b in keys.items():
        ws.cell(r,col(b+AR)).value=o['ar'][f]; ws.cell(r,ENC[f]).value=o['en'][f]
    for i in range(5):
        ws.cell(r,col(f'bullet_point[marketplace_id=A17E79C6D8DWNP][language_tag=ar_AE]#{i+1}.value')).value=o['ar']['b'][i] if i<len(o['ar']['b']) else None
        ws.cell(r,ENB[i]).value=o['en']['b'][i] if i<len(o['en']['b']) else None
wb.save(f'EN-FIX-{PT}.xlsm')
json.dump(out,open(f'en_fix_{PT}.json','w'),ensure_ascii=False,indent=1)
print(len(out),nc)
for o in out[:3]+out[-9:]: print(o['sku'],'|',o['en']['t'][:70],'|',o['ar']['t'][:50])
