
n,m=map(int,input().split())
a=list(map(int,input().split()))
c=list(map(int,input().split()))
a.reverse()
c.reverse()
#print(a,c)
b=[0]*(m+1)
for i in range(m+1):
    b[i]=c[i]//a[0]
    for j in range(n+1):
        c[i+j]-=a[j]*b[i]

b.reverse()
print(*b)