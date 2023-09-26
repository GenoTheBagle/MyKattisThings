a, b = list(map(int, input().split()))

sum = 0
for _ in range(b):
    sum += int(input())
    
low = ((a-b)*(-3)+sum)/a
high = ((a-b)*(3)+sum)/a
print(low, high)