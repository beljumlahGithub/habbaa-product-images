import openpyxl
SEO='/home/claude/habbaa-product-images/seo/'
def rows(f):
    ws=openpyxl.load_workbook(SEO+f,read_only=True)['النموذج']
    return {r[0]:r for r in ws.iter_rows(min_row=7,values_only=True) if r[0]}
H=rows('AR-SEO-HAT.xlsm'); H3=rows('AR-SEO-HAT3.xlsm')
wb=openpyxl.load_workbook(SEO+'AR-SEO-HAT.xlsm',keep_vba=True); ws=wb['النموذج']
hdr=[c.value for c in ws[5]]; I={h:i+1 for i,h in enumerate(hdr) if h}
def col(p): 
    m=[v for k,v in I.items() if k.startswith(p)]; assert m,p; return m[0]
C=dict(t=col('item_name'),d=col('product_description'),k=col('generic_keyword'),br=col('brand['),
       color=col('color[marketplace_id=A17E79C6D8DWNP][language_tag=ar_AE]#1.value'),coo=col('country_of_origin'),
       bat=col('batteries_required'),fab=col('fabric_type'),dg=col('supplier_declared_dg_hz_regulation[marketplace_id=A17E79C6D8DWNP]#1'))
CB=[col(f'bullet_point[marketplace_id=A17E79C6D8DWNP][language_tag=ar_AE]#{i}') for i in range(1,6)]
FAM=[
 ('HABBAA-CAP6P-PARENT', H['HM-BM1G-8R5C'], 'الصين',
  [('XC-TNHL-TKNV','كحلي'),('HM-BM1G-8R5C','أبيض'),('6O-PICR-B8WS','أزرق'),('0D-OTGX-1FLH','أسود')]),
 ('HABBAA-CAPSAT-PARENT', H3['FC-C8Y3-2PL0'], 'الصين',
  [('FC-C8Y3-2PL0','أبيض بحافة كحلي'),('RM-C3D3-X8UX','أبيض بحافة زرقاء'),('LN-DBV6-GXMZ','أبيض بحافة عنابي')]),
]
for r in range(7,ws.max_row+1):
    for c in range(1,ws.max_column+1): ws.cell(r,c).value=None
r=7; out=[]
for psku,ref,coo,kids in FAM:
    t=ref[C['t']-1]; parts=[p.strip() for p in t.split('،')]
    assert parts[-1] in [c for _,c in kids], parts[-1]
    bt='، '.join(parts[:-1])
    ws.cell(r,1).value=psku; ws.cell(r,2).value='HAT'; ws.cell(r,3).value='إنشاء أو استبدال (تحديث كامل)'
    ws.cell(r,4).value='الأصل'; ws.cell(r,6).value='اللون'
    ws.cell(r,C['t']).value=bt; ws.cell(r,C['d']).value=ref[C['d']-1]; ws.cell(r,C['k']).value=ref[C['k']-1]
    for c in CB: ws.cell(r,c).value=ref[c-1]
    ws.cell(r,C['br']).value='HABBAA'
    if coo: ws.cell(r,C['coo']).value=coo
    ws.cell(r,C['fab']).value='قطن' if 'CAP6P' in psku else 'ساتان'
    ws.cell(r,C['bat']).value='لا'; ws.cell(r,C['dg']).value='غير قابل للتطبيق'
    out.append((psku,bt)); r+=1
    for sku,colr in kids:
        ws.cell(r,1).value=sku; ws.cell(r,2).value='HAT'; ws.cell(r,3).value='تحرير (تحديث جزئي)'
        ws.cell(r,4).value='طفل'; ws.cell(r,5).value=psku; ws.cell(r,6).value='اللون'; ws.cell(r,C['color']).value=colr
        out.append((sku,colr)); r+=1
wb.save('CAPS-VARIATIONS.xlsm')
for o in out: print(o)
print(C)
