# so basically, given a table
# x 1 2 3
# 1 7 -1 -1
# 2 -1 -1 4
# outputs 1 1 7 and 2 3 4

r = int(input())
v = []
for i in range(r):
    c = list(map(int, input().split()))
    ii = 0
    for item in c:
        if item > 0:
            v.append(f"{i+1} {ii+1} {item}")
        ii += 1
        
print(len(v))
for item in v: print(item)