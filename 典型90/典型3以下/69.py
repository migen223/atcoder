n,k=map(int,input().split())

if n==1:
    if k==1:
        print(1)
    elif k==2:
        print(2)
    else:
        print(k)
elif n==2:
    if k==1:
        print(0)
    elif k==2:
        print(2)
    else:
        print(k*(k-1))
elif k==1:
    if n==1:
        print(1)
    else:
        print(0)
elif k==2:
    if n==1:
        print(2)
    elif n==2:
        print(2)
    else:
        print(0)
else:
    ans=(k*(k-1))%((10**9)+7)
    p=pow(k-2,n-2,(10**9)+7)
    ans=(ans*p)%((10**9)+7)
    print(ans)