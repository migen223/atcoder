from collections import deque
n,m=map(int,input().split())

def toi(t):
    return t[0]+t[1]

graph={}
for i in range(n+1):
    for j in range(2**10):
        graph[(i,j)]=[]

for i in range(m):
    a,b,w=map(int,input().split())
    for j in range(2**10):
        graph[(a,j)].append((b,j^w))


vis=set()
v=[(1,0)]
vis.add((1,0))
while v:
    now=v.pop()
    #print(now,graph[now])
    for ne in graph[now]:
        if ne not in vis:
            vis.add(ne)
            v.append(ne)
    #print(v)
ans=10**32
for s in vis:
    if s[0]==n:
        ans=min(ans,s[1])
if ans==10**32:
    print(-1)
else:
    print(ans)

