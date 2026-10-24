import sys

def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
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

h,w,q=mi()

ans=[[(-1,"A") for _ in range(w)] for _ in range(h)]
for i in range(q):
    que=input().split()
    r=int(que[0])-1
    c=int(que[1])-1
    x=que[2]
    ans[r][c]=max((i,x),ans[r][c])


for i in range(h-1,-1,-1):
    ma=ans[i][-1]
    for j in range(w-1,0,-1):
        ans[i][j-1]=max(ma,ans[i][j-1])
        ma=max(ma,ans[i][j-1])
        #print(ma,ans[i][j-1],i,j)


for  i in range(w-1 ,-1,-1):
    ma=ans[-1][i]
    for j in range(h-1,0,-1):
        ans[j-1][i]=max(ma,ans[j-1][i])
        ma=max(ma,ans[j-1][i])

for i in range(h):
    for j in range(w):
        print(ans[i][j][1],end="")
    print()

