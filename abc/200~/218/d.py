
n=int(input())

points=[tuple(map(int,input().split())) for i in range(n)]

sep=set(points)

ans=0
for i in range(n-1):
    for j in range(i+1,n):
        if points[i][0]!=points[j][0] and points[i][1]!=points[j][1]:
            if (points[i][0],points[j][1]) in sep and (points[j][0],points[i][1]) in sep:
                ans+=1
                

print(ans//2)