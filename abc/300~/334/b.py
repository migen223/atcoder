
a,m,l,r=map(int,input().split())
a+=m*10**19
l+=m*10**19
r+=m*10**19


if l!=r:
    ans=0
    if (l-a)%m==0:
        ans+=1
        kl=(l-a)//m
    else:
        kl=(l-a)//m+1
    
    kr=(r-a)//m
    if a+kl*m>r or a+kr*m<l:
        print(0)
    else:
        print(kr-kl+1)
        
    
    """
    if (l-a)%m==0:
        kl=(l-a)//m
    else:
        kl=(l-a)//m
    if (r-a)%m==0:
        kr=(r-a)//m
    else:
        kr=(r-a)//m
        for i in range(-5,5):
            if (a+(kr+i)*m>r):
                kl=kl+i-1
                break
    print(kl,kr)
    print(max(kr-kl+1,0))"""
    
else:
    if (l-a)%m==0:
        print(1)
    else:
        print(0)