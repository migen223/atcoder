
h,w,k=map(int,input().split())

grid=[list(input()) for i in range(h)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]
ans=0

visit=[[-1]*w for i in range(h)]

def pri(l):
    for i in range(h):
        print(*l[i])
    print()

def solve(cond,depth,y,x):
    global ans
    for i in range(4):
        ny=dy[i]+y
        nx=dx[i]+x
        if 0<=ny<=h-1 and 0<=nx<=w-1:
            if cond[ny][nx]==-1 and grid[ny][nx]==".":
                if depth+1==k:
                    ans+=1
                    #pri(cond)
                else:
                    cond[ny][nx]=1
                    solve(cond,depth+1,ny,nx)
                    cond[ny][nx]=-1

for i in range(h):
    for j in range(w):
        if grid[i][j]==".":
            visit[i][j]=1
            solve(visit,0,i,j)
            visit[i][j]=-1

print(ans)