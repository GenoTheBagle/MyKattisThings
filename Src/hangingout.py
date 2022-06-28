L, x = map(int, input().split())
# L -> limit
# x -> no. of events

inside = 0
not_allow = 0
for i in range(x):
    action, p = input().split()
    p = int(p)
    if action == 'enter':
        if (inside+p) <= L:
            inside += p
        else:
            not_allow += 1
            
    elif action == 'leave':
        inside -= p

print(not_allow)