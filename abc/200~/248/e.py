import sys
from math import gcd
    
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

n,K=mi()

point=[]

for i in range(n):
    x,y=mi()
    point.append((x,y))

se=set()
ans=0

if K==1:
    print("Infinity")
    exit()

for i in range(n-1):
    x1,y1=point[i]
    for j in range(1,n):
        x2,y2=point[j]
        if x1==x2:
            if (0,inf,x1) not in se:
                res=0
                for k in range(n):
                    if point[k][0]==x1:
                        res+=1
                if res>=K:
                    ans+=1
                se.add((0,inf,x1))
        else:
            g=gcd(abs(y2-y1),abs(x2-x1))
            m=[abs(y2-y1)//g,abs(x2-x1)//g]
            if (y2-y1)*(x2-x1)<0:
                m.append(-1)
            else:
                m.append(1)
            d1=-x1*(y2-y1)+(x2-x1)*y1
            d2=x2-x1
            g2=gcd(abs(d1),abs(d2))
            d=[abs(d1)//g,abs(d2)//g]
            if d1*d2<0:
                m.append(-1)
            else:
                m.append(1)
            line=tuple(tuple(m)+tuple(d))
            if line not in se:
                res=0
                for k in range(n):
                    x3,y3=point[k]
                    if (x2-x1)*(y3-y1)==(y2-y1)*(x3-x1):
                        res+=1
                if res>=K:
                    ans+=1
                #debug(res,k)
                se.add(line)

#print(se)
print(ans)