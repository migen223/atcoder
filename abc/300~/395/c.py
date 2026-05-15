n=int(input())
a=list(map(int,input().split()))
numberlist=[[0,1000000] for i in range(1000000+1)]
for i in range(n):
    if numberlist[a[i]][0]!=0:
        numberlist[a[i]][1]=min(numberlist[a[i]][1],i+1-numberlist[a[i]][0]+1)
    numberlist[a[i]][0]=i+1
ans=1000000000
for i in numberlist:
    ans=min(ans,i[1])
if ans==1000000:
    print(-1)
else:
    print(ans)