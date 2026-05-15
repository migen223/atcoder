
n=int(input())
a=list(map(int,input().split()))
ans=0
for i in range(n):
    now=0
    mi=a[i]
    count=1
    for j in range(i,n):
        
        if mi<=a[j]:
            ans=max(ans,mi*(count))
        else:
            mi=a[j]
            ans=max(ans,mi*(count))
        count+=1
    ans=max(ans,now)
print(ans)


