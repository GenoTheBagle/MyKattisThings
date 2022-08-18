all_stuff = {}
for _ in range(int(input())):
    s = input().split()
    if s[1].isnumeric():
        s = [int(s[1]), s[0]]
    else:
        s = [int(s[0])//2, s[1]]
    all_stuff[s[1]] = s[0]
    
all_stuff = dict(sorted(all_stuff.items(), key=lambda item: item[1]))
for item in all_stuff: print(item)