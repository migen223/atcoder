
n,m=map(int,input().split())

l1=[0]*m
l2=[0]*m
for _ in range(n):
    a,b=map(int,input().split())
    l1[a-1]+=1
    l2[b-1]+=1

for i in range(m):
    print(l2[i]-l1[i])