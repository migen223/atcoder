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

n=ii()
a=li()
r=[0]
if n==1:
    print(a[0])
    sys.exit()
for i in range(n):
    r.append(r[-1]+a[i])

s=[r[-1]]
for i in range(1,n//2):
    ne=r[-1-i]-r[i]
    s.append(s[-1]+ne)
if n%2==1:
    s.append(s[-1]+a[n//2])
#print(s)
k=n//2
for i in range(n//2):
    s.append(s[k-i-1])
#print(s)


ans=0

for i in range(len(s)):
    su=(s[i]*(pow(i+1,-1,mod)%mod))%mod
    ans+=su
    ans%=mod

print(ans)


"""
for  i in range(1,1+n):
    l=[0]*n
    for j in range(n-i+1):
        for k in range(i):
            l[j+k]+=1
    print(l)
    #print(sum(l))
    """