from math import sqrt
n=int(input())

point=[list(map(int,input().split())) for i in range(n)]


leng=[]
for i in range(n-1):
    for j in range(i+1,n):
        l=(point[i][0]-point[j][0])**2+(point[i][1]-point[j][1])**2
        leng.append(l)

print(sqrt(max(leng)))



