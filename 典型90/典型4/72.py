import sys
sys.setrecursionlimit(10**7)
h,w=map(int,input().split())

grid=[input() for i in range(h)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]

def dfs(sy,sx,vis,y,x,d):
    l=[]
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<=h-1 and 0<=nx<=w-1:
            if grid[ny][nx]=="." and (ny,nx) not in vis:
                vis.add((ny,nx))
                l.append(dfs(sy,sx,vis,ny,nx,d+1))
                vis.remove((ny,nx))
            elif ny==sy and nx==sx and d>=3:
                l.append(d+1)
            else:
                l.append(-1)
    return max(l)

if h*w>=4:
    ans=-1
    for i in range(h):
        for j in range(w):
            if grid[i][j]==".":
                res=dfs(i,j,set([(i,j)]),i,j,0)
                ans=max(ans,res)
                #print(res,i,j)
    print(ans)
else:
    print(-1)