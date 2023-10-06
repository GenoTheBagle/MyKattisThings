vals = {}
for _ in range(int(input())):
    word = list(input())
    for i in range(len(word)):
        if not vals.get(i):
            vals[i] = []
        vals[i].append(word[i])

fin = ""
for i in vals.keys():
    added = 0
    for val in vals[i]:
        added += ord(val)
    fin += chr(added//len(vals[i]))

print(fin)