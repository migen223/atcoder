from math import sqrt
from itertools import product
n=int(input())
p=list(map(int,input().split()))

def calc(n):
    return 10*(1-0.9**n)

dp=[[0 for _ in range(n)] for _ in range(n)]
dp[0][0]=p[0]

for i in range(1,n):
    pi=p[i]
    dp[0][i]=max(dp[0][i-1],pi)
    for j in range(1,n):
        if dp[j-1][i-1]!=0:
            dp[j][i]=max(dp[j][i],dp[j-1][i-1]*0.9+pi,dp[j][i-1])

#print()
#for i in range(n):
#    print(*dp[i])
#print()
ans=-10**32

for i in range(n):
    ans=max(ans,dp[i][-1]/calc(i+1)-1200/sqrt(i+1))
    #print(ans,i)
print(ans)
"""
def calc(l):
    k=len(l)
    nume=0
    deno=0
    for i in range(k):
        nume+=l[i]*0.9**(k-i-1)
        deno+=0.9**(k-i-1)
    res=nume/deno-1200/sqrt(k)
    return res

ma=(-10**32,[])
for pr in product([0,1],repeat=n):
    l=[]
    for i in range(n):
        if pr[i]==1:
            l.append(p[i])
    if len(l)>0:
        print(l,calc(l))
        ma=max(ma,(calc(l),l))

for i in range(1,n):
    print(f"1200/{i+1}-1200/{i}=",1200/sqrt(i+1)-1200/sqrt(i))
    
print(ma)"""
"""
5
100 500 600 200 300

4 
1 5000 1 3000

"""
