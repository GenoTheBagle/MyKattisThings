import math # we're going to use the area formula that uses pi B)

r, c = list(map(int, input().split()))

s_w = (r**2) * math.pi # pi r^2 -> area of pizza (circle) w/ crust
s_n = ((r-c)**2) * math.pi # same formula -> area of pizza w/o crust
per = (s_n / s_w) * 100 # then receive the percentage

print(per)