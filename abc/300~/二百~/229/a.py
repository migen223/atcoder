
grid=[list(input()) for i in range(2)]

if grid[0][0]==grid[1][1]=="." or grid[1][0]==grid[0][1]==".":
    print("No")
else:
    print("Yes")
