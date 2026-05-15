
t=int(input())
dx=[-1,0,1]
for _ in range(t):
    n,c=map(int,input().split())
    grid=[list(input()) for i in range(n)]
    fw=[-1]*n
    for i in range(n):
        for j in range(n-1,-1,-1):
            if grid[j][i]=="#":
                fw[i]=j
                break
    dp=[[0]*n for i in range(n)]
    for i in range(n):
        dp[i][c-1]=1
    #print("fw",fw)
    for y in range(n-2,-1,-1):
        for x in range(n):
            f=0
            if dp[y][x]!=1:
                for k in range(3):
                    nx=x+dx[k]
                    if 0<=nx<=n-1:
                        if dp[y+1][nx]==1:
                            f+=1
                            break
                if f==1:
                    if grid[y][x]==".":
                        dp[y][x]=1
                    else:
                        if fw[x]==y:
                            for k in range(y+1):
                                dp[k][x]=1 
    ans=["0"]*n
    for i in range(n):
        if dp[0][i]==1:
            ans[i]="1"
    """
    print("dp")
    for i in range(n):
        print(*dp[i])
"""
    print("".join(ans))  


    """
    while visitable:
        y,x=visitable.pop()
        grid[y][x]="!"
        for i in range(3):
            ny=y-1
            nx=x+dx[i]
            if 0<=ny<=n-1 and 0<=nx<=n-1:
                if grid[ny][nx]==".":
                    visitable.append((ny,nx))
    
    print("grid")
    for i in range(n):
        print(*grid[i])
    ans=["0"]*n
    for i in range(n):
        if grid[0][i]=="!":
            ans[i]="1"
        else:
            a+=2"""