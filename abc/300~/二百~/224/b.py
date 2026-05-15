import sys
h,w=map(int,input().split())
grid=[list(map(int,input().split())) for i in range(h)]

for i in range(h-1):
    for j in range(w-1):
        if grid[i][j]+grid[i+1][j+1]>grid[i+1][j]+grid[i][j+1]:
            print("No")
            sys.exit()

print("Yes")
