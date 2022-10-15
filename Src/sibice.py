import math
n, w, h = list(map(int, input().split()))
wh = math.sqrt(w**2 + h**2)

for _ in range(n):
    a = int(input())
    print("DA") if a <= wh else print("NE")