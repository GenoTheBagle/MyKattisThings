from itertools import permutations

dwarves = []
for i in range(9):
    dwarves.append(int(input()))

total = sum(dwarves)
amt_to_remove = total - 100

to_remove = [p for p in permutations(dwarves, 2) if sum(p) == amt_to_remove]
dwarves.remove(to_remove[0][0]);dwarves.remove(to_remove[0][1])

for d in dwarves: print(d)