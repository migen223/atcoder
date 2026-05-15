import sys
n=int(input())

grid=[list(input()) for i in range(n)]

for i in range(n-5):
    for j in range(n-5):
        utd=0
        dtu=0
        for k in range(6):
            if grid[i+k][j+k]==".":
                utd+=1
            if grid[i+5-k][j+k]==".":
                dtu+=1
        if utd<=2 or dtu<=2:
            print("Yes")
            sys.exit()

for i in range(n):
    for j in range(n-5):
        row=0
        column=0
        for k in range(6):
            if grid[i][j+k]==".":
                row+=1
            if grid[j+k][i]==".":
                column+=1
        if row<=2 or column<=2:
            print("Yes")
            sys.exit()

print("No")


"""
8
........
.......#
.#.##...
.......#
.......#
.......#
........
.......#

"""