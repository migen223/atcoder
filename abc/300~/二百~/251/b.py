from itertools import combinations
n,w=map(int,input().split())
a=list(map(int,input().split()))
se1=set(a)
se2=set()
se3=set()


for c in combinations(range(0,n),2):
    se2.add(a[c[0]]+a[c[1]])
for c in combinations(range(0,n),3):
    se3.add(a[c[0]]+a[c[1]]+a[c[2]])
ans=0

for i in range(1,w+1):
    if i in se1 or i in se2 or i in se3:
        ans+=1
print(ans)





