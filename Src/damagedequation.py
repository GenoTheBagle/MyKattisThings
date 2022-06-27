a, b, c, d = list(input().split())
exps = ['*', '+', '-', '//']
got = False

for op_ab in exps:
    for op_cd in exps:
        if (int(b) == 0 or int(d) == 0) and (op_ab == "//" or op_cd == "//"): continue
        op_ab_ev = eval(f"{a}{op_ab}{b}")
        op_cd_ev = eval(f"{c}{op_cd}{d}")
        if op_ab_ev == op_cd_ev:
            print(f"{a} {op_ab} {b} = {c} {op_cd} {d}".replace('//', '/'))
            got = True

if not got: print("problems ahead") 