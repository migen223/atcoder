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
cand=[0]*n
name={}
name2=[]
for _ in range(n):
    s=input()
    name[s]=0
    name2.append(s)

for _ in range(m):
    t=input()
    l1=[]
    l2=[]
    cand=[]
    f=0
    for s in name:
        
        if s==t:
            name[s]+=1
            f+=1
            break
        if len(s)!=len(t) :
            continue
        count=0
        for j in  range(len(s)):
            if s[j]!=t[j]:
                count+=1
        if count==1:
            cand.append(s)
    #debug(cand,t)
    if len(cand)==1 and f==0:
        name[cand[0]]+=1
    #print(name,t)

for i in range(n):
    print(name[name2[i]])