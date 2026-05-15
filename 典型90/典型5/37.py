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

w,n=map(int,input().split())

st=SegTree(op,e,w+1)
dp=[[0 for _ in range(n)] for i in range(w+1)]

for i in range(n):
    l,r,v=map(int,input().split())
    if i==0:
        for j in range(l,r+1):
            st.set(j,v)
            dp[j][0]=v
        continue
    for j in range(l,r+1):
        ma=max(dp[j][i],v)
        dp[j][i]=v
    for j in range(w+1):
        dp[j][i]=max(dp[j][i-1],dp[j][i])
        if 0>j-l:
            continue
        ma=st.prod(max(0,j-r),max(0,j-l)+1)
        if ma==0:
            continue
        dp[j][i]=max(dp[j][i],ma+v)
    for j in range(w+1):
        st.set(j,dp[j][i])
    

#for i in range(w+1):
 #   print(i,dp[i])
if dp[-1][-1]==0:
    print(-1)
else:
    print(dp[-1][-1])
