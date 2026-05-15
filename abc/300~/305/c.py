import sys
h,w=map(int,input().split())
grid=[list(input()) for _ in range(h)]


rec=[]
for i in range(h):
    f=0
    f1=0
    now=[]
    for j in range(w):
        if grid[i][j]=="#" and f==0:
            f+=1
            now.append(j)
        elif grid[i][j]=="." and f==1:
            now.append(j-1)
            f1+=1
            break
    if f1==0 and f==1:
        now.append(w-1)
    rec.append(now)

#print(rec)
height=0
width=0
start=[h,w]
for i in range(len(rec)):
    if len(rec[i])==2:
        height+=1
        width=max(width,rec[i][1]-rec[i][0]+1)
        start[1]=min(start[1],rec[i][0])
        start[0]=min(start[0],i)
#print(start,height,width)
for i in range(height):
    for j in range(width):
        if grid[start[0]+i][start[1]+j]==".":
            print(start[0]+i+1,start[1]+j+1)
            sys.exit()




