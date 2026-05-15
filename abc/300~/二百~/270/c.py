import sys
n,x,y=map(int,input().split())
tree=[[] for i in range(n+1)]
for i in range(n-1):
    u,v=map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)

visitable=[[x,-1]]
visit=set()
route=[-1]*(n+1)
while visitable:
    now=visitable.pop()
    visit.add(now[0])
    route[now[0]]=now[1]
    #print(now)
    #print(visitable)
    for i in range(len(tree[now[0]])):

        if now[1]!=tree[now[0]][i]:
            visitable.append([tree[now[0]][i],now[0]])

at=y
ans=[y]
#print(route)
while route[at]!=x:
    #print(route[at])
    ans.append(route[at])
    at=route[at]
ans.append(x)
ans.reverse()
print(*ans)