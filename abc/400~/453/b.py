
t,x=map(int,input().split())
a=list(map(int,input().split()))

now=a[0]
ans=[(0,now)]
for i in range(1,t+1):
    #print(ans[-1][-1],a[i])
    if abs(ans[-1][-1]-a[i])>=x:
        ans.append((i,a[i]))
    

for i in range(len(ans)):
    print(*ans[i])