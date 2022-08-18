import math
l, r = list(map(int, input().split()))
print("fits") if math.sqrt(2)*r > l else print("nope")