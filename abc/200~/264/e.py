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

n,m,e=mi()
uf=DSU(n+m)
line=[]
for _ in range(e):
    u,v=mmi()
    line.append((u,v))

q=ii()
check=[0]*e
cut=[]
for _ in range(q):
    x=ii()-1
    check[x]+=1
    cut.append(line[x])
graph=[[] for _ in range(n+m+1)]
for i in range(e):
    if check[i]==0:
        u,v=line[i]
        uf.merge(u,v)
        graph[u].append(v)
        graph[v].append(u)

for i in range(m-1):
    uf.merge(n+i,n+i+1)
ans=[]

for i in range(q):
    ans.append(uf.size(n+m-1)-m)
    u,v=cut.pop()
    uf.merge(u,v)
    

for i in range(q):
    print(ans[-1-i])


"""
n,m,e=mi()
uf=DSU(n+m+1)
line=[]
for _ in range(e):
    u,v=mmi()
    line.append((u,v))

q=ii()
check=[0]*e
cut=[]
for _ in range(q):
    x=ii()-1
    check[x]+=1
    cut.append(line[x])
graph=[[] for _ in range(n+m+1)]
for i in range(e):
    if check[i]==0:
        u,v=line[i]
        uf.merge(u,v)
        graph[u].append(v)
        graph[v].append(u)

for i in range(m):
    uf.merge(n+i,n+m)
ansl=[]
ans=0
elec=[0]*n
for i in range(n):
    if uf.same(i,n+m):
        ans+=1
        elec[i]=1
#print(cut)
for i in range(q):
    ansl.append(ans)
    u,v=cut.pop()
    if uf.same(u,n+m) and uf.same(v,n+m):
        uf.merge(u,v)
        graph[u].append(v)
        graph[v].append(u)
    elif not uf.same(u,n+m) and not uf.same(v,n+m):
        uf.merge(u,v)
        graph[u].append(v)
        graph[v].append(u)
    elif not uf.same(u,n+m) and uf.same(v,n+m):
        count=1
        vis=[u]
        elec[u]=1
        while vis:
            now=vis.pop()
            for ne in graph[now]:
                if ne < n and elec[ne]==0:
                    count+=1
                    elec[ne]=1
                    vis.append(ne)
        uf.merge(u,v)
        ans+=count
    elif uf.same(u,n+m) and not uf.same(v,n+m):
        count=1
        vis=[v]
        elec[v]=1
        while vis:
            now=vis.pop()
            for ne in graph[now]:
                if ne < n and elec[ne]==0:
                    count+=1
                    elec[ne]=1
                    vis.append(ne)
        ans+=count
        uf.merge(u,v)
for i in range(q):
    print(ansl[-1-i])"""