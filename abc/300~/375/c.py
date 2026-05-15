
n=int(input())
grid=[list(input()) for i in range(n)]

ans=[["."]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        num=min(i+1,j+1,n-j,n-i)%4
        if num==0:
            ans[i][j]=grid[i][j]
            #print(i,j,i,j)
        elif num==1:
            #ans[i][j]=grid[j][n-i-1]
            ans[j][n-i-1]=grid[i][j]
            #print(i,j,j,n-i-1)
        elif num==2:
            #ans[i][j]=grid[n-i-1][n-j-1]
            ans[n-i-1][n-j-1]=grid[i][j]
            #print(i,j,n-i-1,n-j-1)
        elif num==3:
            #ans[i][j]=grid[n-j-1][i]
            ans[n-j-1][i]=grid[i][j]
            #print(i,j,n-j-1,i)
#print()
for i in range(n):
    print("".join(ans[i]))