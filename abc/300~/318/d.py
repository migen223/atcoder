n=int(input())

edge={}
for i in range(n-1):
    e=list(map(int,input().split()))
    for j in range(i+1,n):
        edge[(i,j)]=e[j-i-1]
ans=0
dp=[-10**6]*(2**n)
dp[0]=0

for i in range(2**n):
    if dp[i]!=-10**6:
        for j in range(n):
            if not (i>>j)&1:
                for k in range(j+1,n):
                    if not (i>>k)&1:
                        next=i|(1<<j)|(1<<k)
                        dp[next]=max(dp[next],dp[i]+edge[(j,k)])
                        ans=max(ans,dp[next])

"""
for i in range(2**n):
    if dp[i]!=-10**6:
        bit=format(i,'b')
        s=["0"]*n
        for j in range(len(bit)):
            if bit[-1-j]=="1":
                s[-1-j]="1"
        for j in range(n-1):
            if s[-1-j]=="0":
                for k in range(j+1,n):
                    if s[-1-k]=="0":
                        s[-1-j]="1"
                        s[-1-k]="1"
                        next=int("".join(s),2)
                        dp[next]=max(dp[next],dp[i]+edge[(j,k)])
                        ans=max(ans,dp[next])
                        s[-1-j]="0"
                        s[-1-k]="0"
                    """
#print(dp)
print(ans)   
