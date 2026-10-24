
n,k,p=map(int,input().split())
p+=1
dp=[[10**32 for _ in range(n)] for _ in range(p**k)]
plan=[]
for i in range(n):
    ca=list(map(int,input().split()))
    c=ca[0]
    a=ca[1:]
    plan.append((c,a))

def toint(l):
    res=0
    for i in range(k):
        res+=l[i]*(p**i)
    return res

def tol(n):
    res=[0]*k
    for i in range(k-1,-1,-1):
        ad=n//(p**i)
        n-=ad*(p**i)
        #print("n=",n,ad,p**i)
        res[i]=ad
    return res

#print(plan)
l=[min(p-1,plan[0][1][i]) for i in range(k)]
#print(toint(l),l)
dp[toint(l)][0]=plan[0][0]
#se=set()
#se.add(tuple(l))
for i in range(n-1):
    nc,nl=plan[i+1]
    #print(nc,nl)
    ni=toint(nl)
    #dp[ni][i]=min(dp[ni][i],nc)
    for j in range(p**k):
        if dp[j][i]!=10**32:
            next=tol(j)
            #print("next",next,nl,dp[j][i])
            for z in range(k):
                next[z]=min(next[z]+nl[z],p-1)
            nexti=toint(next)
            #print("jfae",next,dp[nexti][i+1],dp[j][i]+nc)
            #se.add(tuple(next))
            dp[nexti][i+1]=min(dp[nexti][i+1],dp[j][i]+nc,dp[nexti][i])
            dp[j][i+1]=min(dp[j][i],dp[j][i+1])
    dp[ni][i+1]=min(dp[ni][i+1],nc)
    #se.add(tuple(nl))
    #print(dp)
    #print(se)
ans=dp[-1][-1]
if ans==10**32:
    print(-1)
else:
    print(ans)

"""
for i in range(p**k+1):
    print(tol(i),i)


print(toint(l))
dp[toint(l)]=plan[0][0]

for i in range(1,n):
    nc,nl=plan[i]
    ni=toint(nl)
    dp[ni]=min(dp[ni],nc)
    for j in range(k**p,-1,-1):

        pre=tol(j)
        f=0
        for z in range(k):
            pre[z]-=nl[z]
            pre[z]=max(pre[z],0)
        if f==0:
            dp[j]=min(dp[j],dp[toint(pre)]+nc)
    print(dp)

print(dp[-1])

"""
"""
5 2 2
5 1 1
4 2 1
2 1 0
9 2 2
3 0 1
"""