from collections import deque

q=int(input())

ball=deque([])
for i in range(q):
    que=list((map(int,input().split())))

    if que[0]==1:
        x=que[1]
        c=que[2]
        ball.append([x,c])
    else:
        c=que[1]
        ans=0
        while c-ball[0][1]>0:
            n=ball.popleft()
            c-=n[1]
            ans+=n[1]*n[0]
        if c-ball[0][1]==0:
            n=ball.popleft()
            ans+=n[1]*n[0]
        else:
            ball[0][1]-=c
            ans+=ball[0][0]*c
        print(ans)


