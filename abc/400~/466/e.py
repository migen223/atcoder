import sys

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

n,k=mi()
def submax(l):
    if max(l)<=0:
        return [0,0,0]
    r=[0]
    sub=[]
    now=[-1,-1]
    #print(l)
    for i in range(len(l)):
        if now[0]<0 :
            if l[i]>=0:
                now=[l[i],i]
        else:
            if now[0]+l[i]<0:
                now.append(i)
                sub.append(now)
                now=[-1,-1]
            else:
                now[0]+=l[i]
        sub.append((now[0],now[1],i+1))
    #print(sub)
    return max(sub,key=lambda x:x[0])


    

d=[]
ans=0
for i in range(n):
    a,b=mi()
    d.append(b-a)
    ans+=a


for i in range(k):
    sub=submax(d)
    if sub:
        for j in range(sub[1],sub[2]):
            d[j]*=-1
        ans+=sub[0]
print(ans)

