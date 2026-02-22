import json

tasks = []
first = True
i = 0
taskmode = False
t_o = {"x": False, "h": False, "id": "", "category": "", "type": "", "tasks": []}
content = []
with open("base.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
for line in lines:
    line = line.replace("\n", "")
    s = line.split(chr(9))
    if s[0] == "":
        first = False
        taskmode = True
        q = {"v": s[2], "x": bool(int(s[3])), "h": bool(int(s[4])), "id": i}
        tasks += [q]
        i += 1
    else:
        if first:
            t = t_o.copy()
            t["id"] = s[0]
            t["type"] = "Input"
            t["category"] = s[2]
            t["x"] = bool(int(s[3]))
            t["h"] = bool(int(s[4]))
        else:
            taskmode = False
            t["tasks"] = tasks
            i = 0
            content += [t]
            t = t_o.copy()
            t["id"] = s[0]
            t["type"] = "Input"
            t["category"] = s[2]
            t["x"] = bool(int(s[3]))
            t["h"] = bool(int(s[4]))
            tasks = []

t["tasks"] = tasks
content += [t]
n = open("FakinItInput.jet", "w", encoding="utf-8")
n.write(
    json.dumps({"episodeid": 1261, "content": content}, ensure_ascii=False, indent=2)
)
n.close()
