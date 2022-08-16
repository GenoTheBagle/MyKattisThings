cups = list(input())
c_pos = [1, 0, 0]

def a_move(pos:list):
    pos[0], pos[1] = pos[1], pos[0]
    return pos

def b_move(pos:list):
    pos[1], pos[2] = pos[2], pos[1]
    return pos

def c_move(pos:list):
    pos[0], pos[2] = pos[2], pos[0]
    return pos

for move in cups:
    if move == "A":
        c_pos = a_move(c_pos)
    elif move == "B":
        c_pos = b_move(c_pos)
    elif move == "C":
        c_pos = c_move(c_pos)

print(c_pos.index(1)+1)