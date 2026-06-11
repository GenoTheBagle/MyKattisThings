import math
n = int(input())
base_scores = [100, 75, 60, 50, 45, 40, 36, 32, 29, 26, 24, 22, 20, 18, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
def rank_points(rank):
    if rank <= 30:
        return base_scores[rank-1]
    else:
        return 0

#def avg(vals: list):
    # for several contestants sharing the same placing
#    return (sum(vals)/len(vals))

contestants = []
for i in range(n):
    s, p, f, o = list(map(int, input().split()))
    # s = num of problems solved
    # p = time penalty
    # f = time submitted last accepted solution
    # o = extra points
    # +id for later tracking
    contestants.append({'id': i, 's': s, 'p': p, 'f': f, 'o': o})
contestants.sort(key=lambda x: (-x['s'], x['p'], x['f'])) # ACM rules
# 1. s (descending)
# 2. p (ascending)
# 3. f (ascending)

i = 0
while i < n:
    j = i
    # to find boundary of tied groups
    while j < n and (contestants[j]['s'] == contestants[i]['s'] and contestants[j]['p'] == contestants[i]['p'] and contestants[j]['f'] == contestants[i]['f']):
        j += 1
        
    size = j - i
    total_rank_points = 0
    
    for rank in range(i + 1, j + 1):
        total_rank_points += rank_points(rank)
        
    calculated_score = math.ceil(total_rank_points/size) # replace avg() function? import math maybe
    # need to assign scores + bonuses
    for k in range(i, j):
        contestants[k]['final_score'] = calculated_score + contestants[k]['o']
        
    i = j
contestants.sort(key=lambda x: x['id']) # restore
for c in contestants:
    print(c['final_score'])