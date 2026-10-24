from sortedcontainers import SortedList
n,q=map(int,input().split())

l=[0]*n
minus=0
sl=SortedList(l)
for _ in range(q):
    que=list(map(int,input().split()))
    if que[0]==1:
        x=que[1]-1
        pre=l[x]
        sl.discard(pre)
        sl.add(pre+1)
        l[x]+=1
    else:
        y=que[1]
        minus=sl[0]
        ind=sl.bisect_left(minus+y)
        #print(sl)
        #print(n-ind)
        #print("ans",n-ind,ind,y)
        print(n-ind)
