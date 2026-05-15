
t,m=map(int,input().split())
fuct=[1]
C=[[0 for i in range(5001)] for i in range(5001)]
C[0][0]=1
for n in range(1,5001):
    C[n][0]=1
    for k in range(1,5001):
        C[n][k]=(C[n-1][k-1]+C[n-1][k])%m


for _ in range(t):
    n=int(input())
    c=list(map(int,input().split()))
    ans=1
    s=0
    for i in range(n):
        s+=c[i]
        ans=(ans*C[s][c[i]])%m   
        
    print(ans)