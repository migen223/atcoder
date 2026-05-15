import sys

n=int(input())
grid=[list(input()) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i!=j:
            if grid[i][j]=="W" and grid[j][i]!="L":
                print("incorrect")
                sys.exit()
            if grid[i][j]=="D" and grid[j][i]!="D":
                print("incorrect")
                sys.exit()
            if grid[i][j]=="L" and grid[j][i]!="W":
                print("incorrect")
                sys.exit()
print("correct")
