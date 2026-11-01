import openpyxl,json,sys
SEO='/home/claude/habbaa-product-images/seo/'
A='[marketplace_id=A17E79C6D8DWNP][language_tag=ar_AE]#'
PEN={'أزرق':'أبيض بلمسة زرقاء','أحمر':'أبيض بلمسة حمراء','أسود':'أبيض بلمسة سوداء','أخضر':'أبيض بلمسة خضراء'}
FAMS={
 'BOTTLE':[('HABBAA-BOT600WC-PARENT',['B9-22HF-M44C','DW-1S5Z-5WFD']),
           ('HABBAA-BOT500MS-PARENT',['C1-RRPE-JA9K','N3-U06P-RVJ6','U9-QYB1-MFHF']),
           ('HABBAA-BOT500WH-PARENT',['E9-JXD3-8V44','H4-M7QM-P64W'])],
 'BADGE_HOLDER':[('HABBAA-REELSQ-PARENT',['7F-72AD-NHU8','EB-BY8Z-QQ2C']),
           ('HABBAA-REEL100-PARENT',['K3-Z50G-S31L','DO-FB2Q-KS6L','N6-FHZ5-XSTQ','ZF-9QP9-SV7V']),
           ('HABBAA-IDHOLD-PARENT',['V0-PFW8-SMUA','0X-13O1-F6VD','ZW-64HV-KXCU','7V-9LCN-VOOI','2J-2ZA7-M5BD'])],
 'WRITING_INSTRUMENT':[('HABBAA-PEN147-PARENT',['4N-FT85-ZYZ5','4W-PKYU-ET8T']),
           ('HABBAA-PEN140-PARENT',['HC-WHB3-RITX','2A-9F2P-WJ8A','X1-JWZK-6JPP','RY-6NGG-HU7V'])],
 'BACKPACK':[('HABBAA-ROPEBAG-PARENT',['7S-5D8X-XFKR','XO-73PL-62D5'])],
}
report=[]
for PT,fams in FAMS.items():
    src=SEO+f'AR-SEO-{PT}.xlsm'
    wr=openpyxl.load_workbook(src,read_only=True)['النموذج']
    hdr=list(next(wr.iter_rows(min_row=5,max_row=5,values_only=True))); I={h:i for i,h in enumerate(hdr) if h}
    R={r[0]:r for r in wr.iter_rows(min_row=7,values_only=True) if r[0]}
    def c(p):
        m=[i for k,i in I.items() if k.startswith(p)]; assert m,(PT,p); return m[0]
    ti,di,ki=c('item_name'),c('product_description'),c('generic_keyword')
    bi=[c(f'bullet_point{A}{n}.value') for n in range(1,6)]
    col=c(f'color{A}1.value'); br=c('brand['); coo=c('country_of_origin'); bat=c('batteries_required')
    dg=c('supplier_declared_dg_hz_regulation[marketplace_id=A17E79C6D8DWNP]#1')
    wb=openpyxl.load_workbook(src,keep_vba=True); ws=wb['النموذج']
    for r in range(7,ws.max_row+1):
        for cc in range(1,ws.max_column+1): ws.cell(r,cc).value=None
    r=7
    for psku,kids in fams:
        ref=R[kids[0]]; parts=[p.strip() for p in ref[ti].split('،')]
        bases=set()
        cols=[]
        for k in kids:
            pp=[p.strip() for p in R[k][ti].split('،')]
            bases.add('، '.join(pp[:-1])); last=pp[-1]
            if last.startswith('بلمسة '): last=PEN[last.split(' ',1)[1]]
            cols.append(last)
        assert len(bases)==1,(psku,bases); assert len(set(cols))==len(cols),(psku,cols)
        bt=bases.pop()
        S=lambda cc,v: ws.cell(r,cc+1).__setattr__('value',v)
        S(0,psku);S(1,PT);S(2,'إنشاء أو استبدال (تحديث كامل)');S(3,'الأصل');S(5,'اللون')
        S(ti,bt);S(di,ref[di]);S(ki,ref[ki])
        for b in bi: S(b,ref[b])
        S(br,'HABBAA');S(coo,'الصين');S(bat,'لا');S(dg,'غير قابل للتطبيق')
        report.append((PT,psku,bt)); r+=1
        for k,cl in zip(kids,cols):
            S(0,k);S(1,PT);S(2,'تحرير (تحديث جزئي)');S(3,'طفل');S(4,psku);S(5,'اللون');S(col,cl)
            report.append((PT,'  '+k,cl)); r+=1
    wb.save(f'VAR-{PT}.xlsm')
for x in report: print(*x)
