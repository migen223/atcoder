from bisect import bisect_left
from collections import deque
n,x=map(int,input().split())
t=list(map(int,input().split()))
mod=998244353
dp=[0]*(x+1)
dp[0]=1

for i in range(x):
    for j in range(n):
        next=i+t[j]
        if 0<=next<=x:
            dp[next]+=dp[i]*pow(n,-1,mod)
            dp[next]%=mod

if x>=t[0]:
    ans=0
    for i in range(x,x-t[0],-1):
        ans+=dp[i]
        ans%=mod
    ans*=pow(n,-1,mod)
    ans%=mod
else:
    ans=0
    for i in range(x):
        ans+=dp[i]
        ans%=mod
    if x==0:
        ans+=1
    ans*=pow(n,-1,mod)
    ans%=mod
print(ans)

"""
f=t[0]
if x!=0:
    mus=[]
    dic={}
    for ti in t:
        if ti in dic:
            dic[ti]+=1
        else:
            mus.append(ti)
            dic[ti]=1
    mus.sort()

    w=x//(min(t))+1
    stack=deque([])
    dp=[[0 for _ in range(w)] for _ in range(x+1)]
    for ti in mus:
        if ti-1<=x:
            dp[ti-1][0]=dic[ti]
            stack.append(ti-1)
    #print(dic)
    #print(mus)
    #print(dp)


    for i in range(w):
        l=[]
        while stack:
            now=stack.popleft()
            ind=bisect_left(mus,x+1-now)
            #print("ind",ind)
            for j in range(ind):
                next=mus[j]
                #print(dp[now+next][i+1],dp[now][i]*dic[next])
                dp[now+next][i+1]=max(dp[now+next][i+1],dp[now][i]*dic[next])
                l.append(now+next)
        for li in l:
            stack.append(li)

    for i in range(x+1):
        print(*dp[i])

    ans=0
    for i in range(w):
        for j in range(x-f+1,x+1):
            ans+=dp[j][i]*pow(n**(i+2),-1,mod)
            ans%=mod
    if f>x:
        ans+=pow(n,-1,mod)
        ans%=mod
else:
    ans=pow(n,-1,mod)

print(ans)"""

"""
5 10000
1 2 3 4 5

"""