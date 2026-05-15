n,x,y=map(int,input().split())
a=list(map(int,input().split()))#sw
b=list(map(int,input().split()))#sl
salt=0
sweet=0
a.sort(reverse=True)
b.sort(reverse=True)
count=0
ans=n
for i in range(n):
    salt+=b[i]
    count+=1
    if salt>y:
        ans=min(count,ans)
        break
count2=0
for i in range(n):
    sweet+=a[i]
    count2+=1
    if sweet>x:
        ans=min(ans,count2)
        break
print(ans)
