import sys
from collections import Counter
from collections import defaultdict
"""
事前計算 O(NlogN)
クエリ O(logN)
で素因数分解をする
"""
class SPF():
    def __init__(self, n):
        self.spf = [0] * (n+1)
        self.isPrime = [True] * (n+1)
        self.isPrime[0] = False
        self.isPrime[1] = False
        self.prime = []
        for i in range(2, n + 1):
            if self.isPrime[i]:
                self.prime.append(i)
                self.spf[i] = i
            for p in self.prime:
                if i * p >  n: break
                if p > self.spf[i]: break
                self.isPrime[i * p] = False
                self.spf[i * p] = p
    def factrication(self, x):
        cnt = defaultdict(int)
        assert  x > 0
        if x == 1: return tuple( [(1,1)] )
        while x != 1:
            cnt[self.spf[x]] += 1
            x //= self.spf[x]
        res = []
        for k in cnt: res.append( (k, cnt[k]) )
        return res
    
def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]

n=ii()

squ=[]
se=set([])
for i in range(1,n+1):
    squ.append(i**2)
    se.add(i**2)

spf=SPF(n)
f=[]
for i in range(1,n+1):
    ma=1
    l=spf.factrication(i)
    for li in l:
        if li[1]>=2:
            if li[1]%2==0:
                ma*=li[0]**li[1]
            else:
                ma*=li[0]**(li[1]-1)
    #debug(ma,i)
    f.append(i//ma)

c=Counter(f)
#print(c)
ans=n
for mc in c.most_common():
    if mc[1]>1:
        ans+=mc[1]*(mc[1]-1)
print(ans)

"""
ans=0
for i in range(1,n+1):
    for j in range(n//i):
        print(i,j,squ[i-1+(i*j)],squ[i-1+(i*j)]//i)
        if squ[i-1+(i*j)]//i<=n:
            if i==squ[i-1+(i*j)]//i:
                ans+=1
            else:
                ans+=2
print(ans)


ans=[]
for i in range(1,1+n):
    for j in range(1,1+n):
        if i*j in se:
            ans.append((i,j,i*j))
print(ans)
print(len(ans))"""
