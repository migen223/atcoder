import sys
from collections import deque
def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
mmi= lambda: map(lambda x:int (x)-1, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]


n,m=mi()

graph=[[] for _ in range(n)]
for _ in range(m):
    u,v=mmi()
    graph[u].append(v)

ans=0
for i in range(n):
    v=deque([(i,0)])
    vis=set([i])
    while  v:
        now,d=v.popleft()
        if d>=2:
            ans+=1
        for ne in graph[now]:
            if ne not in vis:
                vis.add(ne)
                v.append((ne,d+1))

print(ans)
"""
graph=[[] for _ in range(n)]
start={i:[] for i in range(n)}
end={i:[] for i in range(n)}
vis=set([])
edge=[]
for i in range(m):
    u,v=mi()
    u-=1
    v-=1
    edge.append((u,v))
    graph[u].append(v)
    start[u].append(v)
    end[v].append(u)
    vis.add((u,v))

ans=0
v=[]
for i in range(m):
    for j in range(m):
        if i==j:
            continue
        if edge[i][1]==edge[j][0] and (edge[i][0],edge[j][1]) not in vis and edge[i][0]!=edge[j][1]:
            v.append((edge[i][0],edge[j][1]))
            start[edge[i][0]].append(edge[j][1])
            end[edge[j][1]].append(edge[i][0])
            vis.add((edge[i][0],edge[j][1]))
            ans+=1

while v:
    #print(ans,v)
    #print(start)
    #print(end)
    nedge=[]
    for es,ee in v:
        if start[ee]:
            for si in start[ee]:
                if (es,si) not in vis and es!=si:
                    ans+=1
                    nedge.append((es,si))
                    vis.add((es,si))
        if end[es]:
            for ei in end[es]:
                if (ei,ee) not in vis and ei!=ee:
                    ans+=1
                    nedge.append((ei,ee))
                    vis.add((ei,ee))
    v=[]
    
    for ed in nedge:
        v.append(ed)
        start[ed[0]].append(ed[1])
        end[ed[1]].append(ed[0])
    #debug(v)
#print(vis)
print(ans)
    """