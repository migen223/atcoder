import sys
from bisect import bisect_left
from random import randint
from itertools import product
def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
mmi= lambda: map(lambda x:int (x)-1, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]
def dpsolve(v,dp,n):
    if n==0:
        #print(0)
        #sys.exit()
        return -1
    global se
    dp[v[0][1]][0]=v[0][0]
    for i in range(n-1):
        a,c=v[i+1]
        dp[c][i+1]=max(a,dp[c][i+1])
        for j in range(1,x+1):
            dp[j][i+1]=max(dp[j][i+1],dp[j][i])
            if 0<=j+c<=x:
                if dp[j][i]>=1:
                    dp[j+c][i+1]=max(dp[j+c][i+1],dp[j][i]+a)
            else:
                break
    res=[(0,0)]
    for i in range(1,x+1):
        if dp[i][-1]>=1:
            res.append((dp[i][-1],i))
            se.add(dp[i][-1])
    return sorted(res)

def check(m):
    cal=0
    i1=bisect_left(cand1,(m,-1))
    if i1==len(cand1):
        return False
    mi=inf
    for i in range(i1,len(cand1)):
        mi=min(mi,cand1[i][1])
    cal+=mi
    if cal>x:
        return False
    
    i2=bisect_left(cand2,(m,-1))
    if i2==len(cand2):
        return False
    mi=inf
    for i in range(i2,len(cand2)):
        mi=min(mi,cand2[i][1])
    cal+=mi
    if cal>x:
        return False
    
    i3=bisect_left(cand3,(m,-1))
    if i3==len(cand3):
        return False
    mi=inf
    for i in range(i3,len(cand3)):
        mi=min(mi,cand3[i][1])
    cal+=mi
    if cal>x:
        return False

    return True

for _ in range(100):
    n,x=randint(1,10),randint(1,10)
    v1=[]
    v2=[]
    v3=[]

    f=[]
    for _ in range(n):
        v,a,c=randint(1,3),randint(1,7),randint(1,x)
        f.append((v,a,c))
        if v==1:
            v1.append((a,c))
        elif v==2:
            v2.append((a,c))
        else:
            v3.append((a,c))

    n1=len(v1)
    n2=len(v2)
    n3=len(v3)
    dp1=[[0 for _ in range(n1)] for _ in range(x+1)]
    dp2=[[0 for _ in range(n2)] for _ in range(x+1)]
    dp3=[[0 for _ in range(n3)] for _ in range(x+1)]
    se=set()

        


    #(ビタミン、カロリー)の配列
    cand1=dpsolve(v1,dp1,n1)
    cand2=dpsolve(v2,dp2,n2)
    cand3=dpsolve(v3,dp3,n3)
    if cand1==-1 or cand2==-1 or cand3==-1:
        continue
    l=list(se)
    l.append(0)
    l.sort()


    bot=0
    top=len(l)

    

    while top-bot>1:
        m=(top+bot)//2
        if check(l[m]):
            bot=m
        else:
            top=m

    ans1=l[bot]

    ans2=-1
    for p in product([0,1],repeat=n):
        res=0
        vs=[0,0,0]
        cal=0
        for i in range(n):
            v,a,c=f[i]
            if p[i]==1:
                vs[v-1]+=a
                cal+=c
        if cal<=x:
            ans2=max(ans2,min(vs))
    if ans1!=ans2:
        print()
        print(n,x)
        for i in range(n):
            print(*f[i])
        debug(ans1,ans2)
