from collections import defaultdict

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

#要素が含まれてる集合の要素数
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
edges=[[] for _ in range(n+1)]
for i in range(m):
    a,b=map(int,input().split())
    edges[min(a,b)].append((a,b))

uf=DSU(n+1)
ans=[0]
now=0
for i in range(n,0,-1):
    now+=1
    for u,v in edges[i]:
        if not (uf.same(u,v)):
            now-=1
            uf.merge(u,v)
    ans.append(now)

ans.reverse()

for i in range(n):
    print(ans[i+1])

