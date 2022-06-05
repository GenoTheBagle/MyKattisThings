x, y, z = list(map(int, input().split(' ')))

for i in range(z):
    i = i + 1
    if (i%x==0) and (i%y==0):
        print("FizzBuzz")
    elif (i%x==0) and not (i%y==0):
        print("Fizz")
    elif not (i%x==0) and (i%y==0):
        print("Buzz")
    else: print(i)
