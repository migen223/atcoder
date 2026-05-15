n=int(input())
a=list(map(int,input().split()))
q=int(input())
now=-1

se=set()
dic={}
for i in range(q):
    que=list(map(int,input().split()))

    if que[0]==1:
        now=que[1]
        se=set()
        dic={}
    elif que[0]==2:
        if now==-1:
            a[que[1]-1]+=que[2]
        
        else:
            if que[1] not in se:
                dic[que[1]]=que[2]
                se.add(que[1])
            else:
                dic[que[1]]+=que[2]
    elif que[0]==3:
        if now==-1:
            print(a[que[1]-1])
        else:
            if que[1] in se:
                print(now+dic[que[1]])
            else:
                print(now)
