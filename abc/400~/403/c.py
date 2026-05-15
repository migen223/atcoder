
n,m,q=map(int,input().split())

user=[set() for i in range(n+1)]

for _ in range(q):
    que=tuple(map(int,input().split()))
    
    if que[0]==1:
        x=que[1]
        y=que[2]
        user[x].add(y)
    
    elif que[0]==2:
        x=que[1]
        user[x].add(-1)
    else:
        x=que[1]
        y=que[2]
        if -1 in user[x]:
            print("Yes")
        else:
            if y in user[x]:
                print("Yes")
            else:
                print("No")




