import sys

n,x=map(int,input().split())

an=[]
bn=[]
dp=[[0]*(x+1) for i in range(n+1)]
dp[0][0]=1
for i in range(n):
    a,b=map(int,input().split())
    an.append(a)
    bn.append(b)


    
for i in range(1,n+1):
    for j in range(x+1):
        if dp[i-1][j]==1:
            for k in range(bn[i-1]+1):
                if j+an[i-1]*k<=x:
                    dp[i][j+an[i-1]*k]=1
                else:
                    break
    if dp[i][x]==1:
        print("Yes")
        #print(dp)
        sys.exit()
print("No")




