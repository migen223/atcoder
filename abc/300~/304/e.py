from collections import defaultdict
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
uf=DSU(n+1)
for _ in range(m):
    u,v=map(int,input().split())
    uf.merge(u,v)

ban=set()
k=int(input())
for _ in range(k):
    x,y=map(int,input().split())
    if not uf.same(x,y):
        ban.add((uf.leader(x),uf.leader(y)))
        ban.add((uf.leader(y),uf.leader(x)))

q=int(input())
for _ in range(q):
    p,q=map(int,input().split())
    if uf.same(p,q):
        print("Yes")
    else:
        if (uf.leader(p),uf.leader(q)) in ban:
            print("No")
        else:
            print("Yes")
