from itertools import product
n,k=map(int,input().split())
r=list(map(int,input().split()))
ansl=[]
nl=[i for i in range(1,max(r)+1)]
for i in product(nl,repeat=n):
    l=list(i)

    count=0
    if sum(l)%k==0:
        for j in range(n):
            if l[j]<=r[j]:
                count+=1
        if count==n:
            ansl.append(l)
#print(ansl)
ansl.sort()
for i in range(len(ansl)):
    print(*ansl[i])