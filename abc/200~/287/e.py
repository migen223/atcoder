import sys
from collections import deque
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


n=ii()
sl=[]
for i in range(n):
    s=input()
    sl.append(s)
ss=sorted(sl)

#print(ss)
ans=[0]*n
dic={}
for i in range(n):
    if ss[i] in dic:
        continue
    pre=i-1
    plcp=0
    aft=i+1
    alcp=0
    if 0<=pre:
        for j in range(min(len(ss[i]),len(ss[pre]))):
            if ss[i][j]!=ss[pre][j]:
                break
            plcp+=1
    if aft<=n-1:
        for j in range(min(len(ss[i]),len(ss[aft]))):
            if ss[i][j]!=ss[aft][j]:
                break
            alcp+=1
    dic[ss[i]]=max(alcp,plcp)
for i in range(n):
    print(dic[sl[i]])
