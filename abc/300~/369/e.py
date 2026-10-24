import sys
from itertools import permutations
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
def WF(edge,nodes):
    res=[[10**32]*nodes for i in range(nodes)]
    for i in range(nodes):
        res[i][i]=0
    for u,v,w in edge:
        res[u][v]=min(res[u][v],w)
        res[v][u]=min(res[v][u],w)
    for k in range(nodes):#経由する頂点
        for i in range(nodes):#始点
            for j in range(nodes):#終点
                res[i][j]=min(res[i][j],res[i][k]+res[k][j])
    
    return res

n,m=mi()

edge=[]
dic={}
for i in range(m):
    u,v,t=mi()
    edge.append((u-1,v-1,t))
    dic[i+1]=(u-1,v-1,t)
dist=WF(edge,n)

#(i>>j)&1 →j bit目がたっているかどうか
#i|(1<<j) →iのjbit目を立たせる
q=ii()
for _ in range(q):
    k=ii()
    b=li()
    ans=inf
    for i in range(2**k):
        for p in permutations(b):
            route=[0]
            res=0
            now=0
            for j in range(k):
                u,v,t=dic[p[j]]
                if (i>>j)&1:
                    res+=dist[now][u]+t
                    now=v
                else:
                    res+=dist[now][v]+t
                    now=u
            res+=dist[now][n-1]
            ans=min(ans,res)
    print(ans)