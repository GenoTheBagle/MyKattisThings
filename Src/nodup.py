a = input()
a_l = a.split()
a_s = set(a_l)

print('yes') if (len(a_l) == len(a_s)) else print('no')