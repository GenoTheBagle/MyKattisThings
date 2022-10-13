for _ in range(int(input())):
    a, b, c = list(map(int, input().split()))
    w = False

    if (a + b == c) or (a - b == c) or (b - a == c) or (a*b == c) or (a/b==c) or (b/a==c):
        w = True
    
    print('Possible') if w else print('Impossible')