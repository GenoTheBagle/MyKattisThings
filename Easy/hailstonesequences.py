n = int(input())

all_nums = []
all_nums.append(n)
while True:
    if n == 1: break

    if (n%2==0): # even
        n = n // 2
        all_nums.append(n)
    else: # odd
        n = (n*3) + 1
        all_nums.append(n)
        
print(len(all_nums))
