
n=int(input())


ans=2000**2
grid=[[0]*2000 for i in range(2000)]
grid2=[[0]*2000 for i in range(2000)]
for i in range(1,n+1):
    u,d,l,r=map(int,input().split())
    u-=1
    d-=1
    l-=1
    r-=1
    grid[u][l]+=1
    if d!=1999:
        grid[d+1][l]-=1
    if r!=1999:
        grid[u][r+1]-=1
    if d!=1999 and r!=1999:
        grid[d+1][r+1]+=1
    grid2[u][l]+=i
    if d!=1999:
        grid2[d+1][l]-=i
    if r!=1999:
        grid2[u][r+1]-=i
    if d!=1999 and r!=1999:
        grid2[d+1][r+1]+=i
"""
for i in range(6):
    for j in range(6):
        print(grid[i][j],end=" ")
    print()
print()
"""

minus=0
for i in range(2000):
    for j in range(2000-1):
        grid[i][j+1]=grid[i][j]+grid[i][j+1]
        grid2[i][j+1]=grid2[i][j]+grid2[i][j+1]
for i in range(2000):
    for j in range(1999):
        grid[j+1][i]=grid[j][i]+grid[j+1][i]
        grid2[j+1][i]=grid2[j][i]+grid2[j+1][i]

"""
for i in range(7):
    for j in range(7):
        print(grid[i][j],end=" ")
    print()
print()
for i in range(6):
    for j in range(6):
        print(grid2[i][j],end=" ")
    print()
    """

ansl=[0]*n
for i in range(2000):
    for j in range(2000):
        if grid[i][j]==1:
            minus+=1
            ansl[grid2[i][j]-1]+=1
        elif grid[i][j]>1:
            minus+=1

for i in range(n):
    print(ans-(minus-ansl[i]))

    


