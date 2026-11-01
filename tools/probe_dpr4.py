import json
d=json.load(open('/root/.hermes/nabulsi_p2_120.json'))
print('max key:', max(int(k) for k in d))
target='عاش بعد موته'
for k in sorted(d, key=int):
    v=d[k]['txt']
    if target in v:
        i=v.find(target)
        print('=== FOUND in shamela key',k,'pg',d[k]['pg'],'idx',i)
        print(v[max(0,i-800):i+2200])
        print()
