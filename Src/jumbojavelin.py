ll = []
for i in range(int(input())):
    ll.append(int(input()))
fin = ll[0]
ll.pop(0)
for l in ll:
    fin += l
    fin -= 1
print(fin)