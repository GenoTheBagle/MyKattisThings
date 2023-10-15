limit = int(input())
for _ in range(int(input())):
    a, b = input().split()
    print(f'{a} {"lokud" if int(b) < limit else "opin"}')