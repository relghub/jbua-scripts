import json
items = []
trash = []
first = True
itemmode = False
trashmode = False
t_o = {"categories":[],"countrySpecific":False,"difficulty":"","id":"","isValid":"","items":[],"leftLabel":"","prompt":"","rightLabel":"","trash":[],"x":False}
content = []
with open('base.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    if s[0] == 'id':
        if first:
            t = t_o.copy()
            t["id"] = s[1]+"_uk-UA"
            if (s[7] == '1'):
                t["countrySpecific"] = True
            if (s[8] == '1'):
                t["x"] = True
            first = False
        else:
            itemmode = False
            trashmode = False
            t["items"] = items
            t["trash"] = trash
            content += [t]
            t = t_o.copy()
            t["id"] = s[1]+"_uk-UA"
            if (s[7] == '1'):
                t["countrySpecific"] = True
            if (s[8] == '1'):
                t["x"] = True
            trash = []
            items = []
    elif s[0] == 'categories':
        t["categories"] = [s[2]]
    elif s[0] == 'difficulty':
        t["difficulty"] = s[2]
    elif s[0] == 'leftLabel':
        t["leftLabel"] = s[2]
    elif s[0] == 'prompt':
        t["prompt"] = s[2]
    elif s[0] == 'rightLabel':
        t["rightLabel"] = s[2]
    elif itemmode or s[0] == 'items':
        if s[0] == 'trash':
            itemmode = False
            trashmode = True
            if s[2] != '' and s[2] != '<отсутствует>':
                trashsingle = {"longText":s[2],"shortText":s[4]}
            trash += [trashsingle]
        else:
            itemmode = True
            if s[2] != '' and s[2] != '<отсутствует>':
                item = {"displayValue":s[6],"longText":s[2],"shortText":s[4]}
            items += [item]
    elif trashmode or s[0] == 'trash':
        itemmode = False
        trashmode = True
        if s[2] != '' and s[2] != '<отсутствует>':
            trashsingle = {"longText":s[2],"shortText":s[4]}
        trash += [trashsingle]
t["items"] = items
t["trash"] = trash
content += [t]
n = open('LineupLongSequence.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=2))
n.close()
n = open('LineupLongSequenceTech.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=2))
n.close()
