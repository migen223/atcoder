from itertools import combinations
n,m=map(int,input().split())
popcorn=[]
for i in range(n):
    popcorn.append(list(input()))
kind=[0]*m
ans=n
ind=[i for i in range(n)]
for i in range(1,n+1):
    for c in combinations(ind,i):
        for store in list(c):
            for p in range(m):
                if popcorn[store][p]=="o":
                    kind[p]=1
        if 0 not in kind:
            ans=min(ans,i)
        kind=[0]*m

print(ans)
