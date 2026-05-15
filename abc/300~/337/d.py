
h,w,k=map(int,input().split())
grid=[list(input()) for i in range(h)]


xhori=[[0]*w for i in range(h)]
xvert=[[0]*w for i in range(h)]
ohori=[[0]*w for i in range(h)]
overt=[[0]*w for i in range(h)]

for i in range(h):
    for j in range(w):
        if grid[i][j]=="x":
            if j==0:
                xhori[i][j]=1
            else:
                xhori[i][j]=xhori[i][j-1]+1
        else:
            if j!=0:
                xhori[i][j]=xhori[i][j-1]
        if grid[i][j]=="o":
            if j==0:
                ohori[i][j]=1
            else:
                ohori[i][j]=ohori[i][j-1]+1
        else:
            if j!=0:
                ohori[i][j]=ohori[i][j-1]
        
for j in range(w):
    for i in range(h):
        if grid[i][j]=="x":
            if i==0:
                xvert[i][j]=1
            else:
                xvert[i][j]=xvert[i-1][j]+1
        else:
            if i!=0:
                xvert[i][j]=xvert[i-1][j]
        if grid[i][j]=="o":
            if i==0:
                overt[i][j]=1
            else:
                overt[i][j]=overt[i-1][j]+1
        else:
            if i!=0:
                overt[i][j]=overt[i-1][j]


ans=10**32
for i in range(h):
    for j in range(w):
        if grid[i][j]=="o" or grid[i][j]==".":
            if 0<=j+k-1<=w-1:
                if xhori[i][j]==xhori[i][j+k-1] and grid[i][j+k-1]!="x":
                    now=ohori[i][j+k-1]
                    if j!=0:
                        now-=ohori[i][j-1]
                    ans=min(ans,k-now)
            if 0<=i+k-1<=h-1:
                if xvert[i][j]==xvert[i+k-1][j] and grid[i+k-1][j]!="x":
                    now=overt[i+k-1][j]
                    if i!=0:
                        now-=overt[i-1][j]
                    ans=min(ans,k-now)

if ans==10**32:
    print(-1)
else:
    print(ans)
