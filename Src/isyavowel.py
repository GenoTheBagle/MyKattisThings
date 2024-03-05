s = input()
c = len([char for char in s if char in "aieouAEIOU"])
cy = len([char for char in s if char in "aieouyAEIOUY"])
print(f"{c} {cy}")