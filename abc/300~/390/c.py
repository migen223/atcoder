import sys
h,w=map(int,input().split())
grid=[]
for i in range(h):
    grid.append(list(input()))
top=w+1
bottom=-1
left=w+1
right=-1

for i in range(h):
    for j in range(w):
        if grid[i][j]=="#":
            top=min(top,i)
            bottom=max(bottom,i)
            left=min(left,j)
            right=max(right,j)
for i in range(top,bottom+1):
    for j in range(left,right+1):
        if grid[i][j]==".":
            print("No")
            sys.exit()
print("Yes")