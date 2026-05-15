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

#クラスカル法
#edgesは[(頂点,頂点,重さ)]のような辺のリスト nodesは頂点数
#頂点番号は0-index 返り値は最小全域木の重さの和
#anslには最小全域木を構成している辺が格納されてる
def kruskal(edges,nodes):
    edges.sort(key=lambda x:x[2])
    uf=DSU(nodes)
    ansl=[]
    ans=0
    for i in edges:
        u,v,w=i
        if not (uf.same(u,v)):
            ansl.append((u,v))
            uf.merge(u,v)
        else:
            ans+=max(w,0)
    return ans

n,m=map(int,input().split())

edges=[]
for i in range(m):
    a,b,c=map(lambda x:int(x)-1,input().split())
    c+=1
    edges.append([a,b,c])

print(kruskal(edges,n))
