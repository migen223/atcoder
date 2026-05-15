
n=int(input())
a=list(map(int,input().split()))

if sum(a)%n!=0:
    print(-1)
else:
    ans=0
    ave=sum(a)//n
    sub=[ave-a[i] for i in range(n)]
    r=[sub[0]]
    for i in range(1,n):
        r.append(r[-1]+sub[i])
    for i in range(n):
        ans+=abs(r[i])
    print(ans)

