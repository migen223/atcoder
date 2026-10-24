from random import randint
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


for _ in range(100):
    n,m=randint(1,7),randint(1,10)

    wins=[]
    cand=[]
    win=[]
    se=set()
    for _ in range(m):
        a,b=randint(1,n),randint(1,n)
        wins.append(set([a,b]))
        win.append((a,b))

    for a,b in win:
        if a not in se:
            se.add(a)
            cand.append(a)
        if b not in se:
            se.add(b)
            cand.append(b)
        if len(cand)>4:
            break

    ans=0
    for i in range(len(cand)-1):
        for j in range(i+1,len(cand)):
            a,b=cand[i],cand[j]
            f=0
            for k in range(m):
                if a not in wins[k] and b not in wins[k]:
                    f+=1
                    break
            if f==0:
                ans+=1
    #print(ans)

    ans1=0
    for i in range(1,n):
        for j in range(i+1,n+1):
            a,b=i,j
            f=0
            for k in range(m):
                if a not in wins[k] and b not in wins[k]:
                    f+=1
                    break
            if f==0:
                ans1+=1
    if ans1!=ans:
        print()
        print(n,m,win)
        print(ans,ans1)
