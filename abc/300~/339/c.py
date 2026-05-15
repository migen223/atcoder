n=int(input())
a=list(map(int,input().split()))
mi=10000000000
s=0
for i in range(n):
    s+=a[i]
    mi=min(mi,s)
if mi<0:
    mi*=-1
else:
    mi=0

for i in range(n):
    mi+=a[i]

print(mi)