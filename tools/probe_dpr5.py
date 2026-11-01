import json
d=json.load(open('/root/.hermes/nabulsi_p2_120.json'))
out=[]
for k in ['344','345']:
    v=d[k]['txt']
    out.append('===SHAMELA_KEY %s (printed p.%d)===' % (k, d[k]['pg']))
    out.append(v)
open('/root/dream_research/nabulsi_p347_349.txt','w').write('\n'.join(out))
# print the tail of 345 with the resurrection-of-matters passage
v=d['345']['txt']
i=v.find('ميتاً أنه حي')
print('idx',i)
print(v[max(0,i-200):i+1000])
