
m,a,b=map(int,input().split())

grid=[[-1 for i in range(m)] for i in range(m)]

for i in range(m):
    for j in range(m):
        grid[i][j]=(b*i+a*j)%m
    
vis=[[-1 for i in range(m)] for i in range(m)]
for i in range(m):
    vis[i][0]=0
    vis[0][i]=0
for i in range(m):
    for j in range(m):
        if grid[i][j]==0:
            vis[i][j]=0

for i in range(m):
    for j in range(m):
        if vis[i][j]==-1:
            f=0
            v=[(i,j)]
            vis[i][j]=-2
            while v:
                y,x=v[-1]
                if grid[y][x]==0:
                    f=1
                ne=(x,grid[y][x])
                if vis[ne[0]][ne[1]]==-1:
                    v.append(ne)
                    vis[ne[0]][ne[1]]=-2
                elif vis[ne[0]][ne[1]]==0:
                    f=1
                    break
                elif vis[ne[0]][ne[1]]==-2:
                    break
            if f==1:
                for y,x in v:
                    vis[y][x]=0
                
                    """
                print()
                for i in range(m):
                    print(*vis[i])"""
            #print()
            #print(f,v,(v[0][0]+v[0][1])%m)

"""
for i in range(m):
    print(*grid[i])
print()
for i in range(m):
    print(*vis[i])
#"""
ans=0
for i in range(m):
    for j in range(m):
        if vis[i][j]!=0:
            ans+=1

print(ans)
                    