final = int(input()) # get the number it ends with

mumblist = input().split()

last_number = 0
fishy = False
for bl in mumblist:
    if bl.isnumeric(): # is this a number?
        if int(bl) == (last_number + 1): # does it make sense?
            last_number += 1
        else:
            fishy = True # oh no, not the fish!
            break
    else:
        last_number += 1

print("something is fishy") if fishy else print("makes sense")