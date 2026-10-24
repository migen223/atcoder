from heapq import *
n,m=map(int,input().split())

p=list(map(int,input().split()))
l=list(map(int,input().split()))
d=list(map(int,input().split()))

c=[]
for i  in range(m):
    c.append((l[i],d[i]))

hq=[]
p.sort()
c.sort(reverse=True)

ans=sum(p)

for i in range(n):
    pr=p[i]
    if c:
        while pr>=c[-1][0]:
            heappush(hq,-c[-1][1])
            c.pop()
            if not c:
                break
    if hq:
        ans+=heappop(hq)
    #print(i,hq,c)

print(ans)
