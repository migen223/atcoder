import sys
from collections import defaultdict
from bisect import bisect_left,bisect_right
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
a=li()

que=[]
orig=[]
dic=defaultdict(list)
ansd={}
for i in range(q):
    r,x=mi()
    dic[r].append(x)
    orig.append((r,x))

lis=[inf]*n
ans=[0]*q

for i in range(n):
    ind1=bisect_left(lis,a[i])
    lis[ind1]=a[i]
    if i+1 in dic:
        for x in dic[i+1]:
            ind2=bisect_right(lis,x)
            ansd[(i+1,x)]=ind2

for r,x in orig:
    print(ansd[(r,x)])
