

n=int(input())
grid=[list(input()) for _ in range(n)]

dy=[-1,-1,-1,1,1,1,0,0]
dx=[-1,0,1,-1,0,1,1,-1]

ans=0
for i in range(n):
    for j in range(n):
        
        for k in range(8):
            now=[]
            for l in range(n):
                now.append(grid[(i+dy[k]*l)%n][(j+dx[k]*l)%n])
            ans=max(ans,int("".join(now)))

print(ans)