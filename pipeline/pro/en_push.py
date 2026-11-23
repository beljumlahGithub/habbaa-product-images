import json,sys,os,subprocess
D=os.path.dirname(os.path.abspath(__file__));R=os.path.join(D,'..','..')
a=json.load(open(R+'/aplus/pro/alts.json'))
for f in sys.argv[1:]:
    t=json.load(open(f'{D}/en_copy/{f}.json'))
    al=['HABBAA '+' '.join(t['hero']['head'])+': '+t['hero']['sub'],t['feat']['title']+': '+', '.join(x[0] for x in t['feat']['feats']),t['steps']['title']+': '+', '.join(x[0] for x in t['steps']['steps']),t['uses']['title']+': '+', '.join(t['uses']['tiles']),'Specifications: '+', '.join(f'{k} {v}' for k,v in t['specs']['rows'][:3])]
    a[f+'EN']=[s[:100] for s in al]
json.dump(a,open(R+'/aplus/pro/alts.json','w'),ensure_ascii=False,indent=1)
m="Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>\nClaude-Session: https://claude.ai/code/session_01Ad5C64gfiPaS1cUDzr1yxB"
subprocess.run(f'cd {R} && git add -A aplus/pro pipeline/pro && git commit -qm "EN A+: {" ".join(sys.argv[1:])}" -m "{m}" && git push -q && git log --oneline -1',shell=True)
