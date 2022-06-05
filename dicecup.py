n, m = list(map(int, input().split(' ')))

ln = [(i+1) for i in range(n)]
lm = [(i+1) for i in range(m)]
lall = []
 
def mf(stuff:list):
    dic = {}
    for item in stuff:
        if item not in dic.keys():
            dic[item] = 1
        else:
            dic[item] += 1
    return dic
    
for x in ln:
    for y in lm:
        lall.append(x+y)

dall = mf(lall)
high_v = 0
item_with_v = []
for item in dall.keys():
    if dall[item] > high_v:
        high_v = dall[item]
        item_with_v = [k for k,v in dall.items() if v == dall[item]]

for item in item_with_v: print(item)
