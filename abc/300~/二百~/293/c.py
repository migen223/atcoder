
h,w=map(int,input().split())
grid=[list(map(int,input().split())) for i in range(h)]

ans=0
dy=[1,0]
dx=[0,1]
visitable=[[0,0,set([grid[0][0]]),set((0,0))]]
visit=set()
while visitable:
    now=visitable.pop()
    if now[0]==h-1 and now[1]==w-1:
        ans+=1
    for i in range(2):
        ny=now[0]+dy[i]
        nx=now[1]+dx[i]
        if 0<=ny<=h-1 and 0<=nx<=w-1:
            if grid[ny][nx] not in now[2] and (ny,nx) not in now[3]:
                ns=set()
                for j in now[2]:
                    ns.add(j)
                ns.add(grid[ny][nx])
                nv=set()
                for j in now[3]:
                    nv.add(j)
                nv.add((ny,nx))
                visitable.append([ny,nx,ns,nv])
    #print(visitable)
print(ans)




