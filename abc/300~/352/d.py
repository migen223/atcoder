import heapq
n,k=map(int,input().split())
p=list(map(int,input().split()))

minh=[]
maxh=[]
dic1={}
dic2={}
for i in range(n):
    dic1[p[i]]=i
    dic2[i]=p[i]

se=set(range(1,1+k))
for i in range(1,1+k):
    heapq.heappush(minh,dic1[i])
    heapq.heappush(maxh,-dic1[i])

#print(f"min={minh}")
#print(f"max={maxh}")
ans=-maxh[0]-minh[0]
for i in range(1,n-k+1):
    se.discard(i)
    se.add(i+k)
    heapq.heappush(minh,dic1[i+k])
    heapq.heappush(maxh,-dic1[i+k])
    while dic2[minh[0]] not in se:
        heapq.heappop(minh)
    while dic2[-maxh[0]] not in se:
        heapq.heappop(maxh)
    #print(f"min={minh}")
    #print(f"max={maxh}")
    #print(se)
    ans=min(ans,-maxh[0]-minh[0])
print(ans)


