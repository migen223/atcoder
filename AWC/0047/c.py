
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
n,q=map(int,input().split())

a=list(map(int,input().split()))
bit=DBIT(n)
for i in range(n):
    bit.add(i+1,i+1,a[i])

for _ in range(q):
    que=list(map(int,input().split()))
    if que[0]==1:
        qu,l,r,x=que
        bit.add(l,r,x)
    elif que[0]==2:
        p=que[1]
        print(bit.get(p))
