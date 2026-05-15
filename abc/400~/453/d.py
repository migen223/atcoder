from collections import deque
import sys
h,w=map(int,input().split())
grid=[input() for i in range(h)]

dy=[-1,1,0,0]
dx=[0,0,-1,1]
dic={0:"U",1:"D",2:"L",3:"R"}
move=set([".","x","o","S","G"])
start=[-1,-1]

for i in range(h):
    for j in range(w):
        if grid[i][j]=="S":
            start=[i,j]
            break   
    if start[0]!=-1:
        break


v=deque([[start[0],start[1],-1]])

vis=[[[-1 for i in range(w)] for i in range(h)] for _ in range(4)]
for i in range(4):
    vis[i][start[0]][start[1]]=-2


while v:
    y,x,d=v.popleft()
    if grid[y][x]=="S":
        for dir in range(4):
            ny=y+dy[dir]
            nx=x+dx[dir]
            if 0<=nx<=w-1 and 0<= ny <=h-1 :
                if vis[dir][ny][nx]==-1 and grid[ny][nx] in move:
                    vis[dir][ny][nx]=-2
                    v.append((ny,nx,dir))
    elif grid[y][x]==".":
        for dir in range(4):
            ny=y+dy[dir]
            nx=x+dx[dir]
            if 0<=nx<=w-1 and 0<= ny <=h-1 :
                if vis[dir][ny][nx]==-1 and grid[ny][nx] in move:
                    vis[dir][ny][nx]=d
                    v.append((ny,nx,dir))
    elif grid[y][x]=="o":
        ny=y+dy[d]
        nx=x+dx[d]
        if 0<=nx<=w-1 and 0<= ny <=h-1 :
            if vis[d][ny][nx]==-1 and grid[ny][nx] in move:
                vis[d][ny][nx]=d
                v.append((ny,nx,d))
    elif grid[y][x]=="x":
        for dir in range(4):
            if dir==d:
                continue
            ny=y+dy[dir]
            nx=x+dx[dir]
            if 0<=nx<=w-1 and 0<= ny <=h-1 :
                if vis[dir][ny][nx]==-1 and grid[ny][nx] in move:
                    vis[dir][ny][nx]=d
                    v.append((ny,nx,dir))
            
    elif grid[y][x]=="G":
        """
        print("d=",d)
        print(y,x,d)
        for i in range(4):
            print()
            for j in range(h):
                
                print(*vis[i][j])
        #sys.exit()"""
        ans=[dic[d]]
        while vis[d][y][x]!=-2:
            ne=vis[d][y][x]
            y-=dy[d]
            x-=dx[d]
            d=ne
            #print(y,x,d,ne,"huage")
            if d==-2:
                break
            
            ans.append(dic[d])
        ans.reverse()
        print("Yes")
        print("".join(ans))
        sys.exit()
        
print("No")

    