import math
x, y, z = int(input()), int(input()), int(input())
# x = large pizza diameter
# y = small pizza diameter
# z = num small pizza to replace num large pizza
big_piz = math.pi * (x/2)**2
smol_piz = (math.pi * (y/2)**2)*z
print("Neibb") if smol_piz < big_piz else print("Jebb")