import sys
n,m=map(int,input().split())
x=list(map(int,input().split()))
a=list(map(int,input().split()))
if sum(a)!=n:
    print(-1)
else:
    dic={}
    for i in range(m):
        dic[x[i]]=a[i]
    x.sort()
    if x[0]!=1:
        print(-1)
        sys.exit()
    if x[-1]!=n:
        x.append(n)
        dic[n]=-1
    ans=0
    for i in range(m):
        if x[i]==n:
            if dic[x[i]]==1:
                break
            else:
                print(-1)
                sys.exit()
        else:
            
            if dic[x[i]]>=x[i+1]-x[i]:
                N=x[i+1]-x[i]
                a0=dic[x[i]]-1
                ans+=(N*(2*a0-(N-1)))//2
                dic[x[i+1]]+=dic[x[i]]-(x[i+1]-x[i])
            else:
                print(-1)
                sys.exit()
    print(ans)

    
