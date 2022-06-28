n = input() # not using this
print(-sum(filter(lambda x: x < 0, list(map(int, input().split())))))
# misread question, only wanted expenses, not incomes too