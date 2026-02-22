import json
with open("base.txt",'r',encoding='utf-8') as f:
    lines = f.readlines()
content = []
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    if (s[6].find("1") != -1):
        x = True
    else:
        x = False
    t = {"altSpellings":[],"id":s[0],"isValid":"","joke":None if s[4] == "" else s[4],"prompt":s[2],"tags":s[5].split("|"),"title":"","x":x}
    content += [t]
w = open('DrawfulAnimatePrompt.jet','w',encoding='utf-8')
w.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
w.close()
w = open('DrawfulAnimatePromptTech.jet','w',encoding='utf-8')
w.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
w.close()
