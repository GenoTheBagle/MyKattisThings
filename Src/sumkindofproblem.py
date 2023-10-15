for _ in range(int(input())):
    k, n = list(map(int, input().split()))
    print(k, sum(range(n+1)), sum(range(1, n*2+1, 2)), sum(range(2, n*2+1, 2)))