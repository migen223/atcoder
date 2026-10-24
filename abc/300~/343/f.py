import sys
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
    res=[-inf,0,-inf,0]
    l=[x[0],x[2],y[0],y[2]]
    ma=max(l)
    ma2=-inf
    for i in range(4):
        if l[i]==ma:
            continue
        ma2=max(l[i],ma2)
    res[0]=ma
    res[2]=ma2
    for i in [0,2]:
        if x[i]==ma:
            res[1]+=x[i+1]
        if x[i]==ma2:
            res[3]+=x[i+1]
        if y[i]==ma:
            res[1]+=y[i+1]
        if y[i]==ma2:
            res[3]+=y[i+1]
    return res
#単位元
def e():
    return [-inf,0,-inf,0]




def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7c
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]

n,q=mi()
a=li()
va=[[a[i],1,-inf,0] for i in range(n)]
#print(va)
st=SegTree(op,e,n,va)


for _ in range(q):
    que=li()
    if que[0]==1:
        _,p,x=que
        st.set(p-1,[x,1,-inf,0])
    else:
        _,l,r=que
        ans=st.prod(l-1,r)
        #debug(ans)
        print(ans[3])
        
