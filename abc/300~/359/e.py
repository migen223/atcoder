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
h=li()
ans=[0]*n
ans[0]=h[0]+1

water=h[0]
left=[(inf,-1),(h[0],0)]

for i in range(n-1):
    water+=1 
    ans[i]=water
    if left[-1][0]>=h[i+1]:
        water+=h[i+1]-1
        left.append((h[i+1],i+1))
    else:
        now=1
        while left and left[-1][0]<=h[i+1]:
            ban=left.pop()
            now+=ban[0]*(ban[1]-left[-1][1])
        water+=h[i+1]*(i+1-left[-1][1])-now
        #debug(now,i+1-left[-1][1])
        left.append((h[i+1],i+1))
    #debug(left,water)


ans[-1]=water+1
print(*ans)

"""
15
14 3 10 5 15 9 7 8 6 11 2 4 13 1 12
"""