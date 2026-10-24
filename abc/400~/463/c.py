from heapq import *
n=int(input())

hq=[]
for _ in range(n):
    h,l=map(int,input().split())
    heappush(hq,(-h,l))

q=int(input())
t=list(map(int,input().split()))
#print(hq)
ans={}
qsort=sorted(t)
for i in range(q):
    while hq[0][1]<=qsort[i]:
        heappop(hq)
    #print(-hq[0][0])
    if qsort[i] not in ans:
        ans[qsort[i]]=-hq[0][0]

for i in range(q):
    print(ans[t[i]])