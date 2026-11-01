import json
d=json.load(open('/root/.hermes/nabulsi_p2_120.json'))
print('keys present 340-350:', [k for k in range(340,351) if str(k) in d])
for k in ['345','346']:
    if str(k) in d:
        v=d[str(k)]['txt']
        i=v.find('عاش بعد موته')
        print('=== key',k,'pg',d[str(k)]['pg'],'len',len(v),'find عاش بعد موته at',i)
        if i>=0:
            print(v[max(0,i-400):i+1600])
        else:
            print('TAIL:', v[-1200:])
