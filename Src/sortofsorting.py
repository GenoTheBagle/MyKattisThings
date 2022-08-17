while True:
    n = int(input())
    if n == 0: break
    names = []
    for i in range(n):
        names.append(input())
    names.sort(key=lambda l: l[:2])
    print('\n'.join(names))