import json
import os
fold = "FakinItInput"
promptmark = "TextTaskText"
categorymark = "TaskText"
i = 0
first = True
os.makedirs(fold, exist_ok=True)
with open(fold + 'Tech.jet','r',encoding='utf-8') as f:
    content = json.load(f)
content = list(sorted(content["content"], key=lambda f: f["id"]))
for item in content:
    os.makedirs(fold + "/" + item["id"],exist_ok=True)
    with open(fold + '/' + item["id"] + '/data.jet','r',encoding='utf-8') as f:
        data = json.load(f)
    itemtasks = len(item["tasks"])
    fields = data["fields"]
    if fields[5+itemtasks+1]["n"] == categorymark:
        fields[5+itemtasks+1]["v"] = item["category"]
    while i < (itemtasks):
        if first and fields[5+itemtasks+i]["n"] == promptmark+f"{i}":
            fields[5+itemtasks+i]["v"] = item["tasks"][i]["v"]
            first = False
        elif fields[5+itemtasks+1+i]["n"] == promptmark+f"{i}":
            fields[5+itemtasks+1+i]["v"] = item["tasks"][i]["v"]
        i += 1
    m = open(fold + "/" + item["id"] + "/data.jet","w",encoding="utf-8")
    m.write(json.dumps({"fields":fields},ensure_ascii=False,indent=1))
    m.close()
    first = True
    i = 0