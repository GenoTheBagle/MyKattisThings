total = 0
for i in range(int(input())):
    pr = input().lower()
    if 'pink' in pr or 'rose' in pr:
        total += 1

print(total) if total != 0 else print("I must watch Star Wars with my daughter")