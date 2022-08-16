wb_list = []
for _ in range(int(input())):
    wb_list.append(input())

# check if same number of squares in row
for wb in wb_list:
    temp = list(wb)
    if temp.count('W') != temp.count('B'):
        print(0)
        quit()
    
    # check for consecutive same-colour squares
    for i in range((len(wb_list[0])-2)):
        if wb[i] == wb[i + 1] and wb[i + 1] == wb[i + 2]:
            print(0)
            quit()

# check if same number of squares in column
for n in range(len(wb_list)):
    temp = []
    for li in wb_list:
        temp.append(li[n])
    
    if temp.count('W') != temp.count('B'):
        print(0)
        quit()
    
    # check for consecutive same-colour squares
    for i in range((len(wb_list)-2)):
        if temp[i] == temp[i + 1] and temp[i + 1] == temp[i + 2]:
            print(0)
            quit()

print(1)