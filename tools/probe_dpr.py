import json
d=json.load(open('/root/.hermes/nabulsi_p2_120.json'))
v=d['344']
print(type(v).__name__)
if isinstance(v,dict):
    for k2,v2 in v.items():
        s=v2 if isinstance(v2,str) else json.dumps(v2,ensure_ascii=False)
        print('FIELD:',k2,'len',len(s))
        print(s)
else:
    print(v)
