import json
from copy import deepcopy

first = True

choicemode = False
titlemode = True
rejectmode = False

choices = []

t_o = {  # Шаблон завдання
    "choices": [],
    "id": "00000",
    "introAudio": "",
    "outro": None,
    "questionAudio": "",
    "text": "",
    "us": False,
    "x": False
}

content = []
with open("basequestion.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
for line in lines:
    line = line.replace("\n", "")
    s = line.split(chr(9))
    print(s)
    if s[0].isdigit():  # Визначення рядка з номером запитання
        if first:  # Якщо перше завдання
            t = deepcopy(t_o)
            t["id"] = s[0]
            # if s[2] == "1":  # Перевірка завдання на локальне запитання
            #    t["us"] = True
            #else:
            #    t["us"] = False
            first = False
            titlemode = True
        else:  # Для всіх інших завдань
            choicemode = False
            if not rejectmode:
                t["choices"] = choices
                content.append(t)
            t = deepcopy(t_o)
            t["id"] = s[0]
            #if s[2] == "1":  # Перевірка завдання на локальне запитання
            #    t["us"] = True
            #else:
            #    t["us"] = False
            choices = []
            rejectmode = False
            titlemode = True
    elif titlemode:  # Якщо рядок містить запитання завдання
        if rejectmode:
            continue
        elif not rejectmode:
            #if int(s[3]) < 2:
                #rejectmode = True
            #elif s[0] == "Intro":
            if s[0] == "Intro":
                t["introAudio"] = s[2]
            elif s[0] == "озвучка":
                t["questionAudio"] = s[2]
            elif s[0] == "Q" or "текст":
                t["text"] = s[2]
                print(s[2])
                t["introAudio"] = None if t["introAudio"] == "" else t["introAudio"]
                t["questionAudio"] = t["text"] if t["questionAudio"] == "" else t["questionAudio"]
                titlemode = False
                choicemode = True
    elif choicemode:
        choices.append(
            {
                "correct": True if s[0] == "v" else False,
                "text": s[2],
            }
        )

t["choices"] = choices
content += [t]
n = open("TDQuestion.jet", "w", encoding="utf-8")
n.write(
    json.dumps({"content": content}, ensure_ascii=False, indent=2)
)
n.close()
