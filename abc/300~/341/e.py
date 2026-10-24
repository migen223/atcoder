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

n,q=mi()
s=input()
sl=SortedList([])
for i in range(n-1):
    if s[i]!=s[i+1]:
        sl.add(i+1)



for  _ in range(q):
    que=li()
    if que[0]==1:
        _,l,r=que
        if l!=1:
            if l-1 in sl:
                sl.discard(l-1)
            else:
                sl.add(l-1)
        if r!=n:
            if r in sl:
                sl.discard(r)
            else:
                sl.add(r)

    else:
        _,l,r=que
        if l==r:
            print("Yes")
            continue
        indl=sl.bisect_left(l)
        indr=sl.bisect_left(r)
        #print(indl,indr,r-l)
        if indr-indl==r-l:
            print("Yes")
        else:
            print("No")


