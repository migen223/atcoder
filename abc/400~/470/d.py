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

n,q=mi()
p=li()
d1={i:p[i-1] for i in range(1,1+n)}
d2={p[i-1]:i for i in range(1,1+n)}
d=[d1,d2]
now=0


for _ in range(q):
    que=li()
    if que[0]==1:
        _,x,y=que
        o1,o2=d[now%2][x],d[now%2][y]
        d[(now+1)%2][o1],d[(now+1)%2][o2]=d[(now+1)%2][o2],d[(now+1)%2][o1]
        d[now%2][x],d[now%2][y]=o2,o1
    else:
        now+=1

for i in range(1,1+n):
    print(d[now%2][i],end=" ")
print()