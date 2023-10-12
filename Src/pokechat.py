import re
s = list(input())
pid = list(map(int, re.findall('...',input())))

fin = ""
for id in pid:
    fin += s[id-1]
    
print(fin)