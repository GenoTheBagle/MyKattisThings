s = input().split('-')
fin = ""
for n in s:
    fin += [s[0] for s in n.split()][0]
print(fin)
