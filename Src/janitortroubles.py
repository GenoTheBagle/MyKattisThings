import math # for the sqrt()
s1, s2, s3, s4 = list(map(int, input().split()))

# following Bret's formula
sp = s1 + s2 + s3 + s4 # get perimeter
sp *= 0.5 # semiperimeter
k = (sp - s1) * (sp - s2) * (sp - s3) * (sp - s4)
k = math.sqrt(k)
print(k)