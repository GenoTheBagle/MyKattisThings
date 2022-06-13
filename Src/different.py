from sys import stdin

for line in stdin:
    a, b = list(map(int, line.split(' ')))
    if a > b:
        print(a-b)
    else:
        print(b-a)
