n,m=map(int,input().split())
canon=[]

for _ in range(m):
    l,r=map(int,input().split())
    se=[l-1,r]
    canon.append(se)
imos=[0]*n
for i in canon:
    imos[i[0]]+=1
    if i[1]!=n:
        imos[i[1]]-=1
s=0
for i in range(n):
    s+=imos[i]
    imos[i]=s
print(min(imos))
