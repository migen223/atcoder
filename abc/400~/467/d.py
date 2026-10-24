import sys

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

t=ii()

def f(x1,y1,x2,y2):
    return (x2**2-x1**2+y2**2-y1**2)

for _ in range(t):
    px,py,qx,qy,rx,ry,sx,sy=mi()
    if (px-qx)*(ry-sy)!=(rx-sx)*(py-qy):
        print("Yes")
    else:
        #debug(f(px,py,qx,qy),f(rx,ry,sx,sy),px)

        if py==qy:
            if px+qx!=rx+sx:
                print("No")
            else:
                print("Yes")
        else:
            if (f(px,py,qx,qy)*(sy-ry))==(f(rx,ry,sx,sy)*(qy-py)):
                print("Yes")
            else:
                print("No")