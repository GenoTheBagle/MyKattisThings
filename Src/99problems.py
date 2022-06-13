num = int(input())
final = 0
if num < 99:
    final = 99
else:
    num += 1.1
    temp = round(num/100)*100
    final = temp - 1
print(final)
