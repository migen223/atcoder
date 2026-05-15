import heapq
n=int(input())

dic={}
size=[]
num=[]
for i in range(n):
    s,c=map(int,input().split())
    heapq.heappush(size,s)
    num.append(c)
    dic[s]=c

ans=0
count=0
while size:
    now=heapq.heappop(size)
    k=dic[now]//2
    count+=1
    
    ans+=dic[now]-2*k
    
    if k>0:
        if 2*now in dic:
            dic[2*now]+=k
        else:
            dic[2*now]=k
            heapq.heappush(size,2*now)

print(ans)
    
    

