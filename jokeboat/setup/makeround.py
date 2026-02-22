import json
from copy import deepcopy

first = True

decoymode = False
catmode = False
setupmode = False
plmode = False

decoys = []

t_o = { # Шаблон завдання
    "punchline": str,
    "decoys": [],
    "timing": str,
    "x": bool,
    "setup": str,
    "id": int,
    "categories": str,
    "type": str
}

content = []
with open("base.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
for line in lines:
    line = line.replace("\n", "")
    s = line.split(chr(9))
    print(s)
    if s[0].isdigit():  # Визначення рядка з номером запитання
        if first:  # Якщо перше завдання
            t = deepcopy(t_o)
            t["id"] = int(s[0])
            if s[2] == "1":  # Перевірка завдання на локальне запитання
                t["x"] = True
            else:
                t["x"] = False
            t["timing"] = s[3]
            t["type"] = s[4]
            first = False
            catmode = True
        else:  # Для всіх інших завдань
            decoymode = False
            t["decoys"] = decoys
            content.append(t)
            t = deepcopy(t_o)
            t["id"] = int(s[0])
            if s[2] == "1":  # Перевірка завдання на локальне запитання
                t["x"] = True
            else:
                t["x"] = False
            t["timing"] = s[3]
            t["type"] = s[4]
            decoys = []
            catmode = True
    elif catmode:  # Якщо рядок містить запитання завдання
        t["categories"] = s[2]
        catmode = False
        setupmode = True
    elif setupmode:
        t["setup"] = s[2]
        setupmode = False
        plmode = True
    elif plmode:
        t["punchline"] = s[2]
        plmode = False
        decoymode = True
    elif decoymode:
        decoys.append(s[2])

t["decoys"] = decoys
content += [t]
n = open("JokeboatSetup.jet", "w", encoding="utf-8")
n.write(
    json.dumps({"episodeid": 1397, "content": content}, ensure_ascii=False, indent=4)
)
n.close()
