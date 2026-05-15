from sortedcontainers import SortedList
n,k=map(int,input().split())
h=list(map(int,input().split()))

ans=0
sl=SortedList([h[i] for i in range(k)])
ans=sl[-1]-sl[0]
for i in range(n-k):
    sl.discard(h[i])
    sl.add(h[i+k])
    ans=max(ans,sl[-1]-sl[0])
    #print(sl)
print(ans)
