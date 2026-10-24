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

x,y,a,b,c=mi()
def ceil(x,y):
    if x%y==0:
        return  x//y
    return x//y+1

def ycheck(a,b,c,x,y):
    w=ceil(a,y)
    x-=w 
    if x<=0:
        return
    if ychecksub(b,c,x,y):
        print("Yes")
        sys.exit()
    if xcehcksub(b,c,x,y):
        print("Yes")
        sys.exit()

def xcheck(a,b,c,x,y):
    h=ceil(a,x)
    y-=h
    if y<=0:
        return
    if ychecksub(b,c,x,y):
        print("Yes")
        sys.exit()
    if xcehcksub(b,c,x,y):
        print("Yes")
        sys.exit()

def ychecksub(a,b,x,y):
    w=ceil(a,y)
    x-=w
    if x<=0:
        return False
    if x*y>=b:
        return True
    
    return False
def xcehcksub(a,b,x,y):
    h=ceil(a,x)
    y-=h
    if y<=0:
        return False
    if x*y>=b:
        return True
    return False

ycheck(a,b,c,x,y)
ycheck(b,a,c,x,y)
ycheck(c,a,b,x,y)
xcheck(a,b,c,x,y)
xcheck(b,a,c,x,y)
xcheck(c,a,b,x,y)

print("No")