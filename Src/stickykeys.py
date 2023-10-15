s = list(input())
fin = ""
prev = ""
for i in s:
    if i != prev:
        fin += i
        prev = i
print(fin)