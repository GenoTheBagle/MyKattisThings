c = float(input())
v = 0
for _ in range(int(input())):
    w, l = [float(a) for a in input().split()]
    v += (w*l*c)
print(v)