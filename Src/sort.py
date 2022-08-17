from collections import Counter
nc_og = input() #list(map(int, input().split())) # am I even going to use this
nc = input().split()
result = [item for items, c in Counter(nc).most_common() for item in [items] * c]
print(' '.join(result))