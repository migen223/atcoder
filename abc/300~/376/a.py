n,c=map(int,input().split())
t=list(map(int,input().split()))
ans=1
mae=t[0]
for i in range(1,n):
    if t[i]-mae>=c:
        ans+=1
        mae=t[i]
print(ans)