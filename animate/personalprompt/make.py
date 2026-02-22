import json
with open("base.txt",'r',encoding='utf-8') as f:
    lines = f.readlines()
content = []
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    if (s[8].find("1") != -1):
        x = True
    else:
        x = False
    t = {"altSpellings":[],"id":s[0],"isValid":"","joke":None if s[6] == '' else s[6],"prompt":s[2],"tags":s[7].split("|"),"title":s[4],"x":x}
    content += [t]
w = open('DrawfulAnimatePersonalPrompt.jet','w',encoding='utf-8')
w.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
w.close()
w = open('DrawfulAnimatePersonalPromptTech.jet','w',encoding='utf-8')
w.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
w.close()