from collections import Counter
for i in range(int(input())):
    input()
    g = list(map(int, input().split()))
    c = Counter(g)
    odd = [k for k, v in c.items() if v == 1]
    print(f"Case #{i+1}: {odd[0]}")