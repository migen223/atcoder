n,m=map(int,input().split())
a=list(map(int,input().split()))
nut=[0]*m
for i in range(n):
    x=list(map(int,input().split()))
    for j in range(m):
        nut[j]+=x[j]
count=0
for i in range(m):
    if nut[i]>=a[i]:
        count+=1
if count==m:
    print("Yes")
else:
    print("No")
        