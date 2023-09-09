n = int(input())

r = bin(n)[-1:1:-1]
#r += len(str(n))*'0'
print(int(r,2))