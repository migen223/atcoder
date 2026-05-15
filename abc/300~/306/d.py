
n=int(input())
cond=0
dp0=[0]*(n+1)
dp1=[0]*(n+1)
dp1[0]=-10**12
for i in range(1,n+1):
    x,y=map(int,input().split()) #X=0が毒入り
    if x==1:
        dp0[i]=dp0[i-1]
        dp1[i]=max(dp0[i-1]+y,dp1[i-1])
    else:
        dp0[i]=max(dp0[i-1]+y,dp0[i-1],dp1[i-1]+y)
        dp1[i]=dp1[i-1]
print(max(dp1[n],dp0[n]))


