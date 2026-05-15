import sys
n,s=map(int,input().split())
a=list(map(int,input().split()))

su=sum(a)
mi=min(a)
if mi>s:
    print("No")
else:
    if s%su==0:
        print("Yes")
        sys.exit()
    for i in range(n):
        if a[i]==s:
            print("Yes")
            sys.exit()
    r=[a[0]]
    r_rev=[a[-1]]
    for i in range(1,n-1):
        r.append(r[-1]+a[i])
        r_rev.append(r_rev[-1]+a[-1-i])
    r=set(r)
    r_rev=set(r_rev)
    syou=s//su
    mod1=s-su*syou
    mod2=s-su*(syou-1)
    if mod1 in r or mod1 in r_rev or mod2 in r or mod2 in r_rev:
        print("Yes")
        sys.exit()
    else:
        for i in r:
            if mod1-i in r_rev or mod2-i in r_rev:
                print("Yes")
                sys.exit()
        print("No")



