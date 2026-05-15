
n=int(input())
a=list(map(int,input().split()))

a.sort()
ans=0
tail=a[0]
for i in range(1,n):
    if a[i]==tail+1:
        tail+=1
    else:
        tail=a[i]
        ans+=1

print(ans+1)