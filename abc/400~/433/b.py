
n=int(input())
a=list(map(int,input().split()))

for i in range(n):
    ans=-1
    for j in range(i):
        #print(a[i],a[j])
        if a[i]<a[j]:
            ans=j+1
    print(ans)