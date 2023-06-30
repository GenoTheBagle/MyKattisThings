input() # ignore
bats = list(map(int, input().split()))
new_bat = []
for item in bats:
    if item != -1:
        new_bat.append(item)
print((sum(new_bat)/ len(new_bat)))