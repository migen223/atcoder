
n=int(input())

point=set([10**32])
dic={}
tower=[]
for i in range(n):
    x,l,r,c=map(int,input().split())
    tower.append((x,l,r,c))
    point.add(x-l)
    point.add(x+r)

point=list(point)
point.sort()

for i in range(len(point)):
    dic[point[i]]=i

imos=[0]*(len(point))
for i in range(n):
    x,l,r,c=tower[i]
    imos[dic[x-l]]+=c
    imos[dic[x+r]+1]-=c

for i in range(1,len(imos)):
    imos[i]+=imos[i-1]

ans=0
for i in range(len(imos)-1):
    ans=max(ans,imos[i])

print(ans)