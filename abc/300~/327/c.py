import sys
grid=[list(map(int,input().split())) for i in range(9)]

for i in range(9):
    ser=set()
    sec=set()
    for j in range(9):
        if grid[i][j] in ser:
            print("No")
            sys.exit()
        else:
            ser.add(grid[i][j])
    for k in range(9):
        if grid[k][i] in sec:
            print("No")
            sys.exit()
        else:
            sec.add(grid[k][i])

for i in range(3):
    for j in range(3):
        se=set()
        for k in range(3):
            for l in range(3):
                if grid[k+i*3][l+j*3] in se:
                    print("No")
                    sys.exit()
                else:
                    se.add(grid[k+i*3][l+j*3])
print("Yes")