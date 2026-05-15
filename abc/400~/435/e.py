from sortedcontainers import SortedSet

n,q=map(int,input().split())
s=SortedSet([(n,1)])
ans=n
for _ in range(q):
    l,r=map(int,input().split())
    i=s.bisect_left((l,-1))
    leng=len(s)
    delete=[]
    add=[]
    while i<leng:
        ri,li=s[i]
        if l<=li<=r<=ri:
            delete.append((ri,li))
            add.append((ri,r+1))
        elif li<=l<=r<=ri:
            delete.append((ri,li))
            add.append((l-1,li))
            add.append((ri,r+1))
        elif li<=l<=ri<=r:
            delete.append((ri,li))
            add.append((l-1,li))
        elif l<=li<=ri<=r:
            delete.append((ri,li))
        elif r<li:
            break
        i+=1
    #print("disc",delete,"\nadd",add)
    for d in delete:
        ans-=d[0]-d[1]+1
        #print("discard",d)
        s.discard(d)
    for ad in add:
        ans+=ad[0]-ad[1]+1
        s.add(ad)
    #print(s)
    print(ans)
    
