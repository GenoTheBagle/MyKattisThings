from itertools import product
input(); p = list(map(int, input().split()))
cs = list(product(range(1,7,1), range(1,7,1)))
print(sum(sum(d) in p for d in cs) / len(cs))