from heapq import *
n,m=map(int,input().split())

hq=[]
for i in range(n):
    f,d=map(int,input().split())
    heappush(hq,(-f,d))

ans=0
for i in range(m):
    now=heappop(hq)
    #print(now)
    ans+=max(-now[0],0)
    heappush(hq,(now[0]+now[1],now[1]))
    #print(hq)
print(ans)