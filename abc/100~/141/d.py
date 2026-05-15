from heapq import *
n,m=map(int,input().split())
a=list(map(int,input().split()))
h=[-i for i in a]
heapify(h)
for i in range(m):
    ma=heappop(h)
    heappush(h,int(ma/2))
ansl=[]
for _ in range(n):
    ansl.append(heappop(h))
print(-sum(ansl))
