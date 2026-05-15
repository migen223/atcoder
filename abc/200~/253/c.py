import heapq
maxh=[]
minh=[]
se=set()
dic={}
delete=set()
q=int(input())
for i in range(q):
    que=input().split()
    if que[0]=="1":
        x=int(que[1])
        if x in delete:
            delete.remove(x)
        if x in se:
            dic[x]+=1
        else:
            dic[x]=1
            heapq.heappush(maxh,-x)
            heapq.heappush(minh,x)
            se.add(x)
    elif que[0]=="2":
        x=int(que[1])
        c=int(que[2])
        if x in dic:
            if dic[x]<=c:
                se.remove(x)
                delete.add(x)
            else:
                dic[x]-=c
    elif que[0]=="3":
        while -maxh[0] in delete:
            heapq.heappop(maxh)
        ma=-maxh[0]
        while minh[0] in delete:
            heapq.heappop(minh)
        mi=minh[0]
        print(ma-mi)






