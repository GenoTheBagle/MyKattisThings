for _ in range(int(input())):
    k, n = list(map(int, input().split()))
    c = 0
    for i in range(n):
        c += (i+1)
        c += 1
    print(f"{k} {c}")