JJJ = {
    "CPU": 0,
    "MEM": 0,
    "HARD": 0
}
for _ in range(int(input())):
    c, m, h = input().split()
    if c == "J":
        JJJ["CPU"] += 1
    if m == "J":
        JJJ["MEM"] += 1
    if h == "J":
        JJJ["HARD"] += 1

print(JJJ[min(JJJ, key=JJJ.get)])