from bisect import bisect_left
n,q=map(int,input().split())
a=list(map(int,input().split()))

a.sort()
ruiseki=[a[0]]
for i in range(1,n):
    ruiseki.append(ruiseki[-1]+a[i])


for i in range(q):
    ans=0
    x=int(input())
    ind=bisect_left(a,x)
    if x<=a[0]:
       # print(1)
        print(ruiseki[-1]-x*n)
    elif x>=a[-1]:
        #print(2)
        print(x*n-ruiseki[-1])
    else:
        #print(3)
        ans+=x*ind-ruiseki[ind-1]
        ans+=ruiseki[-1]-ruiseki[ind-1]-x*(n-ind)
        print(ans)



