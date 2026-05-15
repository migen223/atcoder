n,q=map(int,input().split())
py=[0]*(n+1)
pr=[0]*(n+1)
for i in range(q):
    que=list(map(int,input().split()))
    if que[0]==1:
        py[que[1]]+=1
    if que[0]==2:
        pr[que[1]]+=1
    if que[0]==3:
        if py[que[1]]>=2 or pr[que[1]]>=1:
            print("Yes")
        else:
            print("No")