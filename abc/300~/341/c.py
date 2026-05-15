h,w,n=map(int,input().split())
t=list(input())
grid=[]
for i in range(h):
    grid.append(list(input()))
def step(now,t):
    if t=="L":
        return [now[0],now[1]-1]
    elif t=="R":
        return [now[0],now[1]+1]
    elif t=="U":
        return [now[0]-1,now[1]]
    else:
        return [now[0]+1,now[1]]

ans=0
for i in range(1,h-1):
    for j in range(1,w-1):
        f=0
        if grid[i][j]==".":
            now=[i,j]
            for k in range(n):
                now=step(now,t[k])
                if grid[now[0]][now[1]]=="#":
                    f+=1
                    break
            if f==0:
                ans+=1

print(ans)