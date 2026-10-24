import sys

from collections import defaultdict
from sortedcontainers import SortedList
#双対BIT 区間加算、一点取得
class DBIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    #内部用 i番目以降にxを加算
    def _add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

    #lからrまでにxを加算する
    def add(self, l, r, x):
        self._add(l, x)
        self._add(r + 1, -x)

    #i番目の値を求める
    def get(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    #初期設定 リストを渡してその値を埋め込む
    def setl(self,l):
        for i in range(len(l)):
            self.add(i+1,i+1,l[i])
        
    #値の設定　i番目の要素をxにする
    def set(self,i,x):
        now=self.get(i)
        self.add(i,i,x-now)

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

n,q=mi()

dic=defaultdict(SortedList)
dic=defaultdict(list)

for _ in range(q):
    l,r,x=mi()
    dic[x].append((l,r))

for d in dic:
    dic[d].sort(reverse=True)

db=DBIT(n+1)
for d in dic:
    l,r=dic[d].pop()
    while dic[d]:
        nl,nr=dic[d].pop()
        if r>=nr:
            continue
        if nl<=r<=nr:
            r=nr
        else:
            db.add(l,r,1)
            l,r=nl,nr
    db.add(l,r,1)

for i in range(1,n+1):
    print(db.get(i),end=" ")
print()

"""
    if x in dic:
        ind=dic[x].bisect_left([l,inf])
        #debug(dic[x],ind)
        pre=dic[x][ind-1]
        aft=dic[x][ind]
        c=0
        if pre[1]>=l and aft[0]<=r:
            c=1
            nl=[min(l,pre[0]),max(r,aft[1])]
            dic[x].discard(pre)
            dic[x].discard(aft)
        elif pre[0]<=l<=pre[1]+1:
            c=2
            nl=[pre[0],max(pre[1],r)]
            dic[x].discard(pre)
        elif r+1>=aft[0]:
            c=2
            nl=[l,max(r,aft[1])]
            dic[x].discard(aft)
            while dic[x][ind][1]<=r:
                dic[x].pop(ind)
            nl[1]=max(nl[1],dic[x][ind][1])
            if nl[1]==inf:
                nl[1]=r
        else:
            c=4
            nl=[l,r]
        dic[x].add(nl)
    else:
        dic[x].add([l,r])
        dic[x].add([-inf,-inf])
        dic[x].add([inf,inf])
    #print(dic[x])
    #if x==7:
     #   debug(dic[7],c)
#for d in dic:
#    print(d,dic[d])
#    print()


db=DBIT(n+1)
for d in dic:
    for i in range(1,len(dic[d])-1):
        l,r=dic[d][i]
        db.add(l,r,1)

for i in range(1,n+1):
    print(db.get(i),end=" ")
print()"""