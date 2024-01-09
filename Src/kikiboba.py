a=input()

if a.count("b") == 0 and a.count("k") == 0:
    print("none")
elif a.count("b") > a.count("k"):
    print("boba")
elif a.count("b") < a.count('k'):
    print("kiki")
else:
    print("boki")