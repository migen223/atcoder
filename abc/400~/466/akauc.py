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
n=ii()
m=1
while 2**m<n:
    m+=1
print(m)

for i in  range(m):
    l=[]
    for j in range(n):
        if (j >> i) & 1:
            l.append(j+1)
    print(len(l),*l)
s=list(input())
s.reverse()
s="".join(s)
print(int(s,2)+1)