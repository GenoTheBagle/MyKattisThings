is_he_blimp = []
for i in range(5):
    if "FBI" in input():
        is_he_blimp.append(str(i+1))

if len(is_he_blimp) == 0:
    print("HE GOT AWAY!")
else:
    print(' '.join(is_he_blimp))