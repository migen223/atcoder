import sys
from bisect import bisect_left
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

t=ii()


for _ in range(t):
    n,m=mi()
    c=[(0,0)]#(値、個数)
    b=[(0,0)]#(累積(最後の値)、要素数)
    br=[(0,0)]#(ブロック終了時点でのbの累積和、要素数)
    #a=[(0,0)]
    change=[]
    for i in range(n):
        x,y=mi()
        c.append([x,y])
        b.append((b[-1][0]+x*y,b[-1][1]+y))
        br.append((br[-1][0]+y*b[-2][0]+x*y*(y+1)//2,b[-1][1]))

    
    for i in range(1,n):
        #debug(b[i][0],b[i+1][0])
        if b[i][0]>=0 and b[i+1][0]<0:
            change.append(b[i][1]+b[i][0]//abs(c[i+1][0]))
    if b[-1][0]>0:
        change.append(m)
    
    ans=c[1][0]
    #print(br)
    for i in range(len(change)):
        ch=change[i]
        ind=bisect_left(br,ch,key=lambda x:x[1])
        
        ch-=br[ind-1][1]
        res=br[ind-1][0]
        #print(br[ind],res,ch,b[ind-1],c[ind],ch*b[ind-1][0],c[ind][0]*ch*(ch+1)//2)
        res+=ch*b[ind-1][0]+c[ind][0]*ch*(ch+1)//2
        #b[ind]ブロックのi=1~chまでの和をたす
        ans=max(ans,res)
    #print(change)
    #print(b)
    print(ans)
    #debug(ans)


    """
    cm=[]
    for x,y in c:
        for j in range(y):
            cm.append(x)
    #print(cm)
    a=[]
    for i in range(1,m+1):
        ai=0
        for j in range(i):
            ai+=(i-j)*cm[j]
        a.append(ai)
    debug(max(a))
    #"""

"""
1
3 7
-1 2
2 3
-3 2

1
10 472
-4 12
1 29
2 77
-1 86
0 51
3 81
3 17
-2 31
-4 65
4 23
"""