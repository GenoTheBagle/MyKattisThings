words = []
for i in range(int(input())):
    words.append(input())

for i in range(len(words)):
    if i % 2 == 0:
        print(words[i])
