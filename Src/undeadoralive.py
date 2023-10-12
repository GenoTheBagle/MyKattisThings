s = input()
if ":)" in s and ":(" in s:
    print("double agent")
elif ":)" in s and not ":(" in s:
    print("alive")
elif not ":)" in s and ":(" in s:
    print("undead")
else:
    print("machine")