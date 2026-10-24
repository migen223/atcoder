from collections import deque
n=int(input())

 
point=[]
for i in range(n):
    x,y=map(int,input().split())
    point.append((x,y))

point.sort(reverse=True)
right=deque([])
mi=10**32
for i in range(n-1):
    mi=min(point[-1-i][1],mi)
    right.appendleft(mi)
#print(point)
#print(right)
ans=n
for i in range(n-1):
    x,y=point[i]
    #print(y,right[0])
    if y>right[0]:
        ans-=1
    right.popleft()

print(ans)