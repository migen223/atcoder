n,m=map(int,input().split())
ans=[]
a=list(map(int,input().split()))
for i in range(1,n+1):
    if i in a:
        continue
    ans.append(i)
if len(ans)==0:
    print(0)
else:
    print(len(ans))
    print(*ans)