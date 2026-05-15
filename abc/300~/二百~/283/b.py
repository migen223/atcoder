n=int(input())
a=list(map(int,input().split()))
q=int(input())
for i in range(q):
    que=list(map(int,input().split()))
    if que[0]==1:
        a[que[1]-1]=que[2]
    else:
        print(a[que[1]-1])
