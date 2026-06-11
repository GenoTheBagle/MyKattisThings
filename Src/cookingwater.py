a, b = [], []
# 0 <= a <= b <= 1000
# edward looks away during seconds [a,b]
for _ in range(int(input())):
    aa, bb = list(map(int, input().split()))
    a.append(aa); b.append(bb)
print("edward is right") if (max(a) > min(b)) else print("gunilla has a point")
