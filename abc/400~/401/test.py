import sys
from itertools import product
from random import randint
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

for i in range(10):

    k=randint(1,5)
    s=[]
    for i in range(randint(0,2)):
        s.append(".")
    for i in range(k):
        s.append("o")
        for i in range(randint(1,3)):
            s.append(".")
    
    n=len(s)
    for i in range(n):
        p=randint(0,9)
        if p<4:
            s[i]="?"
    print("".join(s),n,k)

    for i in range(n):
        f=0
        if 0<=i-1<=n-1:
            if s[i-1]=="o":
                f+=1
        if 0<=i+1<=n-1:
            if s[i+1]=="o":
                f+=1
        if f>=1:
            s[i]="."

    unk=[]
    for i in range(n):
        if s[i]=="?":
            unk.append(i) 
        if s[i]=="o":
            k-=1
    if k==0:
        for i in range(n):
            if s[i]=="?":
                s[i]="."
        print("".join(s))
        continue
        #sys.exit()

    pres=[[unk[0],unk[0]]]
    unk.append(inf)
    limit=0
    for i in range(len(unk)-1):
        if pres[-1][1]+1==unk[i+1]:
            pres[-1][1]+=1
        else:
            limit+=((pres[-1][1]-pres[-1][0]+1)+1)//2
            pres.append([unk[i+1],unk[i+1]])
    pres.pop()

    ans=s[::]

    if k==limit:
        for ps,pe in pres:
            if (pe-ps+1)%2==0:
                continue
            for i in range(ps,pe+1):
                if i%2==ps%2:
                    ans[i]="o"
                else:
                    ans[i]="x"

    print("".join(ans))

    print()
