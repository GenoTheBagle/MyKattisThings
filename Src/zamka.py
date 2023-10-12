L=int(input());D=int(input());X=int(input())
# min. L <= N <= D, sum of digits X
# max. L <= M <= D, sum of digits X
for i in range(L, D+1):
    # working upwards
    i_s = [int(d) for d in str(i)]
    if sum(i_s) == X:
        print(i)
        break

for i in reversed(range(L, D+1)):
    # working downwards
    i_s = [int(d) for d in str(i)]
    if sum(i_s) == X:
        print(i)
        break