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

#union-find
from collections import defaultdict

#uf=DSU(n) nは要素数
class DSU():
    #コンストラクタ
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
        self.mycount=n

#要素の根を返す
    def leader(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.leader(self.parents[x])
            return self.parents[x]

#結合
    def merge(self, x, y):
        x = self.leader(x)
        y = self.leader(y)

        if x == y:
            return
        self.mycount-=1

        if self.parents[x] > self.parents[y]:
            x, y = y, x


        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.leader(x)]

    def same(self, x, y):
        return self.leader(x) == self.leader(y)

#全ての素集合を返す
    def groups(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.leader(member)].append(member)
        return group_members

#現在の集合の個数を返す
    def count(self):
        return self.mycount

def dfs(graph ,nv ,pv,seen,finish,e):
    global cycle
    seen[nv]=True
    cycle.append(nv+1)
    for ne in graph[nv]:

        #有向グラフの時は消す
        if ne==pv:
            continue
        if ne==e:
            cycle.append(ne+1)
            return cycle
        res=dfs(graph,ne,nv,seen,finish,e)
        if res is not False:
            return res
    
    finish[nv]=True
    cycle.pop()
    return False

t=ii()

for _ in  range(t):
    n,m=mi()
    uf=DSU(n)
    edge=[]
    graph=[[] for _ in range(n)]
    for _ in range(m):
        a,b=mmi()
        if uf.same(a,b):
            edge.append((a,b))
            continue
        uf.merge(a,b)
        graph[a].append(b)
        graph[b].append(a)
    bw=[-1]*n
    v=[0]
    bw[0]=0
    while v:
        now=v.pop()
        for ne in graph[now]:
            if bw[ne]==-1:
                bw[ne]=(bw[now]+1)%2
                v.append(ne)
    #debug(graph,edge)
    f=0
    for a,b in edge:
        if bw[a]==bw[b]:
            cycle=[]
            l=[-1]*n
            l2=[-1]*n
            ans=dfs(graph,a,-1,l,l2,b)
            #debug(len(ans))
            #debug(*ans)
            print(len(ans))
            print(*ans)
            f+=1
            break
    
    if f==0:
        print(-1)
        debug(-1)

