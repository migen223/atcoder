from collections  import deque
n,m,c=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort()
a=deque(a)
b=deque(b)
ans=0

while len(a)>0 and len(b)>0:
    if a[0]>=b[0]:
        a.popleft()
        b.popleft()
        ans+=1
    else:
        a.popleft()

print(ans*c)