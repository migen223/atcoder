from bisect import bisect_left
n,k=map(int,input().split())
a=list(map(int,input().split()))
r=[0]
for i in range(n):
    r.append(r[-1]+a[i])

dic={}
for i in range(n+1):
    if r[i] in dic:
        dic[r[i]].append(i)
    else:
        dic[r[i]]=[i]

ans=0
for i in range(1,n+1):
    sl=r[i]-k
    if sl in dic:
        ans+=bisect_left(dic[sl],i)
print(ans)