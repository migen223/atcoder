import sys
from collections import defaultdict
from bisect import bisect_left
def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mi = lambda: map(int, input().split())
mmi= lambda: map(lambda x:int (x)-1, input().split())
li = lambda: list(mi())
inf = 2 ** 61 - 1
mod = 998244353
#mod=10**9+7
dy=[-1,1,0,0]
dx=[0,0,-1,1]
#dy=[-1,-1,-1,1,1,1,0,0]
#dx=[-1,0,1,-1,0,1,-1,1]
dir={"L":2,"R":3,"U":0,"D":1}

h,w,sy,sx=mi()
sy-=1
sx-=1

line=defaultdict(list)
row=defaultdict(list)
n=ii()
for _ in range(n):
    r,c=mmi()
    line[c].append(r)
    row[r].append(c)
#print(line)
#print(row)

for i in line:
    line[i].sort()
for i in row:
    row[i].sort()

q=ii()
for _ in range(q):
    d,l=input().split()
    l=int(l)
    if d=="D":
        if sx in line :
            ind=bisect_left(line[sx],sy)
            
            if ind!=len(line[sx]):
                sy=min(sy+l,line[sx][ind]-1)
            else:
                sy=min(h-1,sy+l)
            #debug(line[sx],ind,sy)
        else:
            sy=min(h-1,sy+l)
    elif d=="U":
        if sx in line :
            ind=bisect_left(line[sx],sy)
            if ind!=0:
                sy=max(sy-l,line[sx][ind-1]+1)
            else:
                sy=max(0,sy-l)
        else:
            sy=max(0,sy-l)
    elif d=="R":
        if sy in row :
            ind=bisect_left(row[sy],sx)
            if ind!=len(row[sy]):
                sx=min(sx+l,row[sy][ind]-1)
            else:
                sx=min(w-1,sx+l)
        else:
            sx=min(w-1,sx+l)
    elif d=="L":
        if sy in row :
            ind=bisect_left(row[sy],sx)
            if ind!=0:
                sx=max(sx-l,row[sy][ind-1]+1)
            else:
                sx=max(0,sx-l)
        else:
            sx=max(0,sx-l)

    print(sy+1,sx+1)
    #debug(sy+1,sx+1)
