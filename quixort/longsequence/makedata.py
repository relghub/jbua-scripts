import json
import os
fold = "LineupLongSequence"
audfold = "LongAudio"
os.makedirs(fold, exist_ok=True)
with open(fold + 'Tech.jet','r',encoding='utf-8') as f:
    content = json.load(f)
content = content["content"]
for item in content:
    os.makedirs(fold + "/" + item["id"],exist_ok=True)
    with open(fold + '/' + item["id"] + '/data.jet','r',encoding='utf-8') as f:
        data = json.load(f)
    fields = data["fields"]
    fields[1]["s"] = item["prompt"] + ": ліворуч - \"" + item["leftLabel"] + "\", праворуч - \"" + item["rightLabel"] + "\""
    m = open(fold + "/" + item["id"] + "/data.jet","w",encoding="utf-8")
    m.write(json.dumps({"fields":fields},ensure_ascii=False,indent=1))
    m.close()
    with open(audfold + "/" + str(item["id"]).split("_")[0] + "_Process.ogg", 'rb') as src, open(fold + "/" + item["id"] + "/prompt.ogg", 'wb') as dst: dst.write(src.read())
