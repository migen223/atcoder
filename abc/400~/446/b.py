from collections import deque
n,m=map(int,input().split())

drink=set(range(1,m+1))
for i in range(n):
    l=int(input())
    x=deque(map(int,input().split()))
    ans=0
    while x:
        d=x.popleft()   
        if d in drink:
            ans=d
            drink.discard(d)
            break
    print(ans)