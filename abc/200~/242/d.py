import sys
from functools import lru_cache
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


s=input()
q=ii()
dic={"A":0,"B":1,"C":2}
l="ABC"


def solve(t,k):
    #debug(t,k)
    if k==0:
        return l[(dic[s[0]]+t)%3]
    if t==0:
        return s[k]
    
    
    pre=solve(t-1,k//2)
    return l[(dic[pre]+k%2+1)%3]
    

for _ in range(q):
    t,k=mi()
    k-=1
    print(solve(t,k))


"""
def Si(s,i):
    l=["A","B","C"]
    if s=="A":
        return l[i]
    if s=="B":
        return l[(1+i)%3]
    if s=="C":
        return l[i-1]

def solve(t,nowt,k,sl):
    global ans
    debug(t,nowt,k,sl)
    count=0
    if nowt==t:
        ans=sl[k-1]
        return 
    for i in range(len(sl)):
        count+=2**(t-nowt)
        #print(k,count,"k,count")
        if k<=count:
            solve(t,nowt+1,k-(count-(2**(t-nowt))),[Si(sl[i],1),Si(sl[i],2)])
            return
    solve(t,nowt+1,k-(count-(2**(t-nowt))),[Si(sl[i],1),Si(sl[i],2)])


for _ in range(q):
    t,k=mi()
    ans=""
    #debug(t,k)
    solve(t,0,k,s)
    print(ans)



CBBAACCCCC
1
57530144230160008 659279164847814847
"""