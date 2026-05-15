n=int(input())
grid=[list(input()) for i in range(n)]
row=[0]*n
column=[0]*n
ans=0
for i in range(n):
    for j in range(n):
        if grid[i][j]=="o":
            row[i]+=1
        if grid[j][i]=="o":
            column[i]+=1
for i in range(n):
    for j in range(n):
        if grid[i][j]=="o":
            ans+=(row[i]-1)*(column[j]-1)
print(ans)