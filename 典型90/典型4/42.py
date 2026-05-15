
k=int(input())
mod=10**9+7  

if k%9!=0:
    print(0)
else:
    
    dp=[0]*(k+1)
    dp[0]+=1
    for i in range(1,k+1):
        j=min(9,i)
        for l in range(1,j+1):
            dp[i]+=dp[i-l]
            dp[i]%=mod
    
    print(dp[-1])
    