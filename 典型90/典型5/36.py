
n,Q=map(int,input().split())

point=[]
for i in range(n):
    x,y=map(int,input().split())
    point.append((x-y,x+y))

xmin=min(point)[0]
xmax=max(point)[0]
ymin=min(point,key=lambda x:x[1])[1]
ymax=max(point,key=lambda x:x[1])[1]
#print(point)

for i in range(Q):
    q=int(input())
    x,y=point[q-1]
    print(max(abs(x-xmin),abs(x-xmax),abs(y-ymin),abs(y-ymax)))
