for i in range(int(input())):
    k = input()
    if "P=NP" in k:
        print('skipped')
        continue
    a, b = list(map(int, k.split('+')))
    print(a+b)
