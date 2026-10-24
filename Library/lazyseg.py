from atcoder.lazysegtree import LazySegTree

inf = 2 ** 61 - 1

#区間加算
"""
from atcoder.lazysegtree import LazySegTree
def mapping(f,a): return f+a
def composition(f,g):return f+g
id_=0
"""
#区間代入
#"""
from atcoder.lazysegtree import LazySegTree
id_=-1
def mapping(f,a):
    if f==-1:
        return a
    return f

def composition(f,g):
    if f==-1:
        return g
    return f
#"""

#区間max
#"""
def op(x,y): return max(x,y)
e=-inf
#"""

#区間min
"""
def op(x,y): return min(x,y)
e=inf
"""

#区間和
"""
def op(x,y): return x+y
e=0
"""

"""
op:定義する関数　(区間に対する演算)
e:演算に対する単位元
mapping(f,a):値aに対するfの操作
compoisiton(f,g):操作の合成 操作gに対するfの操作
id_:操作の単位元(?) 区間加算なら0,区間乗算なら１

mapping(compisition(f,g),a)==mapping(f,mapping(g,a))
composition(f,id_)=f
composition(id_,f)=f

apply(l,r,x):[l,r-1]に値xの操作を実行
prod(l,r):[l,r-1]の演算結果
get(i) : i番めの値の取得
"""

w,n=map(int,input().split())
l=[e]*n
seg=LazySegTree(op,e,mapping,composition,id_,l)

for _ in range(n):
    l,r=map(int,input().split())
    h=seg.prod(l,r+1)
    seg.apply(l,r+1,h+1)