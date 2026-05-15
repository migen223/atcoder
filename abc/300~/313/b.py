import sys
n,m=map(int,input().split())

people=[0]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    people[b]+=(people[a]-1)

ind=0
count=0
for i in range(1,n+1):
    if people[i]==0:
        count+=1
        ind=i
if count>=2:
    print(-1)
else:
    print(ind)


