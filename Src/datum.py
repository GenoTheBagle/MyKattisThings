import datetime
date = input().split(' '); date.append("2009")
date = ' '.join(date)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", 
"Friday", "Saturday", "Sunday"]
print(days[datetime.datetime.strptime(date, '%d %m %Y').weekday()])