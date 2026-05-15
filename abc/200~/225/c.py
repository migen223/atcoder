import sys

n,m=map(int,input().split())
grid=[list(map(int,input().split())) for i in range(n)]

if n!=1:
    for i in range(n-1):
        for j in range(m):
            
            if grid[i][j]%7==0:
                if j!=m-1:
                    print("No")
                    sys.exit()
            if j!=0:
                if grid[i][j-1]+1!=grid[i][j]:
                    print("No")
                    sys.exit()
            
            """
            if j!=0:
                if grid[i][j-1]%7+1!=grid[i][j]%7:
                    print("No")
                    sys.exit()
            """
            if grid[i][j]+7!=grid[i+1][j]:
                print("No")
                sys.exit()
    print("Yes")
else:
    #print(grid)
    for j in range(m):
            
        if grid[0][j]%7==0:
            if j!=m-1:
                print("No")
                sys.exit()
        if j!=0:
            if grid[0][j-1]+1!=grid[0][j]:
                print("No")
                sys.exit()
    print("Yes")