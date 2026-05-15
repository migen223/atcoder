n=int(input())
a=list(map(int,input().split()))
under=0
for i in a:
    if i<=0:
        under+=1
ans=0
while under<n-1:
    a.sort(reverse=True)
    if a[0]-1<=0:
        under+=1
    if a[1]-1<=0:
        under+=1
    a[0]-=1
    a[1]-=1
    ans+=1
print(ans)