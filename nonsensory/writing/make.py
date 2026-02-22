import json
import os
answers = []
first = True
answermode = False
t_o = {
   "allowedAuthorRangeValues": "",
   "categoryId": "",
   "countrySpecific": False,
   "id": "",
   "isValid": "",
   "preferredMax": 0,
   "preferredMin": 0,
   "promptText": "",
   "questionText": "",
   "rangeMax": "",
   "rangeMin": "",
   "rangeType": "",
   "x": False
}
content = []
with open(os.path.dirname(__file__) + '\\base.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    if s[0] == 'id':
        if first:
            t = t_o.copy()
            t["id"] = s[1]+"_uk-UA"
            first = False
        else:
            content += [t]
            t = t_o.copy()
            t["id"] = s[1]+"_uk-UA"
        t["countrySpecific"] = bool(int(s[5]))
        t["x"] = bool(int(s[6]))
    elif s[0] == 'categoryId':
        t["categoryId"] = s[1]+"_uk-UA"
    elif s[0] == 'allowedAuthorRangeValues':
        t["allowedAuthorRangeValues"] = s[1]
    elif s[0] == 'rangeType':
        t["rangeType"] = s[1]
    elif s[0] == 'promptText':
        t["promptText"] = s[2]
    elif s[0] == 'questionText':
        t["questionText"] = s[2]
    elif s[0] == 'rangeMin':
        t["rangeMin"] = s[2]
    elif s[0] == 'rangeMax':
        t["rangeMax"] = s[2]
content += [t]
n = open('RangeGameWritingPrompt.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
n.close()
n = open('RangeGameWritingPromptTech.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
n.close()
