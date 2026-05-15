from collections import deque
#01-BFS
#edgesは[[(node,weight)]]の形で表されるグラフ　
def BFS01(edges, start):
    
    n=len(edges)
    node=[10**32]*n
    node[start]=0
    dq=deque([(0,start)])
    while dq:
        now=dq.popleft()
        
        pos=now[1]
        weight=now[0]
        if node[pos]<weight:
            continue
        for i in edges[pos]:
            if weight+i[1]<node[i[0]]:
                if i[1]==0:
                    dq.appendleft((weight+i[1],i[0]))
                elif i[1]==1:
                    dq.append((weight+i[1],i[0]))
                node[i[0]]=weight+i[1]
    return node 

def toint(y,x,dir):
    return h*w*dir+w*y+x

h,w=map(int,input().split())
s=list(map(lambda x:int(x)-1,input().split()))
g=list(map(lambda x:int(x)-1,input().split()))
grid=[input() for i in range(h)]

graph=[[] for _ in range(h*w*4)]

dy=[-1,1,0,0]
dx=[0,0,-1,1]
v=deque([[s[0],s[1],i] for i in range(4)])
vis=[[[-1 for _ in range(w)] for _ in range(h)]for _ in range(4)]
for i in range(4):
    vis[i][s[0]][s[1]]=0
while v:
    y,x,dir=v.popleft()
    now=toint(y,x,dir)
    if [y,x]==s:
        for d in range(4):
            if dir!=d:
                graph[now].append((toint(y,x,d),0))
    else:
        for d in range(4):
            if dir!=d :
                graph[now].append((toint(y,x,d),1))
    ny=y+dy[dir]
    nx=x+dx[dir]
    if 0<=ny<=h-1  and 0<=nx<=w-1:
        if grid[ny][nx]=="." and vis[i][ny][nx]==-1:
            vis[i][ny][nx]=0
            v.append((ny,nx,dir))
            graph[now].append((toint(ny,nx,dir),0))
for i in range(h*w*4):
    print(i,*graph[i])

"""
for i in range(h):
    for j in range(w):
        if [i,j]==s:
            for d1 in range(4):
                now=toint(i,j,d1)
                for d2 in range(4):
                    if d1!=d2:
                        ne=toint(i,j,d2)
                        graph[now].append((ne,0))
                ny=i+dy[d1]
                nx=j+dx[d1]
                if 0<=ny<=h-1 and 0<=nx<=w-1:
                    if grid[ny][nx]==".":
                        ne=toint(ny,nx,d1)
                        graph[now].append((ne,0))
                
        else:         
            if grid[i][j]==".":
                for d1 in range(4):
                    now=toint(i,j,d1)
                    for d2 in range(4):
                        if d1==d2:
                            continue
                        ne=toint(i,j,d2)
                        graph[now].append((ne,1))
                    ny=i+dy[d1]
                    nx=j+dx[d1]
                    if 0<=ny<=h-1 and 0<=nx<=w-1:
                        if grid[ny][nx]==".":
                            ne=toint(ny,nx,d1)
                            graph[now].append((ne,0))
#for i in range(h*w*4):
 #   print(i,*graph[i])
ans=10**32
ansl=BFS01(graph,toint(s[0],s[1],0))

for i in range(4):
    gi=toint(g[0],g[1],i)
    ans=min(ans,ansl[gi])
print(ans)
"""



"""
v=[-1,s[0],s[1]]
while v:
    dir,y,x=v.pop()
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<=h-1 and 0<=nx<=w-1:
            if grid[ny][nx]=="." and vis[i][ny][nx]==-1:
                if dir==-1:
"""



"""
import sys,heapq
from collections import deque

h,w=map(int,input().split())
s=list(map(lambda x:int(x)-1,input().split()))
g=list(map(lambda x:int(x)-1,input().split()))

grid=[input() for i in range(h)]
dy=[-1,1,0,0]
dx=[0,0,-1,1]

vis=[[[-1 for _ in range(w)] for _ in range(h)]for _ in range(4)]
for i in range(4):
    vis[i][s[0]][s[1]]=0
v=[]
heapq.heappush(v,(0,s[0],s[1],-1))

while v:
    dep,y,x,dir=heapq.heappop(v)
    #print(dep,y,x,dir)
    if [y,x]==g:
        print(dep)
        sys.exit()
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<=h-1 and 0<=nx<=w-1:
            if dir==-1:
                if grid[ny][nx]==".":
                    vis[i][ny][nx]=0
                    heapq.heappush(v,(0,ny,nx,i))
            else:
                if grid[ny][nx]=="." and vis[i][ny][nx]==-1:
                    if dir==i:
                        vis[i][ny][nx]=dep
                        heapq.heappush(v,(dep,ny,nx,i))
                    else:
                        vis[i][ny][nx]=dep+1
                        heapq.heappush(v,(dep+1,ny,nx,i))

while v:
    dep,y,x,dir=v.popleft()
    #print(dep,y,x,dir)
    if g==[y,x]:
        print(dep)
        sys.exit()
    for d in range(4):
        ny=y+dy[d]
        nx=x+dx[d]
        if 0<=ny<=h-1 and 0<=nx<=w-1:
            if grid[ny][nx]=="." :
                if dir==-1:
                    
                    vis[dir][ny][nx]==-1:
                    if dir==-1:
                        heapq.heappush(v,(dep,ny,nx,d))
                        vis[d][ny][nx]=dep
                    elif dir!=d:
                        heapq.heappush(v,(dep+1,ny,nx,d))
                        vis[ny][nx]=dep+1
                    else:
                        heapq.heappush(v,(dep,ny,nx,d))
                        vis[ny][nx]=dep

"""