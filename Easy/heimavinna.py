qs = input().split(";")
ps = 0
for value in qs:
    if "-" in value:
        a, b = value.split("-")
        c = int(b) - int(a)
        c += 1
        ps += c
    else:
        ps += 1
print(ps)
