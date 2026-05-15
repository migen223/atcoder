n,q=map(int,input().split())
nl=[i+1 for i in range(n)]
count=0
for _ in range(q):
    qw=list(map(int,input().split()))
    if qw[0]==1:
        nl[(qw[1]-1+count)%n]=qw[2]
    elif qw[0]==3:
        count+=qw[1]
    else:
        print(nl[(qw[1]-1+count)%n])

