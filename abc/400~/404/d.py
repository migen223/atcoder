from itertools import product
n,m=map(int,input().split())
c=list(map(int,input().split()))

def check(l):
    count=0
    for i in range(len(l)):
        if l[i]<2:
            return False
    return True
            

animals={}
for i in range(n):
    animals[i]=[]

for i in range(m):
    a=list(map(int,input().split()))
    k=a.pop(0)
    for j in range(k):
        animals[a[j]-1].append(i)
#print(animals)

ans=10**19
for p in product(range(3),repeat=n):
    animal=[0]*m
    now=0
    #print(p)
    for i in range(n):
        if p[i]!=0:
            for j in range(len(animals[i])):
                animal[animals[i][j]]+=p[i]
            now+=p[i]*c[i]
        if check(animal):
            ans=min(ans,now)
            #print(now)
            break
print(ans)
        
