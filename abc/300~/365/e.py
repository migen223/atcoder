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

n=ii()
a=li()

ans=0
ab=[format(a[i],'b') for i in range(n)]
ma=len(max(ab,key=lambda x:len(x)))
ab=[format(a[i], f"0{ma}b") for i in range(n)]
ansl=[0]*ma
for i in range(ma):
    l=[0,0] #[偶数、奇数]
    for j in range(n):
        s=ab[j]
        bit=int(s[-1-i])
        if bit==0:
            ansl[i]+=l[1]
            l[0]+=1
        else:
            ansl[i]+=l[0]
            l=[l[1],l[0]]
            l[1]+=1

for i in range(len(ansl)):
    ans+=(2**i)*ansl[i]
print(ans)