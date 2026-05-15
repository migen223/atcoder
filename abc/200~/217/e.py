from sortedcontainers import SortedList
from collections import deque
q=int(input())
a=SortedList([])
aq=deque([])
for _ in range(q):
    que=list(map(int,input().split()))
    if que[0]==1:
        x=que[1]
        aq.append(x)
    elif que[0]==2:
        if len(a)==0:
            print(aq[0])
            aq.popleft()
        else:
            print(a[0])
            a.discard(a[0])
    elif que[0]==3:
        while aq:
            a.add(aq.popleft())