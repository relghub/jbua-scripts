import json
import os
answers = []
first = True
answermode = False

content = []
with open(os.path.dirname(__file__) + '\\base.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    t = {
   "allowedAuthorRangeValues": "ALL",
   "categoryId": "",
   "countrySpecific": bool(int(s[3])),
   "id": s[0]+"_uk-UA",
   "isValid": "",
   "preferredMax": 0,
   "preferredMin": 0,
   "promptText": s[2],
   "questionText": s[2],
   "rangeMax": "",
   "rangeMin": "",
   "rangeType": "DEFAULT",
   "x": bool(int(s[4]))
    }
    content += [t]
n = open('RangeGameAudienceSyncUpPrompt.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
n.close()
n = open('RangeGameAudienceSyncUpPromptTech.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
n.close()
