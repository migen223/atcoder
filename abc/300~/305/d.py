from bisect import *
n=int(input())
a=list(map(int,input().split()))
q=int(input())

sleep=[]
stime=[0]
for i in  range(n-1):
    sleep.append((a[i],a[i+1]))
    if i%2==1:
        stime.append(stime[-1]+a[i+1]-a[i])
    else:
        stime.append(stime[-1])
stime.pop(0)
#print(sleep)
#print(stime)
for _ in range(q):
    ans=0
    l,r=map(int,input().split())
    left=bisect_right(sleep,l,key=lambda x:x[0])-1
    right=bisect_right(sleep,r,key=lambda x:x[0])-1
    #print(" ",left,right,"sbkk")
    if left==right and left%2==1:
        ans+=r-l
    else:
        if left%2==1:
            ans+=sleep[left][1]-l
        if right%2==1:
            ans+=r-sleep[right][0]
        if right-left>=2:
            ans+=stime[right-1]-stime[left]
    print(ans)
    #print(f"ans={ans}")



