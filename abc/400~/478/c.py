import sys

from sortedcontainers import SortedList
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

done=[[0,0,a[0]]]
for i in range(1,n):
    if done[-1][2]<=a[i]:
        done[-1][1]=i
        done[-1][2]=a[i]
    else:
        done.append([i,i,a[i]])

sort=[[0,0] for _ in range(n)]
for i in range(len(done)):
    for j in range(done[i][0],done[i][1]+1):
        sort[j]=[done[i][0],done[i][1]]

sl=SortedList(a[:k])

if sl[-1]<=a[k] and sort[k][1]==n-1:
    print("Yes")
    exit()

for i in range(n-k):
    sl.discard(a[i])
    sl.add(a[i+k])
    if sort[i][0]==0 and a[i]<=sl[0] and sort[i+k+1][1]==n-1 and a[i+k+1]>=sl[-1]:
        print("Yes")
        exit()

print("No")
