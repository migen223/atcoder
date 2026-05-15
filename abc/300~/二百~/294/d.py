from collections import deque

n,q=map(int,input().split())
nocall=deque([i for i in range(1,n+1)])
nogo=deque([])
go=set()
for i in range(q):
    que=list(map(int,input().split()))
    if que[0]==1:
        p=nocall.popleft()
        nogo.append(p)
    if que[0]==2:
        go.add(que[1])
    if que[0]==3:
        while nogo[0] in go:
            nogo.popleft()
        print(nogo[0])
    #print(f"nocall={nocall}")
    #print(f"nogo={nogo}")
    #print(f"go={go}")





