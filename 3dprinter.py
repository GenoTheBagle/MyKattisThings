needed = int(input())

printers = 1
statues = 0
days = 0

while statues < needed: # != causes program to freeze for some reason..?
    if (needed - statues) > printers:
        printers = printers * 2
    else: statues += printers
    days += 1

print(days)