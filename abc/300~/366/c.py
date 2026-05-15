q=int(input())
box=set()
ball=[0]*1000001
kind=0
for i in range(q):
    que=input().split()
    if que[0]=="1":
        ball[int(que[1])]+=1
        if ball[int(que[1])]==1:
            kind+=1
    elif que[0]=="2":
        ball[int(que[1])]-=1
        if ball[int(que[1])]==0:
            kind-=1
    else:
        print(kind)