n,m,k=map(int,input().split())
people=[0]*n
f=0
for i in range(k):
    a,b=map(int,input().split())
    people[a-1]+=1
    if people[a-1]==m:
        print(a,end=" ")
        f+=1
print()


