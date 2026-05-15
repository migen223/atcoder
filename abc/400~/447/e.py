
#union-find
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

edges=[]
graph=[set() for i in range(n+1)]
for i in range(m):
    u,v=map(lambda x:int(x)-1,input().split())
    edges.append((u,v,i+1))
uf=DSU(n)
p=998244353 
s=0
for i in range(1,1+m):
    s+=pow(2,i,p)
ans=0

while edges:
    u,v,i=edges.pop()
    if uf.same(u,v) or uf.size(u)+uf.size(v)<n:
        uf.merge(u,v)
        ans+=pow(2,i,p)

        
#print(ans,s)
print((s-ans)%p)
    
    
