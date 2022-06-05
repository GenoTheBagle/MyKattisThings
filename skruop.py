w = 7
for i in range(int(input())):
    a = input()
    if 'op!' in a:
        if w != 10:
            w += 1
    elif 'ned!' in a:
        if w != 0:
            w -= 1
print(w)