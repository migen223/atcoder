import sys

from itertools import permutations
def debug(*x):print('debug:',*x, file=sys.stderr)
sys.setrecursionlimit(300000)
from collections import defaultdict
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

s=input()

num=defaultdict(list)
for i in range(len(s)):
    num[s[i]].append(i)
nl=[]
for nu in num:
    nl.append(num[nu])
temp=[]
for i in range(len(nl)):
    if nl[i][0]==0:
        temp=nl[i][::]
        ban=i
        break
nl.pop(ban)
#print(nl,temp)

nl.insert(0,temp)
#print(nl)
#print(nl)
p=eratosthenes(10**7)

for per in permutations([0,1,2,3,4,5,6,7,8,9],len(nl)):
    if per[0]==0:
        continue
    ans=[0]*len(s)
    for i in range(len(nl)):
        for j in range(len(nl[i])):
            ans[nl[i][j]]=per[i]
    res=0
    for i in range(len(s)):
        res+=ans[-1-i]*10**i
    if p[res]:
        print(res)
        exit()
print(-1)
