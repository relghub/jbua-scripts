import json
from copy import deepcopy

first = True

answermode = False
titlemode = True
altmode = False

answers = []

t_o = {  # Шаблон завдання
    "x": False,
    "answers": [],
    "id": int,
    "text": "",
    "us": False
}

a_o = {
    "answer": "",
    "alt": []
}

content = []
with open("base.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
for line in lines:
    line = line.replace("\n", "")
    s = line.split(chr(9))
    if s[0].isdigit():  # Визначення рядка з номером запитання
        if first:  # Якщо перше завдання
            t = deepcopy(t_o)
            t["id"] = s[0]
            if s[2] == "1":  # Перевірка завдання на локальне запитання
                t["us"] = True
            else:
                t["us"] = False
            first = False
            titlemode = True
        else:  # Для всіх інших завдань
            answermode = False
            t["answers"] = answers
            content.append(t)
            t = deepcopy(t_o)
            t["id"] = s[0]
            if s[2] == "1":  # Перевірка завдання на локальне запитання
                t["us"] = True
            else:
                t["us"] = False
            answers = []
            titlemode = True
    elif titlemode:  # Якщо рядок містить запитання завдання
        if s[0] == "Q" or "текст":
            t["text"] = s[2]
            titlemode = False
            answermode = True
    elif answermode:
        a = deepcopy(a_o)
        a["answer"] = "" if s[2] == "<отсутствует>" else s[2]
        answermode = False
        altmode = True
    elif altmode:
        altlist = s[2].split(" | ", -1)
        altlist = ["" if e == "<отсутствует>" else e for e in altlist]
        a["alt"].append((altlist))
        altmode = False
        answermode = True
        answers.append(a)

t["answers"] = answers
content += [t]
n = open("TDMindMeld.jet", "w", encoding="utf-8")
n.write(
    json.dumps({"content": content}, ensure_ascii=False, indent=2)
)
n.close()
