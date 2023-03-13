for _ in range(int(input())):
    a = list(input())
    b = list(input())
    ab = []
    
    for i in range(len(a)):
        if a[i] != b[i]:
            ab.append(i)
            
    s = list("."*len(a))
    for i in ab:
        s[i] = "*"
        
    print("".join(a))
    print("".join(b))
    print("".join(s))
    print("")
