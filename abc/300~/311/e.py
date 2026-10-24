
h,w,n=map(int,input().split())
grid=[[0 for _ in range(w+1)] for _ in range(h+1)]
r=[[0 for _ in range(w+1)] for _ in range(h+1)]
for _ in range(n):
    a,b=map(int,input().split())
    grid[a][b]+=1
    r[a][b]+=1


for i in range(h+1):
    for j in range(w):
        r[i][j+1]+=r[i][j]

for i in range(w+1):
    for j in range(h):
        r[j+1][i]+=r[j][i]

def check(d,sx,sy):
    nx,ny=sx+d,sy+d
    if 1<=nx<=w and 1<=ny<=h:
        num=r[ny][nx]-r[sy-1][nx]-r[ny][sx-1]+r[sy-1][sx-1]
        #print(num,d,sx,sy,"obaud")
        if num==0:
            return True
        return False
    return False
        
"""
for i in range(h+1):
    print(*r[i])
print()
for i in range(h+1):
    print(*grid[i])
"""
ans=0
for i in range(1,h+1):
    for j in range(1,w+1):
        if grid[i][j]==1:
            continue
        L=0
        R=min(h,w)+1
        while R-L>1:
            m=(L+R)//2
            #print("LR",L,R)
            if check(m,j,i):
                L=m
            else:
                R=m
        ans+=L+1
        #print("ans,i,j",ans,i,j,L)

print(ans)




"""
5 4 3
1 4
3 3 
4 1


"""