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

n,k=mi()
se=set()
first=[0]*n
first[0]=k
ans=[tuple(first)]
def dfs(now):
    global se,ans
    #debug(now)
    for i in range(1,n):
        if now[0]>=1*(i+1):
            now[0]-=1*(i+1)
            now[i]+=1
            tn=tuple(now)
            if tn not in se:
                dfs(now)
                ans.append(tn)
                se.add(tn)
            now[0]+=1*(i+1)
            now[i]-=1
        else:
            break

se.add(tuple(first))
#debug(se)
dfs(first)
ans.sort()
for i in range(len(ans)):
    print(*ans[i])