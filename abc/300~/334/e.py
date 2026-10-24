#union-find
from math import gcd
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
    
h,w=map(int,input().split())
mod = 998244353 
grid=[input() for i in range(h)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]

def ind(y,x):
    return x+w*y

white=[]
black=[]
uf=DSU(h*w)
for i in range(h):
    for j in range(w):
        if grid[i][j]=="#":
            ny,nx=i+1,j
            if 0<=ny<=h-1 and 0<=nx<=w-1 and grid[ny][nx]=="#":
                uf.merge(ind(i,j),ind(ny,nx))
            ny,nx=i,j+1
            if 0<=ny<=h-1 and 0<=nx<=w-1 and grid[ny][nx]=="#":
                uf.merge(ind(i,j),ind(ny,nx))
            black.append((i,j))
        else:
            white.append((i,j))

ans=0
con=0
vis=[[0 for _ in range(w)] for _ in range(h)]
for y,x in black:
    if vis[y][x]==0:
        con+=1
        vis[y][x]=1
        v=[(y,x)]
        while v:
            y,x=v.pop()
            for d in range(4):
                ny,nx=y+dy[d],x+dx[d]
                if 0<=ny<=h-1 and 0<=nx<=w-1 and grid[ny][nx]=="#" and vis[ny][nx]==0:
                    vis[ny][nx]=1
                    v.append((ny,nx))
#print(con)


ans=0
for y,x in white:
    se=set()
    for d in range(4):
        ny,nx=y+dy[d],x+dx[d]
        if 0<=ny<=h-1 and 0<=nx<=w-1 and grid[ny][nx]=="#":
            #print(ny,nx,ind(ny,nx))
            se.add(uf.leader(ind(ny,nx)))
    deno=len(white)
    nume=con-(len(se)-1)
    g=gcd(nume,deno)
    nume//=g
    deno//=g
    #print(nume,deno)
    ans+=nume*pow(deno,-1,mod)
    ans%=mod

print(ans)


