import json
first = True
logmode = False
t_o = {"doodle":str,"id":int,"log":str,"x":bool}
content = []
with open('base.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    if s[0].isdigit(): # Визначення рядка з номером запитання
        if first: # Якщо перше завдання
            t = t_o.copy()
            t["id"] = int(s[0])
            t["doodle"] = "Log"+s[0]
            t["x"] = True if s[2] == '1' else False # Перевірка запитання на сімейний фільтр
            first = False
            logmode = True
        else: # Для всіх інших завдань
            content += [t]
            t = t_o.copy()
            t["id"] = int(s[0])
            t["doodle"] = "Log"+s[0]
            t["x"] = True if s[2] == '1' else False # Перевірка запитання на сімейний фільтр
            logmode = True
    elif logmode: # Якщо рядок містить запитання завдання
        t["log"] = s[2]
        logmode = False
content += [t]
n = open('JokeboatCaptainLog.jet','w',encoding='utf-8')
n.write(json.dumps({"content":content},ensure_ascii=False,indent=4))
n.close()
