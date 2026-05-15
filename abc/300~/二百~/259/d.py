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
    
n=int(input())
sx,sy,tx,ty=map(int,input().split())

def check(c1,c2):
    x1,y1,r1=c1
    x2,y2,r2=c2
    return abs(r2-r1)**2<=(x2-x1)**2+(y2-y1)**2<=(r1+r2)**2

circles=[]
for i in range(n):
    x,y,r=map(int,input().split())
    circles.append((x,y,r))

uf=DSU(n)
for i in range(n):
    x,y,r=circles[i]
    if (sx-x)**2+(sy-y)**2==r**2:
        start=i
    if (tx-x)**2+(ty-y)**2==r**2:
        goal=i

for i in range(n-1):
    for j in range(i+1,n):
        c1=circles[i]
        c2=circles[j]
        if check(c1,c2):
            uf.merge(i,j)

if uf.same(start,goal):
    print("Yes")
else:
    print("No")