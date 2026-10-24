from collections import deque
import sys
n=int(input())
p=list(map(lambda x:int(x)-1,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
mod= 998244353

graph=[[] for _ in range(n)] #葉->根
rgraph=[[] for _ in range(n)] #根->葉
for i in range(n-1):
    graph[i+1].append(p[i])
    rgraph[p[i]].append(i+1)
#print(graph)
#print(rgraph)
leaf=deque([])
for i in range(1,n):
    if len(rgraph[i])==0:
        leaf.append(i)

def C(n,k):
    deno=1
    nume=1
    for i in range(k):
        deno*=(i+1)
        nume*=(n-i)
        deno%=mod
        nume%=mod
    return nume*pow(deno,-1,mod)

#print(leaf
v=[0]*n
ans=1
while leaf:
    now=leaf.popleft()
    if c[now]>=d[now]:
        ans*=C(c[now],d[now])
        ans%=mod
    else:
        print(0)
        sys.exit()
    c[now]-=d[now]
    for ne in graph[now]:
        v[ne]+=1
        c[ne]+=c[now]
        if v[ne]==len(rgraph[ne]):
            leaf.append(ne)
    #print(now,c,v)
print(ans)


