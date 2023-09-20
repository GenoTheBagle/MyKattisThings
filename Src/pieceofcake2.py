n, h, v = list(map(int, input().split()))
print(max(n-h,h) * max(n-v,v) * 4)