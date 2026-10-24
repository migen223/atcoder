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

h,w,m=mi()
line=set()
row=set()
que=[]
xl=[]
for _ in range(m):
    t,a,x=mi()
    que.append((t,a,x))
    xl.append(x)
color=[0]*(max(xl)+1)
color[0]+=h*w

for i in range(m):
    t,a,x=que[-1-i]
    if t==1:
        if a not in row:
            row.add(a)
            color[x]+=w-len(line)
            color[0]-=w-len(line)
    else:
        if a not in line:
            line.add(a)
            color[x]+=h-len(row)
            color[0]-=h-len(row)

ans=[]

for i in range(max(xl)+1):
    if color[i]>0:
        ans.append((i,color[i]))

print(len(ans))
for ai in ans:
    print(*ai)

