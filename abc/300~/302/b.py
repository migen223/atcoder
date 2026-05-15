import sys
h,w=map(int,input().split())

grid=[list(input()) for i in range(h)]

ans=[]
for i in range(h):
    for j in range(w-4):
        #print(grid[i][j],grid[i][j+1],grid[i][j+2],grid[i][j+3],grid[i][j+4])
        if grid[i][j]=="s" and grid[i][j+1]=="n" and grid[i][j+2]=="u" and grid[i][j+3]=="k" and grid[i][j+4]=="e":
            for k in range(5):
                print(i+1,j+k+1)
            sys.exit()
        if grid[i][j]=="e" and grid[i][j+1]=="k" and grid[i][j+2]=="u" and grid[i][j+3]=="n" and grid[i][j+4]=="s":
            for k in range(5):
                print(i+1,j+5-k)
            sys.exit()
for j in range(w):
    for i in range(h-4):
        #(grid[i][j],grid[i+1][j],grid[i+2][j],grid[i+3][j],grid[i+4][j])
        if grid[i][j]=="s" and grid[i+1][j]=="n" and grid[i+2][j]=="u" and grid[i+3][j]=="k" and grid[i+4][j]=="e":
            for k in range(5):
                print(i+1+k,j+1)
            sys.exit()
        if grid[i][j]=="e" and grid[i+1][j]=="k" and grid[i+2][j]=="u" and grid[i+3][j]=="n" and grid[i+4][j]=="s":
            for k in range(5):
                print(i+5-k,j+1)
            sys.exit()
for i in range(h-4):
    for j in range(w-4):
        #print(grid[i][j],grid[i+1][j+1],grid[i+2][j+2],grid[i+3][j+3],grid[i+4][j+4])
        if grid[i][j]=="s" and grid[i+1][j+1]=="n" and grid[i+2][j+2]=="u" and grid[i+3][j+3]=="k" and grid[i+4][j+4]=="e":
            for k in range(5):
                print(i+1+k,j+1+k)
            sys.exit()
        if grid[i][j]=="e" and grid[i+1][j+1]=="k" and grid[i+2][j+2]=="u" and grid[i+3][j+3]=="n" and grid[i+4][j+4]=="s":
            for k in range(5):
                print(i+5-k,j+5-k)
            sys.exit()
        if grid[i][j+4]=="s" and grid[i+1][j+3]=="n" and grid[i+2][j+2]=="u" and grid[i+3][j+1]=="k" and grid[i+4][j]=="e":
            for k in range(5):
                print(i+1+k,j+5-k)
            sys.exit()
        if grid[i][j+4]=="e" and grid[i+1][j+3]=="k" and grid[i+2][j+2]=="u" and grid[i+3][j+1]=="n" and grid[i+4][j]=="s":
            for k in range(5):
                print(i+5-k,j+1+k)
            sys.exit()
        


