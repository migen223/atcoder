import sys

from bisect import bisect_left
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


q=ii()
s=input()
t=input()
n=len(s)
m=len(t)
part=[]
for i in range(n-m+1):
    f=0
    for j in range(m):
        if s[i+j]!=t[j]:
            f+=1
            break
    if f==0:
        part.append(i+1)


for _ in range(q):
    l,r=mi()
    ind=bisect_left(part,l)
    #debug(l,ind)
    if ind==len(part):
        print("No")
    else:
        if r>=part[ind]+m-1:
            print("Yes")
        else:
            print("No")