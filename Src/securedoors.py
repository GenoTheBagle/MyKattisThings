ents = set()
for n in range(int(input())):
    act, person = input().split()
    out = [person]
    
    if act == "entry":
        out.append("entered")
        if person in ents:
            out.append("(ANOMALY)")
        ents.add(person)
        
    elif act == "exit":
        out.append("exited")
        if person not in ents:
            out.append("(ANOMALY)")
        else:
            ents.remove(person)
        
    print(' '.join(out))