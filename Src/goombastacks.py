total = 0
for _ in range(int(input())):
    g, b = list(map(int, input().split()))
    total += g
    if total >= b:
        continue
    else:
        print("impossible")
        exit()
print("possible")