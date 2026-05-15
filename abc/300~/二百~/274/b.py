h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]
ans=[]
for i in range(w):
    count=0
    for j in range(h):

        if grid[j][i]=="#":
            count+=1
    ans.append(count)
print(*ans)