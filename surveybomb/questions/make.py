import json
choices = []
first = True
choicemode = False
empty = False
t_o = {"category":"","choices":[],"id":"","intro":None,"isValid":"","outro":None,"question":"","questionShort":"","round":"","us":False,"x":False}
content = []
with open('base.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    if s[0] == 'id':
        if first:
            t = t_o.copy()
            t["id"] = s[1]
            first = False
            if s[6] == '1':
                t["x"] = True
        else:
            if not empty:
                choicemode = False
                t["choices"] = choices
                content += [t]
                choices = []
            if s[3] == '2':
                empty = False
                t = t_o.copy()
                t["id"] = s[1]
                t["round"] = s[4]
                if s[6] == '1':
                    t["x"] = True
            else:
                empty = True
    elif s[0] == 'category' and not empty:
        t["category"] = s[1]
    elif s[0] == 'question' and not empty:
        t["question"] = s[2]
    elif s[0] == 'questionShort' and not empty:
        t["questionShort"] = s[2]
    elif (choicemode or s[0] == 'choices') and not empty:
        choicemode = True
        choices += [s[2]]
t["choices"] = choices
content += [t]
n = open('SurveyBombQuestions.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
n.close()
n = open('SurveyBombQuestionsTech.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
n.close()
