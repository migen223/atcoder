n,q=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
mi=0
for i in range(n):
    mi+=min(a[i],b[i])
for _ in range(q):
    l=input().split()
    c=l[0]
    x=int(l[1])
    v=int(l[2])
    bef=min(a[x-1],b[x-1])
    if c=="A":
        aft=min(v,b[x-1])
        a[x-1]=v
    else:
        aft=min(a[x-1],v)
        b[x-1]=v
    mi+=aft-bef
    print(mi)

