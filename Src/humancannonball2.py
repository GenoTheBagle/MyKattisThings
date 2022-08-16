import math
g = 9.81
for _ in range(int(input())):
    v, det, x, h1, h2 = [float(n) for n in input().split()]
    det = math.radians(det)
    t = x / (v*math.cos(det))
    y = (v*t*math.sin(det)) - (0.5 * g * (t**2))
    if y <= (h2-1) and y >= (h1+1):
        print("Safe")
    else:
        print("Not Safe")