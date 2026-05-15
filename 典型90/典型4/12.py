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

    def count(self):
        return self.mycount
    
h,w=map(int,input().split())
q=int(input())
uf=DSU(h*w)
grid=[[0 for _ in range(w)] for  _ in range(h)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]
def toint(y,x):
    return y*w+x


for _ in range(q):
    que=list(map(lambda x:int(x)-1,input().split()))
    if que[0]==0:
        z,r,c=que
        grid[r][c]=1
        for d in range(4):
            ny=r+dy[d]
            nx=c+dx[d]
            if 0<=ny<=h-1 and 0<=nx<=w-1:
                if grid[ny][nx]==1:
                    uf.merge(toint(r,c),toint(ny,nx))           
    else:
        z,ra,ca,rb,cb=que
        if grid[ra][ca]==1 and grid[rb][cb]==1:
            if uf.same(toint(ra,ca),toint(rb,cb)):
                print("Yes")
            else:
                print("No")
        else:
            print("No")
    