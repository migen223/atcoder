
n,t=map(int,input().split())
ans=0
for i in range(n):
    a,c=map(int,input().split())
    ans+=max(0,(t-a)*c)

print(ans)