# this one used a lot of outside reference as I haven't really touched convex polygons
# so I'll write a comment on expected things in variables based on sample 1
def chunks(lst, n):
    # https://stackoverflow.com/a/65215647/14420546
    final = []
    for i in range(0, len(lst), n):
        final.append(lst[i:i + n]) # mainly got confused by syntax involving this line
    return final

for _ in range(int(input())):
    m_l = list(map(int, input().split()))
    # [3, 1, 1, 2, 1, 2, 2]
    n_p = m_l[0]
    # 3
    m_l.pop(0)
    # [1, 1, 2, 1, 2, 2]
    m_chunk = chunks(m_l, 2)
    # if this works, splits list into chunks
    # [[1,1], [2,1], [2,2]]
    total = 0
    step = 0
    for i in range(len(m_chunk)):
        # now formula application
        # taken from https://www.mathopenref.com/coordpolygonarea.html
        if step == (len(m_chunk)-1):
            total += ((m_chunk[0][1]*m_chunk[-1][0]) - (m_chunk[-1][-1]*m_chunk[0][0]))
        else:
            total += ((m_chunk[i][0]*m_chunk[i+1][1]) - (m_chunk[i+1][0]*m_chunk[i][1]))
        step += 1
    print(total/2)