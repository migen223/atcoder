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
    
n,m=map(int,input().split())
h=list(map(int,input().split()))
bit=DBIT(n)
for i in range(n):
    bit.add(i+1,i+1,h[i])

for i in range(m):
    l,r,d=map(int,input().split())
    bit.add(l,r,-d)

ans=0
for i in range(n):
    if bit.get(i+1)>=1:
        ans+=1

print(ans)

