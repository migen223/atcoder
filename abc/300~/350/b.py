n,q=map(int,input().split())
teeth=[1]*n
t=list(map(int,input().split()))
ans=n
for i in range(q):
    if teeth[t[i]-1]==1:
        teeth[t[i]-1]=0
        ans-=1
    else:
        teeth[t[i]-1]=1
        ans+=1
print(ans)