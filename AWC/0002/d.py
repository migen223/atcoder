from collections import deque
n,m=map(int,input().split())
c=list(map(int,input().split()))
r=list(map(int,input().split()))

c.sort()
r.sort()
c=deque(c)
r=deque(r)
ans=0


while len(r)>0 and len(c)>0:
    while r[0]<c[0]:
        r.popleft()
        if len(r)==0:
            break
    if len(c)>0 and len(r)>0:
        ans+=1
        c.popleft()
        r.popleft()

"""
unl=[]
l=0
for i in range(m):
    ind=bisect_left(c,r[i],lo=l)
    print(ind,l)
    if ind==n:
        break
    ans+=1
    l=ind+1
    unl.append(ind)
print(unl)
"""
print(ans)