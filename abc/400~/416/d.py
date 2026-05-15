t=int(input())


for _ in range(t):
    n,m=map(int,input().split())
    a=list(map(int ,input().split()))
    b=list(map(int ,input().split()))
    c=[m-b[i] for i in range(n)]

    c.sort()
    b.sort(reverse=True)
    a.sort()

    ans=0
    r=0
    suma=0
    sumb=0

    for i in range(n):
        #print(f"r={r}")
        if r==n:
            sumb+=b[i]
        
        
        else:
            while c[i]>a[r]:
                
                suma+=a[r]
                
                #print(f"suma={suma},ar={a[r]},ci={c[i]}")
                r+=1
                if r==n:
                    break
            if r==n:
                sumb+=b[i]
            else:
                ans+=a[r]-c[i]
                r+=1
        #print(ans,suma,sumb)
    print(ans+suma+sumb)


    """
    print()
    print(sorted(a))
    print(sorted(b))
    print(sorted(c)) 
    print()
    """

    