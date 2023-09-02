want = "welcome to code jam"
for i in range(int(input())):
    s = input()
    a = [[0]*(len(s)+1) for _ in range(len(want)+1)]
    for j in range(len(want) + 1):
        for k in range(len(s)+1):
            if j == 0:
                a[j][k] = 1
            elif k == 0:
                a[j][k] = 0
            elif s[k-1] == want[j-1]:
                a[j][k] = a[j-1][k-1] + a[j][k-1]
            else:
                a[j][k] = a[j][k-1]
    print(f"Case #{i+1}: {a[len(want)][len(s)]:04d}")