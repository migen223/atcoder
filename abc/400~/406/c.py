from bisect import bisect_left
n=int(input())
p=list(map(int,input().split()))

ma=[]
mi=[]

for i in range(1,n-1):
    if p[i-1]<p[i] and p[i]>p[i+1]:
        ma.append(i)
    if p[i-1]>p[i] and p[i]<p[i+1]:
        mi.append(i)

points=[0]
for i in range(len(ma)):
    points.append(ma[i])
for i in range(len(mi)):
    points.append(mi[i])
points.sort()
points.append(n-1)

pair=[]
for i in range(len(ma)):
    ind=bisect_left(mi,ma[i])
    if ind!=len(mi):
        pair.append((ma[i],mi[ind]))
#print(pair)
ans=0
for now in pair:
    left=bisect_left(points,now[0])-1
    right=bisect_left(points,now[1])+1
    ans+=(now[0]-points[left])*(points[right]-now[1])
print(ans)
    

#print(ma,mi)




