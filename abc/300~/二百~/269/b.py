grid=[list(input()) for i in range(10)]

xmin=10000
xmax=0
ymin=1000
ymax=0

for i in range(10):
    for j in range(10):
        if grid[i][j]=="#":
            xmin=min(xmin,j+1)
            xmax=max(xmax,j+1)
            ymin=min(ymin,i+1)
            ymax=max(ymax,i+1)
print(ymin,ymax)
print(xmin,xmax)