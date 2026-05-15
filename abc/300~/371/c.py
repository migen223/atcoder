from itertools import permutations
n=int(input())
a = [[False] * n for _ in range(n)]
b = [[False] * n for _ in range(n)]
mg=int(input())

for _ in range(mg):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  a[u][v] = a[v][u] = True
  
mh=int(input())
for _ in range(mh):
  u, v = map(int, input().split())
  u -= 1
  v -= 1
  b[u][v] = b[v][u] = True
"""
gg=[set() for i in range(n)]
for i in range(mg):
    u,v=map(lambda x:int(x)-1,input().split())
    gg[u].add(v)
    gg[v].add(u)

gh=[set() for i in range(n)]
mh=int(input())
for i in range(mg):
    u,v=map(lambda x:int(x)-1,input().split())
    gh[u].add(v)
    gh[v].add(u)"""

cost={}
for i in range(n-1):
    al=list(map(int,input().split()))
    for j in range(i+1,i+1+len(al)):
        cost[(i,j)]=al[j-i-1]

ans=10**32
for p in permutations(range(n)):
    now=0
    for i in range(n):
        for j in range(n):
            if a[i][j]!=b[p[i]][p[j]]:
               now+=cost[(min(p[i],p[j]),max(p[i],p[j]))]
    ans=min(ans,now)
#print()
print(ans//2)