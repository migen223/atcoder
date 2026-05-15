
n=int(input())

ans=[[0]*n for i in range(n)]

ans[0][(n-1)//2]=1
r,c,k=(0,(n-1)//2,1)
for i in range(n**2-1):
    if ans[(r-1)%n][(c+1)%n]==0:
        ans[(r-1)%n][(c+1)%n]=k+1
        r=(r-1)%n
        c=(c+1)%n
        k+=1
    else:
        ans[(r+1)%n][c]=k+1
        r=(r+1)%n
        k+=1

for i in range(n):
    print(*ans[i])