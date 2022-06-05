dic_chess = {
"king": 1,
"queen": 1,
"rook": 2,
"bishop": 2,
"knight": 2,
"pawn": 8
}
lis_chess = [piece for piece in dic_chess]
user_in = input().split(" ")
# king, queen, rook, bishop, knight, pawn
final_output = ""
i = 0
for piece in user_in:
    ind = lis_chess[i]
    dif = dic_chess[ind] - int(piece)
    i += 1
    final_output += f"{dif} "
print(final_output)
