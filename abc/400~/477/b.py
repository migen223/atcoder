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

n,d=mi()
x=li()

ans=[]
for i in range(n):
    f=0
    for j in range(n):
        if i==j:
            continue
        if abs(x[i]-x[j])<d:
            f+=1

            break
    if f==0:
        ans.append(i+1)

print(len(ans))
print(*ans)
