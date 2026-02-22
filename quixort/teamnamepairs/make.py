import json
answers = []
decoys = []
first = True
answermode = False
t_o = {"answers":[],"decoys":[],"category":"","id":"","isValid":False,"prompt":"","us":False,"x":False,}
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
            if (s[7] == '1'):
                t["x"] = True
            first = False
        else:
            t["answers"] = answers
            t["decoys"] = decoys
            content += [t]
            t = t_o.copy()
            t["id"] = s[1]
            if (s[7] == '1'):
                t["x"] = True
            decoys = []
            answers = []
            answermode = False
    elif answermode or s[0] == 'answers':
        answermode = True
        if s[2] != '' and s[2] != '<отсутствует>':
            answers += [{"text":s[2]}]
        if s[4] != '' and s[4] != '<отсутствует>':
            decoys += [{"text":s[4]}]
    elif s[0] == 'category':
        t["category"] = s[2]
    elif s[0] == 'prompt':
        t["prompt"] = s[2]
t["answers"] = answers
t["decoys"] = decoys
content += [t]
n = open('TheWheelTappingList.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=2))
n.close()
