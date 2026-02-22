import json

content = []
choices = []
first = True
choicemode = False
empty = False
t_dot = [
    (
        "Fix",
        {
            "category": str,
            "choices": list,
            "correctAnswer": str,
            "id": str,
            "question": str,
        },
    ),
    (
        "GeoImages", 
        {
            "altTexts": list,
            "id": str,
            "name": str
        }
    ),
    (
        "GeoQuestions",
        {
            "category": "",
            "choices": list,
            "correctAnswer": str,
            "id": str,
            "imageId": str,
            "question": str,
        },
    ),
    (
        "Hop",
        {
            "category": str,
            "choices": list,
            "correctAnswer": str,
            "decade": str,
            "id": str,
            "question": str,
        },
    ),
    (
        "Impostor",
        {
            "category": str,
            "id": str,
            "impostor": str,
            "name": str,
            "real": str
        },
    ),
    (
        "ImpostorImages", 
        {
            "altText": str,
            "id": str,
            "name": str,
            "vamping": str
        }
    ),
    (
        "ImpostorStatements",
        {
            "category": str,
            "id": str,
            "imageId": str,
            "impostor": str,
            "real": str
        },
    ),
    (
        "Loop",
        {
            "category": str,
            "choices": list,
            "correctAnswer": str,
            "id": str,
            "question": str,
        },
    ),
    (
        "Year",
        {
            "category": str,
            "contextClue": "",
            "difficulty": str,
            "future": bool,
            "hint": [],
            "id": str,
            "question": str,
            "range": str,
            "tethering": bool,
            "year": int,
        },
    ),
]

def make_jet(file_i):
    t_rand = t_dot[file_i]
    t_o = t_rand[1]
    content = []
    choices = []
    line = ""
    s = ""
    first = True
    with open("../" + t_rand[0].lower() + "/base.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        line = line.replace("<отсутствует>", "")
        s = line.split(chr(9))
        if s[0] == "id":
            if first:
                choicemode = False
                t = t_o.copy()
                t["id"] = s[1]
                first = False
                if s[3] == ("1" or "2"):
                    empty = False
                    t = t_o.copy()
                    t["id"] = s[1]
                    i = 1
                else:
                    empty = True
            else:
                if not empty:
                    choicemode = False
                    if choices != []:
                        t["choices"] = choices
                    content += [t]
                    choices = []
                    i = 1
                if s[3] == ("1" or "2"):
                    empty = False
                    t = t_o.copy()
                    t["id"] = s[1]
                    i = 1
                else:
                    empty = True
        elif s[0] == "category" and not empty:
            t["category"] = s[1] if s[2] == "" else s[2]
        elif s[0] == "contextClue" and not empty:
            t["contextClue"] = s[1] if s[2] == "" else s[2]
        elif s[0] == "difficulty" and not empty:
            t["difficulty"] = s[1] if s[2] == "" else s[2]
        elif s[0] == "range" and not empty:
            t["range"] = s[1] if s[2] == "" else s[2]
        elif s[0] == "tethering" and not empty:
            t["tethering"] = bool(int(s[1] if s[2] == "" else s[2]))
        elif s[0] == "year" and not empty:
            t["year"] = int(s[1] if s[2] == "" else s[2])
        elif s[0] == "question" and not empty:
            t["question"] = s[2]
            choicemode = True
        elif (choicemode or s[0] == "choices") and not empty:
            if (s[0] == '' or s[0] == "v"):
                choicemode = True
                choices += [s[2]]
                if s[0] == "v":
                    t["correctAnswer"] = str(i)
                i += 1
            else: 
                choicemode = False
                continue
        elif s[0] in t_o and not empty:
            if t[s[0]] == bool:
                t[s[0]] = bool(int(s[1] if s[2] == "" else s[2]))
            elif t[s[0]] == int:
                t[s[0]] = int(s[1] if s[2] == "" else s[2])
            else:
                t[s[0]] = s[2] if s[2] != "" else s[1]
    t["choices"] = choices
    content += [t]
    n = open("../" + t_rand[0] + "/TimeTrivia" + t_rand[0] + ".jet", "w", encoding="utf-8")
    n.write(json.dumps({"content": content}, ensure_ascii=False, indent=1))
    n.close()
    n = open("../" + t_rand[0] + "/TimeTrivia" + t_rand[0] + "Tech.jet", "w", encoding="utf-8")
    n.write(json.dumps({"content": content}, ensure_ascii=False, indent=1))
    n.close()
    f.close()