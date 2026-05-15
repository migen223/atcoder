
h,w,n=map(int,input().split())
grid=[list(map(int,input().split())) for i in range(h)]

ans=0
se=set()
for i in range(n):
    b=int(input())
    se.add(b)

for i in range(h):
    count=0
    for j in range(w):
        if grid[i][j] in se:
            count+=1
    ans=max(ans,count)
print(ans)
