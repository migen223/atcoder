import heapq

n,k=map(int,input().split())
people=[]
cand=[]
for i in range(n):
    a,b=map(int,input().split())
    people.append((a,b))
people.sort(reverse=True,key=lambda x:x[1])
cand=[]
s=0
m=10**32
for i in range(k):
    a,b=people[i]
    heapq.heappush(cand,a)
    s+=a
    m=min(m,b)
ans=s*m

for i in range(k,n):
    a,b=people[i]
    m=b
    if cand[0]<a:
        s-=heapq.heappop(cand)
        s+=a
        heapq.heappush(cand,a)
    ans=max(ans,s*m)

print(ans)