
n=int(input())

town=[]
takahashi=0 
total=0
ans=0
for i in range(n):
    x,y,z=map(int,input().split())
    need=(x+y)//2+1-x
    town.append((z,max(0,need)))
    total+=z
#print(town)
#print(total)

if n!=1:
    dp=[[10**14]*(total+1) for i in range(n)]
    dp[0][0]=0
    dp[0][town[0][0]]=town[0][1]
    for i in range(1,n):
        cha,peo=town[i]
        for j in range(total):
            if dp[i-1][j]!=10**14:
                #print(j,cha)
                dp[i][j]=min(dp[i][j],dp[i-1][j])
                dp[i][j+cha]=min(dp[i][j+cha],dp[i-1][j]+peo)
                #print(dp[i][j+cha])
    ans=10**32
    for i in range(total//2+1,total+1):
        ans=min(ans,dp[n-1][i])
        #print(dp[n-1][i])
    print(ans)
    
else:
    print(town[0][1])

#for i in range(n):
 #   print(*dp[i])







