
n=int(input())
ans=[]
for i in range(n):
    ans.append([1]*(i+1))
for i in range(2,n):
    for j in range(i-1):
        ans[i][1+j]=ans[i-1][j]+ans[i-1][j+1]
for i in range(n):
    print(*ans[i])
