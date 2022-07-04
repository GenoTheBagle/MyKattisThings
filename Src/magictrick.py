st = input().strip()
print(0 if len(st) != len(set(st)) else 1)