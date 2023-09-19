import re
input() # ignoring this number
a = re.findall(r'\d+',input())
m = [int(i) for i in a]
print(max(m))