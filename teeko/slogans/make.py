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
    t = {"suggestion":s[2],"id":int(s[0]),"type":"Canned Slogan"}
    content += [t]
w = open('AwShirtSlogans.jet','w',encoding='utf-8')
w.write(json.dumps({"episodeid":1265,"content":content},ensure_ascii=False,indent=2))
w.close()
