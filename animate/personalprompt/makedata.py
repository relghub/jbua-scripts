import json
import os
fold = "DrawfulAnimatePersonalPrompt"
os.makedirs(fold, exist_ok=True)
with open(fold + 'Tech.jet','r',encoding='utf-8') as f:
    content = json.load(f)
content = content["content"]
for item in content:
    os.makedirs(fold + "/" + str(item["id"]),exist_ok=True)
    with open(fold + '/' + str(item["id"]) + '/data.jet','r',encoding='utf-8') as f:
        data = json.load(f)
    fields = data["fields"]
    fields[1]["v"] = item["prompt"]
    m = open(fold + "/" + str(item["id"]) + "/data.jet","w",encoding="utf-8")
    m.write(json.dumps({"fields":fields},ensure_ascii=False,indent=1))
    m.close()
