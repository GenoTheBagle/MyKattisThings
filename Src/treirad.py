n = int(input())
trips = 0

step = 1

while True:
    val =  step*(step+1)*(step+2)
    
    if val < n:
        trips += 1
    else:
        break
    
    step += 1
    
print(trips)