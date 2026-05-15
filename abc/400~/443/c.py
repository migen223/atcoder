from bisect import bisect_left
n,t=map(int,input().split())
a=list(map(int,input().split()))
a.append(t)
ans=a[0]
ne=a[0]+100

while True:
    ind=bisect_left(a,ne)
    if ind==len(a):
        break
    ans+=a[ind]-ne
    ne=a[ind]+100
    #print(ne,ind)

print(ans)

