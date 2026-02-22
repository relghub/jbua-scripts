import json
with open("base.txt",'r',encoding='utf-8') as f:
    lines = f.readlines()
content = []
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    if (s[3].find("1") != -1):
        c = True
    else:
        c = False
    if (s[4].find("1") != -1):
        x = True
    else:
        x = False
    t = {"countrySpecific":c,"id":s[0],"question":s[2],"x":x}
    content += [t]
w = open('UsThemQuestions.jet','w',encoding='utf-8')
w.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
w.close()
w = open('UsThemQuestionsTech.jet','w',encoding='utf-8')
w.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
w.close()
