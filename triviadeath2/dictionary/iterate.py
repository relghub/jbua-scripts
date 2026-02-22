with open('start.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
words = ''
word = ''
for line in lines:
    s = line.split(" ")
    if len(s[0]) == 4 and s[0][3] != '.':
        words += f"{s[0].lower()}\n"
n = open('fin.txt','w',encoding='utf-8')
n.write(words)
n.close()