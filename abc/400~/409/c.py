n,l=map(int,input().split())
point=list(map(int ,input().split()))
llist=[0]*l
s=0
llist[0]=1
ans=0
for i in point:
    s+=i
    llist[s%l]+=1
if l%3==0:
    th=l//3
    for i in range(l//3):
        ans+=llist[i]*llist[i+th]*llist[i+2*th]
    print(ans)
else:
    print(0)
