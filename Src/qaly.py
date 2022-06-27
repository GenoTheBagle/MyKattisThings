f = 0
for i in range(int(input())):
    q, y = list(map(float, input().split()))
    # quality, years
    f += (q * y)
print(f)