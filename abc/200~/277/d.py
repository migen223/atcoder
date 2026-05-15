
n,m=map(int,input().split())
a=list(map(int,input().split()))

s=sum(a)
a.sort()
a2=[a[i%n] for i in range(2*n)]
#print(a2)

nowind=0
sec=[]
ans=0
if n!=1:
    while nowind<=n-1:
        now=a[nowind]
        count=1
        while count<=n :
            #print(nowind,now,count)
            if a2[nowind+1]==a2[nowind] or a2[nowind+1]==(a2[nowind]+1)%m:
                count+=1
                nowind+=1
                now+=a2[nowind]
                if count==n:
                    break
            else:
                nowind+=1
                break
        ans=max(ans,now)
        #print(nowind,now,count)
    print(s-ans)
else:
    print(0)
