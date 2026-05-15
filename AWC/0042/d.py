from bisect import bisect_right
n,k=map(int,input().split())
a=list(map(int,input().split()))

sl=[0]
for i in  range(n):
    sl.append(sl[-1]+a[i])

modl={}
for i in range(1,n+1):
    p=sl[i]%k
    if p in modl:
        modl[p].append(i)
    else:
        modl[p]=[i]

#print(modl)
ans=0

for i in range(n):
    now=sl[i]%k
    if now not in modl:
        continue
    ans+=len(modl[now])-bisect_right(modl[now],i)
    #print(modl[now],"now",now,"i",i,len(modl[now])-bisect_right(modl[now],i))
print(ans)
