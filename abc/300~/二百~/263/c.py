from itertools import combinations
n,m=map(int,input().split())
for c in combinations(range(1,m+1),n):
    print(*c)
