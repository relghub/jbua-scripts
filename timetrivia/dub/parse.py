n = open('start.txt','r',encoding='utf-8')
text = n.read()
with open('base.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    s = line.split(chr(9))
    s[2] = s[2].replace("\n","",1)
    s[1] = s[1].replace('\\"','"')
    s[1] = s[1].replace('"','\\"')
    s[1] = s[1].replace("'","\\'")
    s[2] = s[2].replace('"','\\"')
    if text.find(s[1]) == -1:
        print(s[1] + " was not found")
    text = text.replace(s[1],s[2],1)
n = open('fin.txt','w',encoding='utf-8')
n.write(text)
n.close()
