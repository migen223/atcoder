n=int(input())
grid=[]
def makegrid(n):
    if n==0:
        return [["#"]]
    elif n==1:
        return [["#","#","#"],["#",".","#"],["#","#","#"]]
    else:
        grid=[[] for i in range(3**n)]
        for i in range(3**n):
            for j in range(3**n):
                grid[i].append(".")
        ngrid=makegrid(n-1)

        for i in range(3**(n-1)):
            for j in range(3**(n-1)):
                for k in range(3):
                    grid[i][3**(n-1)*k+j]=ngrid[i][j]
        #print(grid)
        #print()
        for i in range(3**(n-1)):
            for j in range(3**(n-1)):
                grid[3**(n-1)+i][j]=ngrid[i][j]
        #print(grid)
        #print()
        for i in range(3**(n-1)):
            for j in range(3**(n-1)):
                grid[3**(n-1)+i][3**(n-1)*2+j]=ngrid[i][j]
        #print(grid)
        #print()
        for i in range(3**(n-1)):
            for j in range(3**(n-1)):
                for k in range(3):
                    grid[3**(n-1)*2+i][3**(n-1)*k+j]=ngrid[i][j]
        #print(grid)
        #print()
        return grid

        


    
if n==0:
    print("#")
else:
    grid=makegrid(n)
    for i in range(3**n):
        print("".join(grid[i]))