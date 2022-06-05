values = input().split(" ")
order = input()
# bah! the input wasn't "A B C", it was "ABC"!

order = [c for c in order]
values = sorted([int(value) for value in values])

gen_order = {
"A":values[0],
"B":values[1],
"C":values[2]
}

final = []

for alph in order:
    temp = str(gen_order[alph])
    final.append(temp)

print(" ".join(final))
