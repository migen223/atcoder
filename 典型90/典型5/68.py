import sys
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

n=ii()
q=ii()

query=[]
q0=[-inf]*(n-1)
for _ in range(q):
    t,x,y,v=mi()
    query.append((t,x-1,y-1,v))
    if t==0:
        q0[x-1]=v

dif=[0]
for i in range(n-1):
    if q0[i]>=0:
        dif.append(q0[i]-dif[-1])
    else:
        dif.append(0)
    
uf=DSU(n)
for t,x,y,v in query:
    if t==0:
        uf.merge(x,y)
    else:
        if uf.same(x,y):
            if abs(x-y)%2==0:
                print(dif[y]+v-dif[x])
            else:
                print(dif[y]-(v-dif[x]))
        else:
            print("Ambiguous")
