n,k=map(int,input().split())
a=list(map(int,input().split()))
nokori=k
ans=0
for i in range(n):
    
    if nokori<a[i]:
        nokori=k-a[i]
        ans+=1
    else:
        nokori-=a[i]
    #print(ans,a[i],nokori)
if nokori!=k:
    ans+=1
print(ans)