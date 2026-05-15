
n=int(input())
town=[]
for _ in range(n):
    town.append([])
for _ in range(n-1):
    a,b=map(int,input().split())
    town[a-1].append(b-1)
    town[b-1].append(a-1)


def dfs(at,p,d,dist):
    dist[at]=d
    for to in town[at]:
        if to!=p:
            dfs(to,at,d+1,dist)

dist=[-1]*n
dfs(0,-1,0,dist)
far=dist.index(max(dist))

dist=[-1]*n
dfs(far,-1,0,dist)
print(max(dist)+1)