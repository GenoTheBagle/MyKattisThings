p, n = list(map(int, input().split()))
# number of parts, number of days
order = [] # order of parts replaced
og = [] # parts that have been replaced (no repeats)
for _ in range(n):
    w = input()
    order.append(w)
    if w not in og:
        og.append(w)
        
if len(og) != p:
    print("paradox avoided")
else:
    print(order.index(og[-1])+1)