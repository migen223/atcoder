n=int(input())
points=[]
for i in range(n):
    x,y=map(int,input().split())
    points.append([x,y])
for i in range(n):
    ma=0
    ind=0
    for j in range(n):
        if ma<(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2:
            ma=(points[i][0]-points[j][0])**2+(points[i][1]-points[j][1])**2
            ind=j
    print(ind+1)
