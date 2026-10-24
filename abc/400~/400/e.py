import sys
from bisect import bisect_right
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
def eratosthenes(n):
    is_prime = ([False, True] * (n//2+1))[0: n+1]
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, n+1, 2):
        if not(is_prime[i]):
            continue
        if i*i > n:
            break
        for k in range(i*i, n+1, i):
            is_prime[k] = False
    return is_prime

el=eratosthenes(10**6+1)
se=set()
pri=[]
for i in range(10**6+1):
    if el[i]:
        now=i*i
        while now<=10**12:
            se.add(now)
            pri.append((now,i))
            now*=i*i

ansl=[]
pri.sort()
for i in range(len(pri)-1):
    for j in range(i+1,len(pri)):
        if pri[i][0]*pri[j][0]>10**12:
            break
        if pri[i][1]==pri[j][1]:
            continue
        ansl.append(pri[i][0]*pri[j][0])
ansl.sort()
#print(ansl[:10])
q=ii()
for _ in range(q):
    a=ii()
    ind=bisect_right(ansl,a)-1
    print(ansl[ind])
    #debug(ansl[ind])