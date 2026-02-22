import json
with open("base.txt",'r',encoding='utf-8') as f:
    lines = f.readlines()
content = []
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
##    if (s[3].find("1") != -1):
##        x = True
##    else:
##        x = False
    x = False
    t = {"id":s[0],"isValid":"","weapon":s[2],"x":x}
    content += [t]
w = open('MurderDetectivesWeapon.jet','w',encoding='utf-8')
w.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
w.close()
