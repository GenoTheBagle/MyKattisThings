# in short, odd squares
n = int(input())
s = 0
a = 0
num = 1
while True:
    if (s+num**2) > n:
        break
    s += num**2
    num += 2 # every odd
    a += 1 # add to total height
    
print(a)