import json
import os

fold = "TDQuestion"
os.makedirs(fold, exist_ok=True)
with open(fold + '.jet','r',encoding='utf-8') as f:
    content = json.load(f)
content = content["content"]
for item in content:
    os.makedirs(fold + "/" + str(item["id"]),exist_ok=True)
    try:
        open(fold + '/' + str(item["id"]) + '/data.jet','r',encoding='utf-8')
    except FileNotFoundError:
        continue
    with open(fold + '/' + str(item["id"]) + '/data.jet','r',encoding='utf-8') as f:
        data = json.load(f)
    fields = data["fields"]
    if item["introAudio"] is not None:
        fields[1]["s"] = item["introAudio"]
    fields[3]["s"] = item["questionAudio"]
    m = open(fold + "/" + str(item["id"]) + "/data.jet","w",encoding="utf-8")
    m.write(json.dumps({"fields":fields},ensure_ascii=False,indent=1))
    m.close()
