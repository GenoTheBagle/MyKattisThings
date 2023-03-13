alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # do I even need to write it like this
s = input()
a, b = list(s[:len(s)//2]), list(s[len(s)//2:])

# first deal with a
a_l = 0
for l in a:
    a_l += alph.find(l)

a_new = []
for l in a:
    p = alph.find(l)
    p += a_l
    p %= len(alph)
    a_new.append(alph[p])
    
# now deal with b
b_l = 0
for l in b:
    b_l += alph.find(l)

b_new = []
for l in b:
    p = alph.find(l)
    p += b_l
    p %= len(alph)
    b_new.append(alph[p])
    
# rotation station situation
fin = []
for i in range(len(a_new)):
    ap = alph.find(a_new[i])
    bp = alph.find(b_new[i])
    ap += bp
    ap %= len(alph)
    fin.append(alph[ap])

print("".join(fin))