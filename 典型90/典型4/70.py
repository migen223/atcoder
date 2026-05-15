
n=int(input())

xs=[]
ys=[]

for i in range(n):
    x,y=map(int,input().split())
    xs.append(x)
    ys.append(y)
xs.sort()
ys.sort()

xans=xs[n//2]
yans=ys[n//2]

ans=0
for i in range(n):
    ans+=abs(xans-xs[i])
    ans+=abs(yans-ys[i])
print(ans)
