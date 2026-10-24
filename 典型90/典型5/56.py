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

n,s=mi()
dp=[[False for _ in range(n)] for _ in range(s+1)]

goods=[]
for i in range(n):
    a,b=mi()
    goods.append((a,b))
if goods[0][0]<=s:
    dp[goods[0][0]][0]=True
if goods[0][1]<=s:
    dp[goods[0][1]][0]=True

for i in range(n-1):
    for j in range(s):
        if not dp[j][i]:
            continue
        if j+goods[i+1][0]<=s:
            dp[j+goods[i+1][0]][i+1]=True
        if j+goods[i+1][1]<=s:
            dp[j+goods[i+1][1]][i+1]=True



if dp[-1][-1]:
    ans=[]
    orig=s
    for i in range(n-1,0,-1):
        #debug(s-goods[i][1],i-1,dp[s-goods[i][1]][i-1])
        if 0<=s-goods[i][0]<=orig and dp[s-goods[i][0]][i-1]:
            ans.append("A")
            s-=goods[i][0]
            continue
        if 0<=s-goods[i][1]<=orig and dp[s-goods[i][1]][i-1]:
            ans.append("B")
            s-=goods[i][1]
        #debug("efaub",ans)
    if s==goods[0][0]:
        ans.append("A")
    else:
        ans.append("B")
    ans.reverse()
    print("".join(ans))
else:
    print("Impossible")
"""
if goods[0][0]<=s:
    dp[goods[0][0]][0][1]="A"
if goods[0][1]<=s:
    dp[goods[0][1]][0][1]="B"

for i in range(n-1):
    for j in range(s):
        if dp[j][i][1]=="c":
            continue
        if j+goods[i+1][0]<=s:
            dp[j+goods[i+1][0]][i+1]=[j,"A"]
        if j+goods[i+1][1]<=s:
            dp[j+goods[i+1][1]][i+1]=[j,"B"]

if dp[-1][-1][1]=="c":
    print("Impossible")
else:
    ans=[dp[-1][-1][1]]
    ne=dp[-1][-1][0]
    i=n-2
    while i>=0:
        ans.append(dp[ne][i][1])
        ne=dp[ne][i][0]
        i-=1
    ans.reverse()
    print("".join(ans))

    """