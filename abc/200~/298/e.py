import sys
from collections import deque
from math import gcd
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
def getpro(x,y): #x/y
    g=gcd(x,y)
    x//=g
    y//=g
    return (x*pow(y,-1,mod))%mod
 
n,a,b,p,q=mi()
dpt=[[0 for _ in range(n+1)] for _ in range(n)] #dp[ターン数][そこにいる確率]
dpa=[[0 for _ in range(n+1)] for _ in range(n)]
dpt[0][a]=1
dpa[0][b]=1

for i in range(n-1):
    for j in range(n):
        if dpt[i][j]>0:
            for k in range(1,p+1):
                if j+k<n :
                    nextpro=(dpt[i][j]*getpro(1,p))%mod
                    dpt[i+1][j+k]+=nextpro
                else:
                    #print(p)
                    nextpro=(dpt[i][j]*getpro(p-k+1,p))%mod
                    dpt[i+1][n]+=nextpro
                    break
for i in range(n-1):
    for j in range(n):
        if dpa[i][j]>0:
            for k in range(1,q+1):
                if j+k<n :
                    nextpro=(dpa[i][j]*getpro(1,q))%mod
                    dpa[i+1][j+k]+=nextpro
                else:
                    nextpro=(dpa[i][j]*getpro(q-k+1,q))%mod
                    dpa[i+1][n]+=nextpro
                    break
#print(dpt)
#print(dpa)
ans=0
for i in range(1,n):
    ao=0
    for j in range(n):
        ao+=dpa[i-1][j]
        ao%=mod
    #debug(ao)
    ans+=ao*dpt[i][-1]
    ans%=mod
print(ans)

"""
tk={}
ao={}
tk[0]=[(a,1)] #位置,確率
ao[0]=[(b,1)]
def getpro(x,y): #x/y
    #g=gcd(x,y)
    #x//=g
    #y//=g
    return (x*pow(y,-1,mod))%mod

v=deque([(a,1,0)])
seta=set([(a,0)])

while v:
    now,pro,dep=v.popleft()
    #debug(now,pro,dep)
    for i in range(1,p+1):
        if now+i<n and (now+i,dep+1) not in seta:
            nextpro=(pro*getpro(1,p))%mod
            v.append((now+i,nextpro,dep+1))
            seta.add((now+i,dep+1))
            if dep+1 not in ao:
                ao[dep+1]=[(now+i,nextpro)]
            else:
                ao[dep+1].append((now+i,nextpro))
        else:
            nextpro=(pro*getpro(p-i+1,p))%mod
            if dep+1 not in ao:
                ao[dep+1]=[(n,nextpro)]
            else:
                ao[dep+1].append((n,nextpro))
            break


v=deque([(b,1,0)])
sett=set([(b,0)])
while v:
    now,pro,dep=v.popleft()
    #debug(now,pro,dep)
    for i in range(1,q+1):
        if now+i<n and (now+i,dep+1) not in sett:
            nextpro=(pro*getpro(1,q))%mod
            v.append((now+i,nextpro,dep+1))
            sett.add((now+i,dep+1))
            if dep+1 not in tk:
                tk[dep+1]=[(now+i,nextpro)]
            else:
                tk[dep+1].append((now+i,nextpro))
        else:
            nextpro=(pro*getpro(q-i+1,q))%mod
            if dep+1 not in tk:
                tk[dep+1]=[(n,nextpro)]
            else:
                tk[dep+1].append((n,nextpro))
            break

#print(ao)
#print(tk)
ans=0

for i in range(1,n+1):
    if i not in ao:
        break
    l=ao[i]
    #print("aiaw",l)
    if l[-1][0]!=n:
        continue
    if i-1 not in tk:
        continue
    tkp=0
    for tkpi in tk[i-1]:
        #debug(tkpi)
        if tkpi[0]>=n:
            break
        tkp+=tkpi[1]
        tkp%=mod
    ans+=tkp*l[-1][1]
    ans%=mod
    
        
print(ans)"""