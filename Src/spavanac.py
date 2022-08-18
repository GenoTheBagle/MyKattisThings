h, m = list(map(int, input().split()))

m -= 45
if m < 0:
    h -= 1
    if h < 0:
        h = 23
    m += 60

print(f"{h} {m}")