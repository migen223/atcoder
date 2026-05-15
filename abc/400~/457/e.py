from bisect import *

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
    return min(x,y)
#単位元
def e():
    return 2*10**5+1

n,m=map(int,input().split())

clo=[]
ccount={}
start={}
end={}
for i in range(m):
    l,r=map(int,input().split())
    if l in start:
        start[l].append(r)
    else:
        start[l]=[r]
    if r in end:
        end[r].append(l)
    else:
        end[r]=[l]
    clo.append((l,r))
    if (l,r) in ccount:
        ccount[(l,r)]+=1
    else:
        ccount[(l,r)]=1

mini={}
for s in start:
    start[s].sort()
    mini[s]=start[s][0]
for ei in end:
    end[ei].sort()

st=SegTree(op,e,n+1)
for mi in mini:
    st.set(mi,mini[mi])

clo.sort()


q=int(input())
for i in range(q):
    s,t=map(int,input().split())
    #print("s,t",s,t)
    if (s,t) in ccount:
        if ccount[(s,t)]>=2:
            print("Yes")
        else:
            if s==t:
                print("No")
                continue
            mi1=st.prod(s,t)
            mi2=st.prod(s+1,t+1)
            #print("s",st.get(s),"t",st.get(t))
            #print("mi1",mi1,"mi2",mi2)
            if s<=mi1<=t-1 or s+1<=mi2<=t :
                print("Yes")
            else:
                print("No")
    else:
        if s in start and t in end:
            li=bisect_right(start[s],t)
            if li==0:
                print("No")
                continue
            ri=bisect_left(end[t],s)
            if len(end[t])==ri:
                print("No")
                continue
            l=start[s][li-1]
            r=end[t][ri]
           # print("l,r",l,r)
            if l+1>=r:
                print("Yes")
            else:
                print("No")
        else:
            print("No")


"""
4 3
1 2
1 1
3 4
4
1 4
2 4
1 2
1 1


"""