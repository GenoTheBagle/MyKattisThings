stop = list(input())
memo = input().split(' ')

for letter in stop:
    memo_new = []
    for word in memo:
        if letter in word:
            word = '*'*len(word)
        memo_new.append(word)
    memo = memo_new
    
print(' '.join(memo))