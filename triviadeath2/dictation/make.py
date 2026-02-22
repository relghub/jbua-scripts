import json
from copy import deepcopy

first = True

textmode = False
catmode = False
setupmode = False
plmode = False

texts = []
event_str = "HOST/DictationVO/"
event_str_start = "HOST/ua/DictationVO/"

t_o = { # Шаблон завдання
   "eventName": str,
   "id": str,
   "text": [],
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
            t["id"] = s[0]#+"_uk-UA"
            t["eventName"] = event_str+s[0]
            texts.append(s[2])
            first = False
            textmode = True
        else:  # Для всіх інших завдань
            textmode = False
            t["text"] = texts
            content.append(t)
            t = deepcopy(t_o)
            t["id"] = s[0]#+"_uk-UA"
            t["eventName"] = event_str+s[0]
            texts = []
            texts.append(s[2])
            textmode = True
    elif textmode:
        texts.append(s[2])

t["text"] = texts
content += [t]
n = open("TDDictation.jet", "w", encoding="utf-8")
n.write(
    json.dumps({"content": content}, ensure_ascii=False, indent=4)
)
n.close()
