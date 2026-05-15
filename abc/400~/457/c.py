from bisect import bisect_left
n,k=map(int,input().split())


ll=[]
al=[[]]
for i in range(n):
    l=list(map(int,input().split()))
    a=l[1:]
    l=l[0]
    al.append(a)
    ll.append(l)

c=list(map(int,input().split()))
r=[0]
for i in range(n):
    r.append(r[-1]+ll[i]*c[i])


ind=bisect_left(r,k)
#print(r,ind,r[ind-1])
#print(al)
print(al[ind][(k-1-r[ind-1])%len(al[ind])])