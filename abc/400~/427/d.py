
t=int(input())

for i in range(t):
    n,m,k=map(int,input().split())
    s=input()
    graph=[[] for _ in range(n+1)]
    for j in range(m):
        u,v=map(int,input().split())
        graph[u].append(v)
    dp=[[False]*(1+n) for _ in range(2*k+1)]
    for i in  range(1,n+1):
        if s[i-1]=="A":
            dp[-1][i]=True
        else:
            dp[-1][i]=False
    
    for i in range(2*k-1,-1,-1):
        for j in range(1,n+1):
            if i%2==1:
                for k in graph[j]:
                    f=0
                    if not dp[i+1][k]:
                        f+=1
                        dp[i][j]=False
                        break
                    if f==0:
                        dp[i][j]=True
            else:
                for k in graph[j]:
                    f=0
                    if dp[i+1][k]:
                        f+=1
                        dp[i][j]=True
                        break
    if dp[0][1]:
        print("Alice")
    else:
        print("Bob")
"""
    print("DP")               
    for i in range(2*k+1):
        print(*dp[i])
"""
    