from collections import deque
n,q=map(int,input().split())

train=[[-1,-1] for i in range(n+1)]
#前,後ろ

for i in range(q):
    que=list(map(int,input().split()))
    x=que[1]
    if que[0]==1:
        y=que[2]
        train[x][1]=y
        train[y][0]=x
    if que[0]==2:
        y=que[2]
        train[x][1]=-1
        train[y][0]=-1
    elif que[0]==3:
        ans=deque([x])
        pre=x
        bac=x
        while train[pre][0]!=-1:
            ans.appendleft(train[pre][0])
            pre=train[pre][0]
        while train[bac][1]!=-1:
            ans.append(train[bac][1])
            bac=train[bac][1]
        print(len(ans),end=" ")
        print(*ans)


