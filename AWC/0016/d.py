from bisect import bisect_right
n,k,q=map(int,input().split())
a=list(map(int,input().split()))
cum=[0]
for i in range(n):
    cum.append(cum[-1]+a[i])

stop=[]
for i in range(1,1+n):
    ind=bisect_right(cum,k+cum[i-1])
    stop.append(min(n,ind))
#print(stop)

sc=[0]
for i in range(len(stop)):
    sc.append(sc[-1]+stop[i])
#print(sc)
for i in range(q):
    l,r=map(int,input().split())
    print(sc[r]-sc[l-1])
