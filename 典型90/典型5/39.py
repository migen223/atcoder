import sys

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

n=ii()

origin=[[] for _ in range(n)]

r=[[] for _ in range(n)]
for _ in range(n-1):
    a,b=mmi()
    origin[a].append(b)
    origin[b].append(a)

graph=[[] for _ in range(n)]
rgraph=[[] for _ in range(n)]

v=[0]
vis=[False]*n
vis[0]=True
while v:
    now=v.pop()
    for ne in origin[now]:
        if not vis[ne]:
            vis[ne]=True
            v.append(ne)
            graph[now].append(ne)
            rgraph[ne].append(now)
leaf=[]
count=[1]*n
vis=[0]*n
for i in range(n):
    if len(graph[i])==0:
        leaf.append(i)
        vis[i]=1

#print(graph)

while leaf:
    now=leaf.pop()
    for ne in rgraph[now]:
        vis[ne]+=1
        count[ne]+=count[now]
        #debug(now,ne,count,vis,graph[now])
        if vis[ne]==len(graph[ne]):
            leaf.append(ne)
#print(count)
ans=0
for i in range(1,n):
    ans+=count[i]*(n-count[i])
print(ans)
