import json
import os
content = []
with open(os.path.dirname(__file__) + '\\cat.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    t = {"difficulty":s[3],"id":s[0]+"_uk-UA","isValid":"","text":s[2]}
    content += [t]
n = open('RangeGameFinalRoundDrawingCategory.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
n.close()
n = open('RangeGameFinalRoundDrawingCategoryTech.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=1))
n.close()
