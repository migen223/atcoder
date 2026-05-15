import sys
h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]
visit=[[-1]*w for i in range(h)]

start=[]
for y in range(h):
    for x in range(w):
        if grid[y][x]=="S":
            for k in range(4):
                ny=y+dy[k]
                nx=x+dx[k]
                if 0<=nx<=w-1 and 0<=ny<=h-1:
                    if grid[ny][nx]==".":
                        start.append((ny,nx))

id=0
for i in range(len(start)):
    visitable=[(start[i][0],start[i][1])]
    visit[start[i][0]][start[i][1]]=i
    while visitable:
        y,x=visitable.pop()
        for j in range(4):
            ny=y+dy[j]
            nx=x+dx[j]
            if 0<=ny<=h-1 and 0<=nx<=w-1:
                if grid[ny][nx]==".":
                    if visit[ny][nx]==-1:
                        visit[ny][nx]=i
                        visitable.append((ny,nx))
                    elif visit[ny][nx]!=i:
                        print("Yes")
                        sys.exit()
print("No")