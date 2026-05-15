from collections import defaultdict
class DSU():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def leader(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.leader(self.parents[x])
            return self.parents[x]

    def members(self,x):
        root=self.leader(x)
        return [i for i in range(self.n) if self.find(i) == root]

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

    def groups(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.leader(member)].append(member)
        return group_members
n,q=map(int,input().split())
black={}
color=[0]*n

uf=DSU(n)

for _ in range(q):
    que=list(map(int,input().split()))
    u=que[1]-1
    if que[0]==1:
        v=que[2]-1
        ul=uf.leader(u)
        vl=uf.leader(v)
        f=0
        if ul in black:
            f+=black[ul]
            black.pop(ul)
        if vl in black:
            f+=black[vl]
            black.pop(vl)
        uf.merge(u,v)
        if f>=1:
            black[uf.leader(u)]=f

    elif que[0]==2:
        ld=uf.leader(u)
        if color[u]==1:
            color[u]=0
            if black[ld]==1:
                black.pop(ld)
            else:
                black[ld]-=1
        else:
            color[u]=1
            if ld in black:
                black[ld]+=1
            else:
                black[ld]=1
    elif que[0]==3:
        if uf.leader(u) in black:
           print("Yes")
        else:
           print("No")
