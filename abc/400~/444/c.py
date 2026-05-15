from collections import Counter
n=int(input())
a=list(map(int,input().split()))
a.sort()
c=Counter(a)

if len(c)==1:
    if n%2==0:
        print(a[0],2*a[0])
    else:
        print(a[0])
else:
    ans=[]
    ma=a[-1]
    f=0
    for i in c:
        if i!=ma:
            if 2*i!=ma:

                if i in c and ma-i in c:
                    if c[i]==c[ma-i]:
                        f+=1
            else:
                if c[i]%2==0:
                    f+=1
    if len(c)-1==f:
        ans.append(ma)
    
    f=0
    ma=a[-1]+a[0]
    for i in c:
        if 2*i!=ma:
            if i in c and ma-i in c:
                if c[i]==c[ma-i]:
                    f+=1
        else:
            if c[i]%2==0:
                f+=1
    if len(c)==f:
        ans.append(ma)
    print(*ans)
