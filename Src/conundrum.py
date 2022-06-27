s = list(input().lower())
per = ['p', 'e', 'r']
c = 0
d = 0
for l in s:
    if l != per[c]: d += 1
    if c == 2: c = 0
    else: c += 1
print(d)