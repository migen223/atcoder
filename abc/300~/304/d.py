from bisect import bisect_left
w,h=map(int,input().split())
n=int(input())

point=[]
for i in range(n):
    p,q=map(int,input().split())
    point.append((p,q))

an=int(input())
a=list(map(int,input().split()))
a.insert(0,0)
a.append(w)
bn=int(input())
b=list(map(int,input().split()))
b.insert(0,0)
b.append(h)

ans={}
for p,q in point:
    xind=bisect_left(a,p)
    yind=bisect_left(b,q)
    if (xind,yind) not in ans:
        ans[(xind,yind)]=1
    else:
        ans[(xind,yind)]+=1

mi=10**18
ma=1
if len(ans)<(an+1)*(bn+1):
    mi=0
else:
    for i in ans:
        mi=min(mi,ans[i])

for i in ans:
    ma=max(ma,ans[i])
print(mi,ma)
