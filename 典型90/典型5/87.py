import sys
from collections import defaultdict
#edgeは(頂点,頂点、重さ)の形式の辺が格納されてるリスト、nodesは頂点数
#O(頂点数^3)
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

n,p,k=mi()

unknown=[]
e=[]
for i in range(n):
    a=li()
    for j in range(i+1,n): 
        aij=a[j]
        if aij==-1:
            unknown.append((i,j))

        else:
            e.append((i,j,aij))

if not unknown:
    edge=WF(e,n)
    res=0
    for i in range(n-1):
        for j in range(i+1,n):
            if edge[i][j]<=p:
                res+=1
    if res==k:
        print("Infinity")
    else:
        print(0)
    exit()

#debug(unknown,e)
def check(m,e,k):
    for i,j in unknown:
        e.append((i,j,m))
    edges=WF(e,n)
    res=0
    for i in range(n-1):
        for j in range(i+1,n):
            if edges[i][j]<=p:
                res+=1
    for _ in range(len(unknown)):
        e.pop()
    if res<=k:
        return True
    return False

l1=0
r1=10**9+1
while (r1-l1)>1:
    m=(l1+r1)//2
    if check(m,e,k):
        r1=m
    else:
        l1=m


l2=0
r2=10**9+1
while (r2-l2)>1:
    m=(l2+r2)//2
    if check(m,e,k-1):
        r2=m
    else:
        l2=m

#print(l1,r1)
#print(l2,r2)
if r1==10**9+1:
    print(0)
elif r2==10**9+1:
    print("Infinity")
else:
    print(r2-r1)