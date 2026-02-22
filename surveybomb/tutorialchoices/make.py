import json
choices = []
first = True
i = 0
taskmode = False
t_o = {"prompt":"","choices":[]}
content = []
with open('base.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    if s[0] == "choices":
        first = False
        taskmode = True
        choices += [s[2]]
    elif taskmode:
        choices += [s[2]]
    elif s[0] == "prompt":
        if first:
            t = t_o.copy()
            t["prompt"] = s[2]
        else:
            taskmode = False
            t["choices"] = choices
            content += [t]
            t = t_o.copy()
            tasks = []
            t["prompt"] = s[2]
            
t["choices"] = choices
content += [t]
n = open('SurveyBombTutorialChoices.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=2))
n.close()
