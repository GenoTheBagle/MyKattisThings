def check_pos(num:int):
    if num > 0:
        return True
    else: return False

x_in = int(input())
y_in = int(input())

if check_pos(x_in) and check_pos(y_in):
    print(1)
elif not check_pos(x_in) and check_pos(y_in):
    print(2)
elif not check_pos(x_in) and not check_pos(y_in):
    print(3)
elif check_pos(x_in) and not check_pos(y_in):
    print(4)
