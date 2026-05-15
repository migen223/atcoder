
n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=set((map(int,input().split())))
x=int(input())
dp=[0]*(x+1)
dp[0]=1
for i in range(x+1):
    if dp[i]==1:
        for j in range(n):
            if i+a[j]<=x: 
                if i+a[j] not in b:
                    dp[i+a[j]]=1
#print(dp)
if dp[x]==0:
    print("No")
else:
    print("Yes")


