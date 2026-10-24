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

n,m=mi()

que=[]
for i in range(m):
    r,c=mi()
    que.append((r,c))

line=set()
row=set()
ans=0
for i in range(m-1,-1,-1):
    
    r,c=que[i]
    #debug(r,c)
    if r not in line and c not in row:
        ans+=1
    line.add(r)
    row.add(c)
    #print(line,row)
print(ans)

