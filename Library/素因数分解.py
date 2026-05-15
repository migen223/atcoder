

def prime_factorize(n):#素因数分解 返り値はリスト Counterに渡すと良い感じになる
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

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

# nを素因数分解して、[素因数, その個数]のリストを作る
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])
    if temp!=1: arr.append([temp, 1])
    if arr==[]: arr.append([n, 1])
    return arr
class cumSum1D(object):
    sdat = []
    def init(self):
        pass
    def load(self, l):
        import itertools
        self.sdat = list(itertools.accumulate(itertools.chain([0], l)))
    def query(self, l, r):
        """
        query [l, r)
        """
        # assert l < r
        return self.sdat[r] - self.sdat[l]
n = int(input())
print(factorization(n))
"""
spf = SPF(n)
squares = [] # i**2がn以下の平方数を全列挙
i = 1
cnt = [0] * (n+1)
while i**2 <= n:
    cnt[i**2] += 1
    i += 1
ans = 0
cum = cumSum1D()
cum.load(cnt)
# xを総当たりする
for i in range(1, n+1):
    fact = spf.factrication(i)
    odd = 1
    # 素因数分解を行い、素因数が奇数個含まれている 素因数の積を計算する
    for a, cnt in fact:
        if cnt % 2 == 1: odd *= a
    ans += cum.query(0, n // odd + 1)
#print(ans)

"""