import sys


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

grid=[input() for _ in range(2)]

for i in range(2):
    for j in range(2):
        if grid[i][j]=="A":
            for d in range(4):
                ny=i+dy[d]
                nx=j+dx[d]
                if 0<=ny<=1 and 0<=nx<=1:
                    if grid[ny][nx]=="D":
                        print("Yes")
                        exit()

print("No")


