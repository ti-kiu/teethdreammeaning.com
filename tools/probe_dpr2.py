import json
d=json.load(open('/root/.hermes/nabulsi_p2_120.json'))
for k in ['344','345']:
    v=d[k]['txt']
    # print tail of 344 and head-check of 345 around عاش / حي
    print('=== KEY',k,'pg',d[k]['pg'],'len',len(v))
    print(v)
    print()
