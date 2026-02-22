import json
safety_answers = []
sign_posts = []
first = True
spmode = False
safetymode = False
titlemode = False
t_o = {"id":str,"safetyAnswers":[],"signposts":[],"title":str,"x":bool}
content = []
with open('base.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    if s[0].isdigit(): # Визначення рядка з номером запитання
        if first: # Якщо перше завдання
            t = t_o.copy()
            t["id"] = s[0]
            if (s[2] == '1'):
                t["x"] = True
            first = False
            titlemode = True
        else: # Для всіх інших завдань
            spmode = False
            safetymode = False
            t["safetyAnswers"] = safety_answers
            t["signposts"] = sign_posts
            content += [t]
            t = t_o.copy()
            t["id"] = s[0]
            if (s[2] == '1'): # Перевірка запитання на сімейний 
                t["x"] = True if s[2] == '1' else False
            safety_answers = []
            sign_posts = []
            titlemode = True
    elif titlemode: # Якщо рядок містить запитання завдання
        t["title"] = s[2]
        titlemode = False
    elif s[0] == 'middle' or s[0] == 'end':
        safetymode = False
        spmode = True
        sign_posts += [{"position":s[0],"signpost":s[2]}]
    elif s[0] == 'SafeAns.': # Визначення рятівничок (запасних варіантів)
        safetymode = True
        safety_answers += [s[2]]
    elif safetymode:
        safety_answers += [s[2]]
    elif spmode:
        sign_posts += [{"position":"","signpost":""}]
t["safetyAnswers"] = safety_answers
t["signposts"] = sign_posts
content += [t]
n = open('JackboxTalksTitle.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=2))
n.close()
