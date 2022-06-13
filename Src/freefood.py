amt_events = int(input())

days = set() # only one instance of 'thing' can be in a set :]

for i in range(amt_events):
    s, t = list(map(int, input().split(' ')))
    
    for day in range(s, (t+1)):
        days.add(day)
        
print(len(days))
