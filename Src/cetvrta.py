coords = []
for i in range(3):
    coords.append(list(map(int, input().split(' '))))

fin = []

if coords[0][0] == coords[1][0]:
    fin.append(coords[2][0])
elif coords[0][0] == coords[2][0]:
    fin.append(coords[1][0])
else:
    fin.append(coords[0][0])
    
if coords[0][1] == coords[1][1]:
    fin.append(coords[2][1])
elif coords[0][1] == coords[2][1]:
    fin.append(coords[1][1])
else:
    fin.append(coords[0][1])
    
print(f"{fin[0]} {fin[1]}")
# untested code 2: electric boogaloo