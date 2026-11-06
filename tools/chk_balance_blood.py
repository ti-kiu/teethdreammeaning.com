import re
for f in ("site/index.html","site/dream/gold/index.html","site/dream/dead-person-resurrected/index.html","site/dream/teeth-falling-out-with-blood/index.html","site/dream/blood/index.html"):
    p=open(f,encoding='utf-8').read()
    bad=[t for t in ("div","p","section","ul","li") if len(re.findall(rf'<{t}[ >]',p))!=p.count(f'</{t}>')]
    print(f, "BALANCED" if not bad else "BROKEN "+str(bad))
import subprocess
print(subprocess.run(["grep","-o","-i",".\\{50\\}[Vv]ein.\\{50\\}","site/dream/dead-person-resurrected/index.html"],capture_output=True,text=True).stdout)
