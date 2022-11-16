cur = 0
bal = 0
for _ in range(int(input())):
    # pos dep, neg with
    bal += int(input()) # += t
    cur = max(cur, -bal)
print(cur)
