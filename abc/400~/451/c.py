import heapq
q=int(input())

ans=[]
for _ in range(q):
    que=list(map(int,input().split()))
    h=que[1]
    if que[0]==1:
        heapq.heappush(ans,h)
    else:
        if len(ans)==0:
            print(0)
            continue
        while ans[0]<=h:
            heapq.heappop(ans)
            if len(ans)==0:
                break
    
    print(len(ans))
