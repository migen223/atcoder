
import sys
from collections import deque
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

dic={}
change=[]
for i in range(n):
    a,d,b=mi()
    if d==1:
        if b not in dic:
            dic[b]=1
        else:
            dic[b]+=1
    else:
        if a not in dic:
            dic[a]=1
        else:
            dic[a]+=1
        change.append((d,a,b))
change.sort()
change=deque(change)
#print(dic)
for i in range(1,1+m):
    
    while change and change[0][0]==i:
        d,a,b=change.popleft()
        dic[a]-=1
        if dic[a]==0:
            dic.pop(a)
        if b not in dic:
            dic[b]=1
        else:
            dic[b]+=1
    #print(dic)
    print(len(dic))

    
