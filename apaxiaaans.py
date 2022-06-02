name = input()

l_last = ""
l_final = ""

for i in name.strip():
    if l_last != i:
        l_final += i

    l_last = i

print(l_final)