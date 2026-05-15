t=int(input())


for i in range(t):
    ans=0
    n=int(input())
    a=list(map(int,input().split()))
    for j in range(n):
        if a[j]%2==1:
            ans+=1
    print(ans)
