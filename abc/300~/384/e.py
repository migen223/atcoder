from heapq import *
h,w,x=map(int,input().split())
p,q=map(lambda x:int(x)-1,input().split())

grid=[list(map(int,input().split())) for _ in range(h)]
dy=[-1,1,0,0]
dx=[0,0,1,-1]
power=grid[p][q]
visit=[[-1]*w for _ in range(h)]
visit[p][q]=1
visitable=[]
p_to_grid={}
for i in range(4):
    ny=p+dy[i]
    nx=q+dx[i]
    if 0<=ny<=h-1 and 0<=nx<=w-1:
        
        if grid[ny][nx] not in p_to_grid:
            p_to_grid[grid[ny][nx]]=[[ny,nx]]
            heappush(visitable,grid[ny][nx])
        else:
            p_to_grid[grid[ny][nx]].append([ny,nx])
        visit[ny][nx]=1

while visitable:
    #print(visitable)
    #print(p_to_grid)
    np=heappop(visitable)
    nl=p_to_grid[np]
    
    if power>x*np:
        power+=np*(len(p_to_grid[np]))
        p_to_grid.pop(np)
        for ne in nl:
            for i in range(4):
                ny=ne[0]+dy[i]
                nx=ne[1]+dx[i]
                if 0<=ny<=h-1 and 0<=nx<=w-1:
                    if visit[ny][nx]==-1:
                        visit[ny][nx]=1
                        if grid[ny][nx] not in p_to_grid:
                            p_to_grid[grid[ny][nx]]=[[ny,nx]]
                            heappush(visitable,grid[ny][nx])
                        else:
                            p_to_grid[grid[ny][nx]].append([ny,nx])
    else:
        break
print(power)

    