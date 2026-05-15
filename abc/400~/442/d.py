
n,q=map(int,input().split())
a=list(map(int,input().split()))
r=[a[0]]
for i in range(1,n):
    r.append(r[-1]+a[i])
r.insert(0,0)
r.append(10**32)
#print(r)
for _ in range(q):
    que=list(map(int,input().split()))
    
    if que[0]==1:
        x=que[1]
        r[x]+=a[x]-a[x-1]
        i=a[x-1]
        a[x-1]=a[x]
        a[x]=i
        
        """
        if a[x]>=a[x+1]:
            r[x]-=abs(a[x]-a[x+1])
        else:
            r[x]+=abs(a[x]-a[x+1])"""
    else:
        left,right=que[1],que[2]
        #print("ans",r[right]-r[left-1])
        print(r[right]-r[left-1])
   # print("r",r)
    #print("a",a)