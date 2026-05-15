
n=int(input())
x,y=map(int,input().split())

box=[]
for i in range(n):
    a,b=map(int,input().split())
    box.append((a,b))

now=[[1000 for i in range(x+1)] for i in range(y+1)]

now[min(y,box[0][1])][min(x,box[0][0])]=1

"""
for i in range(n):
    print()
    print(dp[i])
"""
    
for i in range(n-1):
    nx=min(box[i+1][0],x)
    ny=min(box[i+1][1],y)
    next=[[now[j][i] for i in range(x+1)] for j in range(y+1)]
    next[ny][nx]=1
    for j in range(1,y+1):
        for k in range(1,x+1):
            if now[j][k]!=1000:
                next[min(j+ny,y)][min(k+nx,x)]=min(next[min(j+ny,y)][min(k+nx,x)],now[j][k]+1)
                """
                print("ny,nx",j+ny,y,k+nx,x,j,k,ny,nx)
    for i in range(y+1):
        print(*now[i])
    print("next")
    for i in range(y+1):
        print(*next[i])
    print("now")
    """

    now=[[next[j][i] for i in range(x+1)] for j in range(y+1)]


ans=-1
if now[-1][-1]==1000:
    print(-1)
else:
    print(now[-1][-1])


