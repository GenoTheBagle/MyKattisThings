a, b = list(map(int, input().split()))
for _ in range(a):
    b -= int(input())
print("Jebb") if (b>=0) else print("Neibb")