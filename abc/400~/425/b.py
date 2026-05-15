import sys

n=int(input())
a=list(map(int,input().split()))
other=[]
if sum(a)==-n:
    print("Yes")
    print(*[i for i in range(1,n+1)])
else:
    for i in range(n):
        if a[i]!=-1:
            if a[i] in other:
                print("No")
                sys.exit()
            else:
                other.append(a[i])

    ans=[0]*n
    nokori=[i for i in range(1,n+1)]
    if max(other)>n:
        print("No")
    else:
        for i in range(n):
            if a[i]!=-1:
                ans[i]=a[i]
                nokori.remove(a[i])
        for i in range(n):
            if ans[i]==0:
                ans[i]=nokori.pop()
        print("Yes")
        print(*ans)
