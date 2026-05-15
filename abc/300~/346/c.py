n,k=map(int,input().split())
a=list(map(int,input().split()))
ase=set()
for i in range(n):
    if a[i]<=k:
        ase.add(a[i])
ans=int(k*(k+1)/2)
minus=0
for i in ase:
    minus+=i
#print(minus)

print(ans-minus)