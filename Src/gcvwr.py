G, T, N = list(map(int, input().split()))
w = list(map(int, input().split()))
print(int(((G-T)*(0.9))-sum(w)))