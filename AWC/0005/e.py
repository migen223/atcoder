#セグ木 https://qiita.com/AkariLuminous/items/32cbf5bc3ffb2f84a898
#0-index
class SegTree:
    #コンストラクタは(演算,単位元,配列サイズ,初期値(なくてもok))
    
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (self._size << 1)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])
    
    #値の更新 a_pをxに更新　O(演算の計算量*log(n))
    def set(self, p, x):
        p += self._size
        self._d[p] = x
        while p:
            self._d[p >> 1] = self._op(self._d[p], self._d[p ^ 1])
            p >>= 1
    
    #値の取得 a_p
    def get(self, p):
        return self._d[p + self._size]

    #区間[l,r-1]までの演算結果
    def prod(self, l, r):
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)
    
    #すべての要素の演算結果
    def all_prod(self):
        return self._d[1]

#定義する演算
def op(x,y):
    return max(x,y)
#単位元
def e():
    return 0

n,q=map(int,input().split())
a=list(map(int,input().split()))
seg=SegTree(op,e,n)
for i in range(n):
    seg.set(i,a[i])

for i in range(q):
    l,r=map(int,input().split())
    print(seg.prod(l-1,r))