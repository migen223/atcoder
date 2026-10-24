from collections import deque
from heapq import *
n=int(input())

time=[]
for _ in range(n):
    t,d=map(int,input().split())
    time.append((t,t+d))

time.sort()
time=deque(time)
hq=[]
ans=0
now=1
while time or hq:
    while time and time[0][0]<=now:
        s,e=time.popleft()
        heappush(hq,(e,s))
    if hq:
        e,s=hq[0]
        if s<=now<=e:
            ans+=1
            now+=1
            heappop(hq)
        else:
            while hq and hq[0][0]<now:
                heappop(hq)
    else:
        if time :
            now=time[0][0]
    
    #print(hq,now,ans)

print(ans)

