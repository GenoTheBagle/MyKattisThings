f = []
for _ in range(10): f.append(int(input()))
print(len(set(a%42 for a in f)))