from sortedcontainers import SortedList
q=int(input())

balls=SortedList([])
dic={}
plus=0

for i in range(q):
    que=list(map(int,input().split()))
    if que[0]==1:
        x=que[1]
        balls.add(x-plus)
    elif que[0]==2:
        x=que[1]
        plus+=x
    elif que[0]==3:
        print(balls.pop(0)+plus)