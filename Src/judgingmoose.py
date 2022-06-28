l, r = map(int, input().split())
if l == 0 and r == 0:
    print("Not a moose")
    quit()
if l == r:
    print(f"Even {l+r}")
elif l > r:
    print(f"Odd {l + l}")
elif r > l:
    print(f"Odd {r + r}")