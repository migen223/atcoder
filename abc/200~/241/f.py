import sys
from bisect import bisect_left
from collections import deque
def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]

h,w,n=mi()
sy,sx=map(lambda x:int(x)-1, input().split())
gy,gx=map(lambda x:int(x)-1, input().split())

line={}
row={}

for i in range(n):
    y,x=map(lambda x:int(x)-1, input().split())
    if x not in line:
        line[x]=[y]
    else:
        line[x].append(y)
    if y not in row:
        row[y]=[x]
    else:
        row[y].append(x)
for li in line:
    line[li].sort()
for ri in row:
    row[ri].sort()

v=deque([(sy,sx,0)])
vis=set([(sy,sx)])

while v:
    y,x,d=v.popleft()
    if (y,x)==(gy,gx):
        print(d)
        sys.exit()
    #print(y,x,d)
    if y in row:
        indx=bisect_left(row[y],x)
        right=indx
        left=indx-1
        if 0<=right<len(row[y]) and (y,row[y][right]-1) not in vis:
            vis.add((y,row[y][right]-1))
            v.append((y,row[y][right]-1,d+1))
        if 0<=left<len(row[y]) and (y,row[y][left]+1) not in vis:
            vis.add((y,row[y][left]+1))
            v.append((y,row[y][left]+1,d+1))
    if x in line:
        indy=bisect_left(line[x],y)
        right=indy
        left=indy-1
        if 0<=right<len(line[x]) and (line[x][right]-1,x) not in vis:
            vis.add((line[x][right]-1,x))
            v.append((line[x][right]-1,x,d+1))
        if 0<=left<len(line[x]) and (line[x][left]+1,x) not in vis:
            vis.add((line[x][left]+1,x))
            v.append((line[x][left]+1,x,d+1))
 
print(-1)