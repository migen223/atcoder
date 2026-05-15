

"""
n=int(input())
grid=[[0 for _ in range(8)] for _ in range(8)]
for i in range(n):
    lx,ly,rx,ry=map(int,input().split())
    grid[ly][lx]+=1
    grid[ly][rx+1]-=1
    grid[ry+1][lx]-=1
    grid[ry+1][rx+1]+=1

for i in range(7):
    for j in range(1,7):
        grid[i][j]+=grid[i][j-1]

for i in range(7):
    for j in range(1,7):
        grid[j][i]+=grid[j-1][i]
print(grid)
ans=[0]*(n+1)

for i in range(7):
    for j in range(7):
        l=[grid[i][j],grid[i+1][j],grid[i][j+1],grid[i+1][j+1]]
        area=min(l)
        ans[area]+=1

for i in range(1,n+1):
    print(ans[i])

"""
n=int(input())
grid=[[0 for _ in range(1002)] for _ in range(1002)]
for i in range(n):
    lx,ly,rx,ry=map(int,input().split())
    rx-=1
    ry-=1
    grid[ly][lx]+=1
    grid[ly][rx+1]-=1
    grid[ry+1][lx]-=1
    grid[ry+1][rx+1]+=1
    

for i in range(1001):
    for j in range(1,1001):
        grid[i][j]+=grid[i][j-1]

for i in range(1001):
    for j in range(1,1001):
        grid[j][i]+=grid[j-1][i]

ans=[0]*(n+1)

for i in range(1001):
    for j in range(1001):
        if grid[i][j]>=1:
            ans[grid[i][j]]+=1


for i in range(1,n+1):
    print(ans[i])
#"""