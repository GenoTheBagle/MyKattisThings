num = int(input())
temps = list(map(int, input().split(' ')))
total = 0
for temp in temps:
    if temp < 0:
        total += 1
print(total)