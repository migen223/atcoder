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

h,w=mi()

grid=[list(input()) for i in range(h)]

def check(l):
    for i in l:
        if i=="#":
            return False
    return True
def check2(l):
    ll=[]
    for i in range(len(l)):
        ll.append(l[i][0])
    return check(ll)
def check3(l):
    ll=[]
    for i in range(len(l)):
        ll.append(l[i][-1])
    return check(ll)


while True:
    l=[]
    f=0
    while check(grid[0]):
        grid.pop(0)
        f+=1
    while check(grid[-1]):
        grid.pop()
        f+=1
    while check2(grid):
        f+=1
        for i in range(len(grid)):
            grid[i].pop(0)
    while check3(grid):
        f+=1
        for i in range(len(grid)):
            grid[i].pop()
    if f==0:
        break

for i in range(len(grid)):
    print("".join(grid[i]))



"""
ans=[]
f=0
up=0
bo=h
l=0
r=w

f=0
for i in range(h):
    for j in range(w):
        if grid[i][j]=="#":
            f+=1
            up=i
            debug(i,j)
            break
    if f>1:
        break
f=0
for i in range(h-1,-1,-1):
    for j in range(w):
        if grid[i][j]=="#":
            f+=1
            bo=i
            debug(i,j)
            break
    if f>1:
        break
f=0
for i in range(w):
    for j in range(h):
        if grid[j][i]=="#":
            f+=1
            l=i
            debug(i,j)
            break
    if f>1:
        break
    
f=0
for i in range(w-1,-1,-1):
    for j in range(h):
        if grid[j][i]=="#":
            f+=1
            r=i
            debug(i,j)
            break
    if f>1:
        break

debug(up,bo,l,r)"""