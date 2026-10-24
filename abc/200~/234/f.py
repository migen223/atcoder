import sys
from itertools import permutations
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

s=list(input())
n=len(s)

rle=[]
s.sort()
rle.append([s[0],1])
for i in range(1,n):
    if s[i]==rle[-1][0]:
        rle[-1][1]+=1
    else:
        rle.append([s[i],1])

dp=[[0 for _ in range(len(rle))] for _ in range(n+1)]
for i in range(1,rle[0][1]+1):
    dp[i][0]+=1

for i in range(len(rle)):
    dp[0][i]+=1
fact=[1,1,2]
for i in range(3,5001):
    fact.append((fact[-1]*i)%mod)


rfact=[]
for i in range(5001):
    rfact.append(pow(fact[i],-1,mod)%mod)

def C(n,k):
    return (fact[n]*(rfact[k])%mod*(rfact[n-k]%mod))%mod

ans=0
for i in range(1,len(rle)):
    for j in range(1,n+1):
        for k in range(rle[i][1]+1):
            if 0<=j-k<=n:
                #print(i,j,k,C(j,k))
                dp[j][i]+=dp[j-k][i-1]*C(j,k)
                dp[j][i]%=mod
                #debug(j,i,dp[j][i])
            else:
                break
#print(dp)
for i in range(1,n+1):
    ans+=dp[i][-1]
    ans%=mod
print(ans)

"""
def create():
    res=set()
    for i in range(n):
        for p in permutations(s,i+1):
            res.add("".join(p))
    return res
        
def createn(n):
    res=set()
    for p in permutations(s,n):
        res.add("".join(p))
    return res

print(create())
print(len(create()))

"""