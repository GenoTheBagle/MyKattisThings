n = int(input())
c_l = list(map(int, input().split()))
c_l.sort()
b_l = list(range(1, n+1))
f = 1 # minimum starting cap

for b, c in zip(b_l, c_l):
    if b < c: 
        print("impossible")
        break
    
    f = min(f, c/b) # returns lowest number
    
else:
    print(f)