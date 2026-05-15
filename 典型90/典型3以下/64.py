n,q=map(int,input().split())
a=list(map(int,input().split()))
ans=0
dif=[a[i+1]-a[i] for i in range(n-1)]
for i in range(n-1): 
    ans+=abs(a[i]-a[i+1])
for i in range(1,q+1):
    l,r,v=map(int,input().split()) 
    bef=0
    aft=0
    if l>=2:
        bef+=abs(dif[l-2])
        dif[l-2]+=v
        aft+=abs(dif[l-2])
    if r<n:
        bef+=abs(dif[r-1])
        dif[r-1]-=v
        aft+=abs(dif[r-1])

    ans+=aft-bef
    print(ans)
    


"""
for i in range(n-1):
    ans+=abs(a[i]-a[i+1])
for _ in range(q):
    l,r,v=map(int,input().split()) 
    nv=abs(v)
    if v>=0:
        if l==1 and r!=n:
            if a[r-1]>=a[r]:
                ans+=nv
            else:
                if a[r]-a[r-1]<=nv:
                    ans+=nv+a[r-1]-a[r]
                else:
                    ans-=nv
        elif l!=1 and r==n:
            if a[l-2]<=a[l-1]:
                ans+=nv
            else:
                if a[r-2]-a[r-1]<=nv:
                    ans+=nv+a[r-1]-a[r-2]
                else:
                    ans-=nv
        elif l==1 and r==n:
            print(ans)
            break
        else:
            if a[r-1]>=a[r]:
                ans+=nv
            elif a[r-1]<a[r]:
                if a[r]-a[r-1]<=nv:
                    ans+=nv+a[r-1]-a[r]
                else:
                    ans-=nv
            if a[l-2]<=a[l-1]:
                ans+=nv
            elif a[l-2]>a[l-1]:
                if a[r-2]-a[r-1]<=nv:
                    ans+=nv+a[r-1]-a[r-2]
                else:
                    ans-=nv
    else:
        if l==1 and r!=n:
            if a[r-1]>a[r]:
                if a[r-1]-a[r]<=nv:
                    ans+=nv+a[r]-a[r-1]
                else:
                    ans-=nv
            else:
                ans+=nv
        elif l!=1 and r==n:
            if a[l-2]<a[l-1]:
                if a[l-1]-a[l-2]<=nv:
                    ans+=nv+a[l-2]-a[l-1]
                else:
                    ans-=nv
            else:
                ans+=nv
        elif l==1 and r==n:
            print(ans)
            break
        else:
            if a[r-1]>a[r]:
                if a[r-1]-a[r]<=nv:
                    ans+=nv+a[r]-a[r-1]
                else:
                    ans-=nv
            elif a[r-1]<=a[r]:
                ans+=nv
            if a[l-2]<a[l-1]:
                if a[l-1]-a[l-2]<=nv:
                    ans+=nv+a[l-2]-a[l-1]
                else:
                    ans-=nv
            elif a[l-2]>=a[l-1]:
                ans+=nv
    print(ans)
"""
