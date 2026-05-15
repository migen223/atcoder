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
graph=[{} for i in range(n)]
uf=DSU(n)
unuse=deque([])

for i in range(m):
    a,b=map(lambda x:int(x)-1,input().split())
    if not uf.same(a,b):
        uf.merge(a,b)
    else:
        unuse.append([a,b,i])

root=set()
for i in range(n):
    root.add(uf.leader(i))

ans=[]
while uf.size(0)<n:
    c1,c2,num=unuse.popleft()
    r=uf.leader(c1)
    preroot=[r]
    for nr in root :
        if nr==r:
            continue
        preroot.append(nr)
        ans.append([num+1,c2+1,nr+1])
        uf.merge(c1,nr)
        break
    for pr in preroot:
        if pr in  root:
            root.discard(pr)
    root.add(uf.leader(c1))

print(len(ans))
for i in range(len(ans)):
    print(*ans[i])
