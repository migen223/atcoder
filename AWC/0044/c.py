
n,m=map(int,input().split())

imos=[0]*(n+1)
for i in range(m):
    l,r=map(lambda x:int(x)-1,input().split())
    imos[l]+=1
    imos[r+1]-=1

for i in range(1,n):
    imos[i]+=imos[i-1]

imos.pop()
print(*imos)
