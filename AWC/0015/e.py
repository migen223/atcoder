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

n,q=map(int,input().split())
p=list(map(int,input().split()))
que=[]

for i in range(q):
    l,r=map(int,input().split())
    que.append((l,r,i))
que.sort(key=lambda x:x[1])
ans=[-1]*q
use={}
for i in set(p):
    use[i]=0
right=0
bit=DBIT(n)

for l,r,i in que:
    if right<=n:
        for k in range(right,r):
            #print("use",use[p[k]]+1,p[k],k+1)
            bit.add(use[p[k]]+1,k+1,1)
            use[p[k]]=k+1
        right=r
    ans[i]=bit.get(l)

for i in range(q):
    print(ans[i])

