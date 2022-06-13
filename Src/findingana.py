s = input()
s = [c for c in s]
r_amt = 0
for c in s:
    if c != "a":
        r_amt += 1
    else:
        break

for i in range(r_amt):
    s.pop(0)
print(''.join(s))
