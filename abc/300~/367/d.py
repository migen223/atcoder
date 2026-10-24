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

n,m=mi()
a=li()

l=[0]
for i in range(2*n):
    l.append(a[i%n])

r=[0]
for i in range(1,2*n):
    r.append((r[-1]+l[i])%m)

ans=0
dic={}
for i in range(n):
    if r[i] not in dic:
        dic[r[i]]=1
    else:
        dic[r[i]]+=1
ans=dic[r[0]]-1
for i in range(1,n):
    dic[r[i-1]]-=1
    if dic[r[i-1]]==0:
        dic.pop(r[i-1])
    if r[i+n-1] in dic:
        dic[r[i+n-1]]+=1
    else:
        dic[r[i+n-1]]=1
    ans+=dic[r[i]]-1
print(ans)