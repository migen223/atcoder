from bisect import bisect_left
n=int(input())
inf=float('inf')

kite=[]
for _ in range(n):
    a,b=map(int,input().split())
    kite.append((a,-b))
kite.sort()

lis=[inf]*(n+1)
for i in range(n):
    a,b=kite[i][0],-kite[i][1]
    ind=bisect_left(lis,b)
    lis[ind]=min(lis[ind],b)

ans=0
for i in range(n):
    if lis[i]==inf:
        break
    ans=i+1
print(ans)