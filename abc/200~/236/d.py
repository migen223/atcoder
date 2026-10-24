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

n=ii()
good=[[0 for  _ in range(2*n)] for  _ in range(2*n)]
for i in range(2*n-1):
    a=li()
    for j in range(i+1,2*n):
        good[i][j]=a[j-i-1]
        good[j][i]=a[j-i-1]
ans=0
se=set()
def solve(use,peo):
    global ans
    #print(use)
    start=-1
    b=use[-1]
    if peo==2*n:
        ans=max(ans,b)
        return
    for i in range(2*n):
        if use[i]==0:
            start=i
            break
    use[start]=1
    """
    for i in range(start+1,2*n):
        if use[i]==0:
            nuse=use[::]
            nuse[i]=1
            nuse[-1]=b^good[start][i]
            solve(nuse)
            #debug(nuse,i,start)"""

    for i in range(start+1,2*n):
        if use[i]==0:
            use[i]=1
            use[-1]=b^good[start][i]
            solve(use,peo+2)
            #debug(use,i,start)
            use[i]=0
            use[-1]=b
    use[start]=0
            
solve([0 for _ in range(2*n+1)],0)
print(ans)
"""
for i in range(start+1,2*n):
        if use[i]==0:
            nuse=use[::]
            nuse[i]=1
            nuse[-1]=b^good[start][i]
            solve(nuse)
            debug(nuse,i,start)
def solve(use):
    global ans,se
    #print("0",use)
    b=use[-1]
    if sum(use)-b==2*n:
        ans=max(b,ans)
        return
    for i in range(2*n-1):
        for j in range(i+1,2*n):
            if use[i]+use[j]==0 :
                use[i]=1
                use[j]=1
                pre=use[-1]
                use[-1]=pre^good[i][j]
                #print("1",use)
                t=tuple(use)
                if t not in se:
                    #print("4",use)
                    solve(use)
                    se.add(t)
                #print("2",use)
                use[i]=0
                use[j]=0
                use[-1]=pre
solve([0 for _ in range(2*n+1)])
print(ans)"""
"""
ans=0
se=set()
def solve(use):
    global ans,se
    print("0",use)
    b=use.pop()
    if sum(use)==2*n:
        ans=max(b,ans)
        return
    for i in range(2*n-1):
        for j in range(i+1,2*n):
            if use[i]+use[j]==0 :
                use[i]=1
                use[j]=1
                use.append(b^good[i][j])
                print("1",use)
                t=tuple(use)
                if t not in se:
                    print("4",use)
                    solve(use)
                    se.add(t)
                print("2",use)
                use.pop()
                use[i]=0
                use[j]=0
solve([0 for _ in range(2*n+1)])
print(ans)"""