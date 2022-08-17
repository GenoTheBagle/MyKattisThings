s = input()
t = s.count("T")
c = s.count("C")
g = s.count("G")
sets = min(t,c,g)
print(t**2+c**2+g**2+sets*7)
# ** = ^