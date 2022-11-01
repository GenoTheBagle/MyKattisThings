m_t = 210 # 3 min 30 sec
t_t = 0 # total time
k = int(input())
ind = k - 1

for _ in range(int(input())): # n
    t, z = input().split()
    t = int(t)
    t_t += t
    if t_t >= m_t: break
    if z == "T": 
        ind = ((ind+1)%8)

print(ind+1)
