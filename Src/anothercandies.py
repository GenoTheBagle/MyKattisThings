t = int(input())
for _ in range(t):
    input() #blank
    child = int(input())
    candy = 0
    for _ in range(child):
        n = int(input())
        candy += n
    print("YES") if candy % child == 0 else print("NO")