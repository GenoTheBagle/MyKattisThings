def split_add(num):
    num = sum([int(n) for n in list(str(num))])
    return num
    

while True:
    n = int(input())
    if n == 0: break
    val = 11
    num = split_add(n)
    while True:
        if split_add(val*n) == num:
            break
        val += 1
    print(val)