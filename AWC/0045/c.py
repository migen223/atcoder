
n,q=map(int,input().split())
imos=[0]*(n+1)
for i in range(q):
    l,r,c=map(lambda x:int(x)-1,input().split())
    c+=1
    imos[l]+=c
    imos[r+1]-=c

for i in range(1,n):
    imos[i]+=imos[i-1]

for i in range(n):
    print(imos[i],end=" ")
print()