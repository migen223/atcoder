from collections import deque
from sortedcontainers import SortedList
import sys
n,m=map(int,input().split())
cars=[]
for _ in  range(m):
    l,r=map(lambda x:int(x)-1,input().split())
    cars.append((l,r))
cars.sort(key=lambda x:x[1])
stop=SortedList(range(n))

for i in range(m):
    if len(stop)==0:
        print("No")
        sys.exit()
    l,r=cars[i]
    ind=stop.bisect_left(l)
    if ind==len(stop):
        print("No")
        sys.exit()
    if stop[ind]>r:
        print("No")
        sys.exit()
    stop.discard(stop[ind])

print("Yes")
"""
cars=[]
for _ in  range(m):
    l,r=map(lambda x:int(x)-1,input().split())
    cars.append((l,r))
cars.sort()
print(cars)
stop=deque((range(n)))

for i in range(m):
    if len(stop)==0:
        print("No")
        sys.exit()
    if cars[i][0]>stop[0]:
        while cars[i][0]<=stop[0]:
            stop.popleft()
    elif cars[i][0]<=stop[0]<=cars[i][1]:
        stop.popleft()
    else:
        print("No")
        sys.exit()


print("Yes")

       """

"""
imos=[0]*(n+1)
for _ in range(m):
    l,r=map(int,input().split())
    imos[l-1]+=1
    imos[r]-=1

for i in range(n):
    imos[i+1]+=imos[i]


res=0
for i in range(n):
    if imos[i]>=1:
        res+=1

if res>=m:
    print("Yes")
else:
    print("No")"""