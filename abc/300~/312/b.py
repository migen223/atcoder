
n,m=map(int,input().split())
grid=[list(input()) for i in range(n)]

ans=[]
for i in range(n-9+1):
    for j in range(m-9+1):
        f=0
        for k in range(3):
            for l in range(3):
                if grid[i+k][j+l]==".":
                    f+=1
                    break
        for k in range(4):
            if grid[i+3][j+k]=="#":
                f+=1
                break
        for k in range(3):
            if grid[i+k][j+3]=="#":
                f+=1
                break
        for k in range(4):
            if grid[i+5+k][j+5]=="#":
                f+=1
                break
        for k in range(3):
            if grid[i+5][j+5+k]=="#":
                f+=1
                break
        for k in range(3):
            for l in range(3):
                #print(i,j,k,l)
                if grid[i+6+k][j+6+l]==".":
                    f+=1
                    break
        if f==0:
            ans.append((i+1,j+1))
for i in ans:
    print(*i)
