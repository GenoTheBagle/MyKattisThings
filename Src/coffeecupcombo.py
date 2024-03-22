lectures = int(input())
halls = list(map(int, [*input()]))
awake = 0
cups = 0 # start value

for i in range(lectures):
    if halls[i] == 1:
        # reset cups
        cups = 2
        awake += 1
    else:
        # check cups
        if cups > 0:
            cups -= 1
            awake += 1
        
print(awake)