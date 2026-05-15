#union-find
from collections import defaultdict,deque
#uf=DSU(n) nは要素数
class DSU():
    #コンストラクタ
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

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
    
n,m=map(int,input().split())

graph=[[] for i in range(n+1)]
edges=set()
edges2=set()
for  i in range(m):
    u,v=map(int,input().split())
    if u==v:
        continue
    graph[u].append(v)
    graph[v].append(u)
    edges.add((min(u,v),max(u,v)))
    edges2.add((max(u,v),min(u,v)))

edges=list(edges)
edges.sort()
edges=deque(edges)
edges2=list(edges2)
edges2.sort()
edges2=deque(edges2)
#print(edges)
#print(edges2)
uf=DSU(n+1)
uf2=DSU(n+1)
for i in range(n):
    if len(edges)>0:
        while edges[0][0]==i+1:
            u,v=edges.popleft()
            uf.merge(u,v)
            if len(edges)==0:
                break
    if len(edges2)>0:
        while edges2[0][0]==i+1:
            u,v=edges2.popleft()
            uf2.merge(u,v)
            if len(edges2)==0:
                break
    if uf2.size(1)==i+1:
        print(uf.size(1)-(i+1))
    else:
        print(-1)
