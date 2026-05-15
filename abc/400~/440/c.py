
t=int(input())

for _ in range(t):
    n,w=map(int,input().split())
    c=list(map(int,input().split()))
    if n>w:
        r=[0]
        for i in range(n):
            r.append(r[-1]+c[i])

        ans=10**32
        s=r[-1]
        for i in range(w):
            res=0
            j=0
            while i+w*(j+1)<n:
                j+=1
                if j%2==1:
                    res+=r[i+w*j]-r[i+w*(j-1)]
            if j%2==0:
                res+=r[-1]-r[i+w*j]
            #print("res=",res,s-res,i,j)
            ans=min(res,s-res,ans)
        print(ans)
        #print("ans=",ans)
    else:
        print(0)

        



