import json

first = True

choicemode = False
titlemode = True

choices = []

t_o = {"x": False, "id": "", "text": "", "choices": [], "us": False}  # Шаблон завдання
content = []
with open("basefinal.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
for line in lines:
    line = line.replace("\n", "")
    s = line.split(chr(9))
    if s[0].isdigit():  # Визначення рядка з номером завдання
        if first:  # Якщо перше завдання
            t = t_o.copy()
            t["id"] = s[0]
            if s[6] == "1":  # Перевірка завдання на локальне запитання
                t["us"] = True
            first = False
            titlemode = True
        else:  # Для всіх інших завдань
            choicemode = False
            t["choices"] = choices
            content += [t]
            t = t_o.copy()
            t["id"] = s[0]
            if s[6] == "1":  # Перевірка завдання на локальне запитання
                t["us"] = True
            choices = []
            titlemode = True
    elif titlemode:  # Якщо рядок містить запитання завдання
        t["text"] = s[6]
        titlemode = False
        choicemode = True
    elif choicemode:  # Обробка варіантів відповіді
        choices += [
            {
                "difficulty": int(s[4]),
                "correct": True if s[5] == "v" else False,
                "text": s[6],
            }
        ]
t["choices"] = choices
content += [t]
n = open("TDFinalRound.jet", "w", encoding="utf-8")
n.write(
    json.dumps({"content": content}, ensure_ascii=False, indent=2)
)
n.close()
n = open("TDFinalRoundTech.jet", "w", encoding="utf-8")
n.write(
    json.dumps({"content": content}, ensure_ascii=False, indent=2)
)
n.close()
