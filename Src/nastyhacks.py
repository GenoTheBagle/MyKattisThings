for i in range(int(input())):
    r, e, c = list(map(int, input().split()))
    # r -> expected revenue without advertising
    # e -> expected revenue with advertising
    # c -> cost of advertising

    # deduct cost of advertising from revenue
    e_c = e - c
    if r > e_c: print("do not advertise")
    elif r < e_c: print("advertise")
    else: print("does not matter")