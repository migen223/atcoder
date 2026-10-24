import sys

def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
mmi= lambda: map(lambda x:int (x)-1, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
#mod = 998244353
mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]

n=ii()
c=input().split()

origin=[[] for _ in range(n)]

for _ in range(n-1):
    a,b=mmi()
    origin[a].append(b)
    origin[b].append(a)

vis=[0]*n
vis[0]=1
v=[0]
graph=[[] for _ in range(n)]
rgraph=[[] for _ in range(n)]
while v:
    now=v.pop()
    for ne in origin[now]:
        if  not vis[ne]:
            graph[now].append(ne)
            rgraph[ne].append(now)
            vis[ne]=1
            v.append(ne)


leaf=[]
count=[0]*n
ans=[[0,0,0] for _ in range(n)]
for i in range(n):
    if len(graph[i])==0:
        leaf.append(i)
    if c[i]=="a":
        ans[i][0]=1
    else:
        ans[i][1]=1


while leaf:
    now=leaf.pop()
    for ne in rgraph[now]:
        tmp=[0,0,0]
        tmp[0]+=ans[ne][0]*ans[now][2]+ans[now][0]*ans[ne][0]
        tmp[1]+=ans[ne][1]*ans[now][2]+ans[now][1]*ans[ne][1]
        tmp[2]+=ans[ne][0]*ans[now][1]+ans[ne][1]*ans[now][0]
        for i in range(3):
            tmp[2]+=ans[ne][i]*ans[now][2]
            tmp[2]+=ans[now][i]*ans[ne][2]
        for  i in range(3):
            tmp[i]%=mod
        #debug(tmp,now,ne,count)
        ans[ne]=tmp[::]
        count[ne]+=1
        if len(graph[ne])==count[ne]:
            leaf.append(ne)

#print(ans)
print(ans[0][2]%mod)
        