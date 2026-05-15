
n=int(input())
a=list(map(int,input().split()))
dic={}
for i in range(n):
    if a[i] not in dic:
        dic[a[i]]=[i]
    else:
        dic[a[i]].append(i)
gap=[]
for i in dic:
    orig=dic[i]
    if len(orig)>=2:
        l=[]
        for j in range(1,len(orig)):
            l.append(orig[j]-orig[j-1]-1)
        gap.append(l)

ans=0
for l in gap:
    now=l[0]
    ans+=now
    for j in range(1,len(l)):
        now+=l[j]*(j+1)
        ans+=now  
print(ans)
"""
dic={}
done=set()
for i in range(n):
    if a[i] not in dic:
        dic[a[i]]=[i]
    else:
        dic[a[i]].append(i)
if len(dic[a[0]])>=2:
    done.add(a[0])

ans=0
for i in range(1,n-1):
    for j in done:
        if a[i]!=j:
            l=dic[j]
            ind=bisect_left(l,i)
            ans+=ind*(len(l)-ind)
    if len(dic[a[i]])>=2:
        done.add(a[i])
print(ans)
"""