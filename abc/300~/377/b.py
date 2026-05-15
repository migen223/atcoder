grid=[]
for i in range(8):
    a=list(input())
    grid.append(a)
ans=0
gridc=[[".",".",".",".",".",".",".","."] for i in range(8)]
add=["#","#","#","#","#","#","#","#"]
for i in range(8):
    if "#" in grid[i]:
        gridc[i]=add
for i in range(8):
    l=[]
    for j in range(8):
        l.append(grid[j][i])
    #print(l)
    if "#" in l:
        for j in range(8):
            gridc[j][i]="#"
#for i in range(8):
    #print(gridc[i])
for i in range(8):
    for j in range(8):
        if gridc[i][j]==".":
            ans+=1
print(ans)
