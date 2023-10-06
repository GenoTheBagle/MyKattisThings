import math
n = int(input())
m = int(input())

if m%n == 0:
    mdivn = m//n
    for _ in range(n):
        print('*'*mdivn)
    exit()
    
mremn = m%n
mdivn = math.floor(m//n)
for _ in range(n):
    if mremn != 0:
        print('*'+'*'*mdivn)
        mremn -= 1
    else:
        print('*'*mdivn)