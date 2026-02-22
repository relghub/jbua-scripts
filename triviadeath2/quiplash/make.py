import json

with open("base.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
content = []
for line in lines:
    line = line.replace("\n", "")
    s = line.split(chr(9))
    t = {
        "id": s[0],
        "includesPlayerName": False,
        "keywords": [],
        "prompt": "[EventName=HOST/AltHost]" + s[2],
        "response": None,
        "safetyQuips": [],
        "us": False,
        "x": False,
    }
    content += [t]
w = open("QuiplashContent.jet", "w", encoding="utf-8")
w.write(json.dumps({"content": content}, ensure_ascii=False, indent=1))
w.close()
w = open("QuiplashContentTech.jet", "w", encoding="utf-8")
w.write(json.dumps({"content": content}, ensure_ascii=False, indent=1))
w.close()