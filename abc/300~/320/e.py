from heapq import *
n,m=map(int,input().split())

ans=[0]*n
eat=[]
wait=[]
for i in range(n):
    heappush(wait,i)
for _ in range(m):
    t,w,s=map(int,input().split())
    if eat:
        while eat[0][0]<=t:
            time,p=heappop(eat)
            heappush(wait,p)
            if not eat:
                break

    if len(wait)==0:
        continue
    now=heappop(wait)
    ans[now]+=w
    heappush(eat,(t+s,now))
    #print("t",t)
    #print("wait",wait)
    #print("eat",eat)

for i in range(n):
    print(ans[i])