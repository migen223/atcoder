import sys
from functools import lru_cache
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
#(i>>j)&1 →j bit目がたっているかどうか
#i|(1<<j) →iのjbit目を立たせる
n=ii()

word=[]
top={}
graph=[[] for i in range(n)]
for i in range(n):
    s=input()
    word.append("".join([s[0],s[-1]]))
    if s[0] in top:
        top[s[0]].append(i)
    else:
        top[s[0]]=[i]

for i in range(n):
    if word[i][1] in top:
        for ne in top[word[i][1]]:
            graph[i].append(ne)

@lru_cache(None)
def solve(vis,now):
    for ne in graph[now]:
        if not (vis>>ne)&1:
            if not solve(vis|(1<<ne),ne):
                return True
    return False

ans=False
for s in range(n):
    if not solve(1<<s,s):
        ans=True
        break
if ans:
    print("First")
else:
    print("Second")