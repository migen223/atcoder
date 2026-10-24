import heapq 
n,k,m=map(int,input().split())

hq=[]
for _ in range(n):
    c,v=map(int,input().split())
    heapq.heappush(hq,(-v,c))

ans=[]
kind=set()
stock=[]

while hq:
    v,c=heapq.heappop(hq)
    v*=-1
    if c in kind:
        stock.append(v)
    else:
        if len(kind)<m:
            ans.append(v)
            kind.add(c)
        else:
            stock.append(v)

#print(ans)
#print(stock)

ind=0
while len(ans)<k:
    ans.append(stock[ind])
    ind+=1
print(sum(ans))