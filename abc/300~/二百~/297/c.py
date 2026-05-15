h,w=map(int,input().split())

grid=[list(input()) for i in range(h)]
ans=0
for i in range(h):
    for j in range(w-1):
        if grid[i][j]=="T" and grid[i][j+1]=="T":
            grid[i][j]="P"
            grid[i][j+1]="C"
for i in range(h):
    print("".join(grid[i]))

