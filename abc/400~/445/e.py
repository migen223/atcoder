from collections import defaultdict
from sortedcontainers import SortedList
from math import lcm
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

t=int(input())
mod=998244353 
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    dic={}
    ans=[]
    fs=[]
    LCM=lcm(*a)
    for i in a:
        fact=factorization(i)
        fs.append(fact)
        for f in fact:
            if f[0] in dic:
                if f[0]**f[1] not in dic[f[0]]:
                    dic[f[0]].add(f[0]**f[1])
            else:
                dic[f[0]]=SortedList([1,f[0]**f[1]])
    #print("fs",fs)
    #print(dic)
    for f in fs:
        res=LCM
        for num,p in f:
            if num**p==dic[num][-1]:
                #print(f,dic[num][-1],dic[num][-2])
                res//=dic[num][-1]//dic[num][-2]
        ans.append(res%mod)
    print(*ans)

"""
600 1800 360 900 1800
447582749 506009091 523568328 588652065 196217355 471970745 921220985 738745385
747032704 756838459 344127037 146466685 159487731 555429485 826726159 884617928 322846201 298477407

600 1800 360 900 1800
430289476 506009091 523568328 785392961 430640641 471970745 921220985 738745385
747032704 756838459 89491426 490079728 53162577 42725345 120222102 605563723 322846201 298477407
"""