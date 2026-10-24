import sys
#union-find
from collections import defaultdict
from sortedcontainers import SortedList
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

#結合 x,yの親のうち、サイズが大きい方の親になる
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
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]


n,q=mi()

uf=DSU(n)
l=[SortedList([i]) for i in range(n)]
for _ in range(q):
    que=li()
    if que[0]==1:
        _,u,v=que
        u-=1
        v-=1
        ul=uf.leader(u)
        vl=uf.leader(v)
        if not uf.same(u,v):
            uf.merge(u,v)
            if ul!=uf.leader(u):
                for ver in l[ul]:
                    l[vl].add(ver)
            else:
                for ver in l[vl]:
                    l[ul].add(ver)
    else:
        _,v,k=que
        v-=1
        if len(l[uf.leader(v)])>=k:
            print(l[uf.leader(v)][-k]+1)
        else:
            print(-1)
    #for  i in range(n):
    #    debug(l[i])
    
       