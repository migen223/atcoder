"""
import heapq
n=int(input())
minheap=list(map(int,input().split()))
maxheap=[-minheap[i] for i in range(n)]

heapq.heapify(minheap)
heapq.heapify(maxheap)

ans=0
ma=-heapq.heappop(maxheap)
mi=heapq.heappop(minheap)
heapq.heappush(maxheap,-ma)
heapq.heappush(minheap,mi)
while ma-mi>=2:
    ma=-(heapq.heappop(maxheap)+1)
    mi=heapq.heappop(minheap)+1
    ans+=1
    heapq.heappush(maxheap,-ma)
    heapq.heappush(minheap,mi)
    ma=-heapq.heappop(maxheap)
    mi=heapq.heappop(minheap)
    heapq.heappush(maxheap,-ma)
    heapq.heappush(minheap,mi)
    #print(maxheap)
    #print(minheap)
print(ans)
"""

n=int(input())
a=list(map(int,input().split()))
s=sum(a)
p=s//n
r=s%n
a.sort()
b=[]
for i in range(n-r):
    b.append(p)
for i in range(r):
    b.append(p+1)
ans=0
for i in range(n):
    ans+=abs(a[i]-b[i])
print(ans//2)

