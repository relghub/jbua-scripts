import json
content = []
with open('base.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    line = line.replace('\n','')
    s = line.split(chr(9))
    t = {"x":bool(int(s[4])),"h":bool(int(s[5])),"id":int(s[0]),"category":s[3],"type":s[1]}
    content += [t]
n = open('FakinItTasks.jet','w',encoding='utf-8')
n.write(json.dumps({"episodeid":1259,"content":content},ensure_ascii=False,indent=2))
n.close()
