h,w,n=map(int,input().split())
grid=[]
for i in range(h):
    line=["."]*w
    grid.append(line)
now=[0,0]
d=[[-1,0],[0,1],[1,0],[0,-1]]
dir=0
for i in range(n):
    if grid[now[0]][now[1]]==".":
        grid[now[0]][now[1]]="#"
        dir=(dir+1)%4
        now[0]=(now[0]+d[dir][0])%h
        now[1]=(now[1]+d[dir][1])%w
    else:
        grid[now[0]][now[1]]="."
        dir=(dir-1)%4
        now[0]=(now[0]+d[dir][0])%h
        now[1]=(now[1]+d[dir][1])%w
for i in range(h):
    for j in range(w):
        print(grid[i][j],end="")
    print()