import math
h, v = list(map(int, input().split()))
print(int(math.ceil(h/math.cos(math.radians(90-v)))))