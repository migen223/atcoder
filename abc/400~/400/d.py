import heapq
from collections import deque
#ダイクストラ法
#edgesは[[(node,weight)]]の形で表されるグラフ　
def dijkstra(edges, start):
    
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

def id(y,x):
    return x+w*y

h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]
A,B,C,D=map(lambda x:int(x)-1,input().split())
dy=[1,0,-1,0]
dx=[0,1,0,-1]
graph=[[] for i in range(h*w)]

for i in range(h):
    for j in range(w):
        for d in range(4):
            ny=i+dy[d]
            nx=j+dx[d]
            if 0<=ny <=h-1 and 0<=nx<=w-1:
                u,v=id(i,j),id(ny,nx)
                if grid[ny][nx]==".":
                    graph[u].append((v,0))
                    #graph[v].append((u,0))
                else:
                    graph[u].append((v,1))
                    #graph[v].append((u,1))
                nny=ny+dy[d]
                nnx=nx+dx[d]
                if 0<=nny <=h-1 and 0<=nnx<=w-1:
                    u,v=id(i,j),id(nny,nnx)
                    if grid[ny][nx]=="#" or grid[nny][nnx]=="#":
                        graph[u].append((v,1))
                        #graph[v].append((u,1))


#print(graph)
ansg=dijkstra(graph,id(A,B))
print(ansg[id(C,D)])

"""
visited=[[-1]*w for i in range(h)]
visit=deque([(A,B,0)])
f=0
while visit:
    y,x,depth=visit.popleft()
    if visited[y][x]!=-1:
        continue
    visited[y][x]=depth
    nvisit=[(y,x)]
    route=[(y,x)]
    while nvisit:
        y1,x1=nvisit.pop()
        for d in range(4):
            ny=y1+dy[d]
            nx=x1+dx[d]
            if 0<=ny<=h-1 and 0<=nx<=w-1:
                if grid[ny][nx]=="." and visited[ny][nx]==-1:
                    visited[ny][nx]=depth
                    nvisit.append((ny,nx))
                    route.append((ny,nx))
        
    change=[]
    #print(route)
    for y1,x1 in route:
        for d in range(4):
            for i in range(1,3):
                ny=y1+dy[d]*i
                nx=x1+dx[d]*i
                if 0<=ny<=h-1 and 0<=nx<=w-1:
                    if visited[ny][nx]==-1:
                        #visited[ny][nx]=depth+1
                        change.append((ny,nx))
                        visit.append((ny,nx,depth+1))
    #print(change)
    for ny,nx in change:
        grid[ny][nx]="."
    if f<30:
        for i in range(h):
            for j in range(w):
                print(visited[i][j],end="")
            print()
        for i in range(h):
            for j in range(w):
                print(grid[i][j],end="")
            print()
        print("depth",depth,y,x)
    f+=1
    #print(visit)



print(visited[C][D])
            
4 7
.#.#.##.
.#.#.##.
.#....##
.#.#.##.
1 1 4 7

9 20
####################
##...##....###...###
#.....#.....#.....##
#..#..#..#..#..#..##
#..#..#....##..#####
#.....#.....#..#####
#.....#..#..#..#..##
#..#..#.....#.....##
#..#..#....###...###
3 3 9 17
"""