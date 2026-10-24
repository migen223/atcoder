import sys

from collections  import defaultdict
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
a=li()

minus=0
have=0

dic=defaultdict(list)
for i in range(n):
    dic[a[i]].append(i)
    if a[i]>0:
        have+=1
kind=sorted(list(set(a)),reverse=True)
if kind[-1]==0:
    kind.pop()
#print(dic,kind)
eat=0

while kind:
    orig=kind.pop()
    now=orig-minus
    if eat+have*now>=k:
        minus+=(k-eat)//have
        ind=((k-eat)%have)
        if ind==0:
            for i in range(n):
                a[i]=max(a[i]-minus,0)
        else:
            count=0
            for i in range(n):
                if a[i]-minus>0:
                    if count<ind:
                        a[i]-=minus+1
                    else:
                        a[i]-=minus
                    count+=1
                else:
                    a[i]=0
        break
    else:
        eat+=have*now
        have-=len(dic[orig])
        minus+=now
    #debug(eat,have,minus)

print(*a)