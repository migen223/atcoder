import sys
n,d=map(int,input().split())
p=list(map(int,input().split()))
w=list(map(int,input().split()))
mod=998244353 
sp=sum(p)
smod=pow(sp,-1,mod)
w=sum(w)

ans=1
for i in range(n):
    t=(p[i]*w*smod)%mod
    ans*=t
    ans%=mod

print(ans)