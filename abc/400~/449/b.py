
h,w,q=map(int,input().split())

for _ in range(q):
    que=list(map(int,input().split()))
    if que[0]==1:
        print(que[1]*w)
        h-=que[1]
    else:
        print(que[1]*h)
        w-=que[1]
