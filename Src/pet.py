cons = []
for i in range(5):
    cons.append(list(map(int, input().split())))
high_con = [0, 0]
i = 1
for con in cons:
    if high_con[1] < sum(con):
        high_con = [i, sum(con)]
    i += 1
print(high_con[0], high_con[1])