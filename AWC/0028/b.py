
n,l,r=map(int,input().split())

t=list(map(int,input().split()))
left=0
right=0
ans=0
now=0
for i in range(n):
    if l<=t[i]<=r:
        now+=1
    else:
        now=0
   # print(now,t[i])
    ans=max(now,ans)
ans=max(now,ans)
print(ans)