import sys
from sortedcontainers import SortedList
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

n,m=mi()

a=li()
b=li()
c=li()
d=li()
box=SortedList([])
event=[]
for i in range(n):
    event.append((-a[i],1,b[i]))
for i in range(m):
    event.append((-c[i],0,d[i]))
event.sort()

for i in range(n+m):
    y,obj,x=event[i]
    y*=-1
    if obj==0:
        box.add(x)
    else:
        if box:
            ind=box.bisect_left(x)
            if ind!=len(box):
                box.pop(ind)
            else:
                print("No")
                sys.exit()
        else:
            print("No")
            sys.exit()

print("Yes")