days = {} # days[day][c] - (s, c)
for _ in range(int(input())):
    s, c, b = input().strip().split()
    c = int(c)
    if (b not in days) or (c > days[b][1]):
        days[b] = [s, c]
    
print(len(days))
for s, _ in sorted(days.values()):
    print(s)
        
