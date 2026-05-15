h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]

ans=0
for i in range(h):
    for j in range(w):
        if grid[i][j]=="#":
            ans+=1
print(ans)