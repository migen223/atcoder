from sortedcontainers import SortedList
n,m=map(int,input().split())

sl=SortedList(range(1,n+1))
sl.add(10**32)
que=[]
for i in range(m):
    l,r,c=map(int,input().split())
    que.append((l,r,c))

ans=[0]*(n+1)
while que:
    l,r,c=que.pop()
    i=sl.bisect_left(l)
    ban=[]
    while l<=sl[i]<=r:
        ban.append(sl[i])
        i+=1
    for b in ban:
        ans[b]=c
        sl.remove(b)
    #print(sl)

for i in range(1,n+1):
    print(ans[i],end=" ")
print()