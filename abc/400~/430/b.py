
n,m=map(int,input().split())

grid=[list(input()) for i in range(n)]

se=set()

for i in range(n-m+1):
    for j in range(n-m+1):
        subgrid=[[] for i in range(m)]
        for k in range(m):
            for l in range(m):
                subgrid[k].append(grid[i+k][j+l])
        for k in range(m):
            subgrid[k]=tuple(subgrid[k])
        subgrid=tuple(subgrid)
        se.add(subgrid)
#print(se)
print(len(se))
        

