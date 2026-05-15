
n,m=map(int,input().split())

ans=0
se=set()
for i in range(m):
    r,c=map(int,input().split())
    now=set([(r,c),(r,c+1),(r+1,c),(r+1,c+1)])
    if len(now&se)==0:
        ans+=1
        for j in now:
            se.add(j)
print(ans)