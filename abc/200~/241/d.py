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

q=ii()
a=SortedList([])
for _ in range(q):
    que=li()
    if que[0]==1:
        x=que[1]
        a.add(x)
    elif que[0]==2:
        _,x,k=que
        ind=a.bisect_right(x)
        ans=ind-k
        #debug(ind)
        if 0<=ans<len(a):
            print(a[ans])
        else:
            print(-1)
    else:
        _,x,k=que
        ind=a.bisect_left(x)
        ans=ind+k-1
        if 0<=ans<len(a):
            print(a[ans])
        else:
            print(-1)