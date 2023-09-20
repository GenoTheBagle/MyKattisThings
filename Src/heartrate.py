for _ in range(int(input())):
    b, p = list(map(float, input().split()))
    print((60/(p/(b-1))), (60*b/p), (60/(p/(b+1))))