
n,m=map(int,input().split())

change=[]
ab=[]

for i in range(m):
    a,b=map(int,input().split())
    ab.append((a,b))
ab.sort(key=lambda x:x[0])
for i in range(m):
    change.append((ab[i][0],ab[i][1],ab[i][0]-ab[i][1]))
change.sort(key=lambda x:x[2])
#print(change)
ans=0
for i in range(m):
    a=change[i][0]
    b=change[i][1]
    k=0
    if change[i][0]<=n:
        k=(n-a)//(a-b)+1
        ans+=k
        n-=k*(a-b)
    #print(n,ans,k)
print(ans)
