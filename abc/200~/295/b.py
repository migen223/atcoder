
h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]

dy=[-1,0,1,0]
dx=[0,-1,0,1]

visit=set()
for i in range(h):
    for j in range(w):  
        if grid[i][j]=="#":
            f=0
            for y in range(h):
                for x in range(w):
                    if grid[y][x]!="#" and grid[y][x]!=".":
                        if abs(y-i)+abs(j-x)<=int(grid[y][x]):
                            grid[i][j]="."
                            f=1
                            break
                if f==1:
                    break
for i in range(h):
    for j in range(w):
        if grid[i][j]!="#" and grid[i][j]!=".":
            grid[i][j]="."
for i in range(h):
    print("".join(grid[i]))


                


