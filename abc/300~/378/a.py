a=list(map(int,input().split()))
l=[0,0,0,0,0]
for i in a:
    l[i]+=1
ans=0
for i in l:
    if i==2 or i==3:
        ans+=1
    elif i==4:
        ans=2
print(ans)