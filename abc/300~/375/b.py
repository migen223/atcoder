from math import sqrt

n=int(input())
x,y=0,0
ans=0
for i in range(n):
    nx,ny=map(int,input().split())
    ans+=sqrt((x-nx)**2+(y-ny)**2)
    x=nx
    y=ny
ans+=sqrt((x-0)**2+(y-0)**2)
print(ans)