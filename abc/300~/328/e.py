from itertools import combinations
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

    def count(self):
        return self.mycount
    

n,m,k=map(int,input().split())

graph=[[] for _  in range(n)]
edge=[]
for _ in range(m):
    v1,v2,w=map(int,input().split())
    v1-=1
    v2-=1
    graph[v1].append((v2,w))
    graph[v2].append((v1,w))
    edge.append((v1,v2,w))

ans=10**32
for c in combinations(edge,n-1):
    uf=DSU(n)
    res=0
    f=0
    for i in range(n-1):
        u,v,w=c[i]
        if not uf.same(u,v):
            uf.merge(u,v)
            res+=w
        else:
            f+=1
            break
    if uf.count()!=1:
        f+=1
    if f==0:
        ans=min(ans,res%k)
print(ans)