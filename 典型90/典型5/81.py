
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

n,k=mi()

x=[]
y=[]

for _ in range(n):
    a,b=mi()
    x.append(a)
    y.append(b)

w=max(x)+1
h=max(y)+1
grid=[[0 for _ in range(w)] for _ in range(h)]
for i in range(n):
    ai,bi=x[i],y[i]
    grid[bi][ai]+=1


for i in range(w):
    for j in range(h-1):
        grid[j+1][i]+=grid[j][i]

for i in range(h):
    for j in range(w-1):
        grid[i][j+1]+=grid[i][j]

ans=1
for i in range(1,w):
    for j in range(1,h):
        #debug(j,i,j+k,i+k)
        res=grid[min(h-1,j+k)][min(w-1,i+k)]-grid[min(h-1,j+k)][i-1]-grid[j-1][min(w-1,i+k)]+grid[j-1][i-1]
        
        ans=max(ans,res)

print(ans)

"""
n,k=mi()

x=[]
y=[]

for _ in range(n):
    a,b=mi()
    x.append(a)
    y.append(b)

w=max(x)+1
h=max(y)+1
r1=[[0 for _ in range(w)] for _ in range(h+1)]
r2=[[0 for _ in range(w)] for _ in range(h+1)]
for i in range(n):
    ai,bi=x[i],y[i]
    r1[bi][ai]+=1
    r2[bi][ai]+=1


for i in range(w):
    for j in range(h-1):
        r1[j+1][i]+=r1[j][i]
        r2[h-j-2][i]+=r2[h-j-1][i]

for i in range(h):
    for j in range(w-1):
        r1[i][j+1]+=r1[i][j]
        r2[i][j+1]+=r2[i][j]

#for i in range(h):
  #  print(*r2[i])


ans=1
for i in range(n):
    xi,yi=x[i],y[i]
    #debug(min(h,yi+k))
    res=r1[min(h-1,yi+k)][min(w-1,xi+k)]-r1[min(h-1,yi+k)][xi-1]-r1[yi-1][min(w-1,xi+k)]+r1[yi-1][xi-1]
    ans=max(ans,res)

for i in range(n):
    xi,yi=x[i],y[i]
    res=r2[max(0,yi-k)][min(w-1,xi+k)]-r2[max(0,yi-k)][xi-1]-r2[yi-1][min(w-1,xi+k)]+r2[yi+1][xi-1]

print(ans)
    """