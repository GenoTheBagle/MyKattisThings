x = int(input())
ps = []
for i in range(int(input())):
    ps.append(int(input()))
t = 0
for p in ps:
    temp = x - p
    t += temp
t += x
print(t)