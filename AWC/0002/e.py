from itertools import product
n,s=map(int,input().split())
a=list(map(int,input().split()))

left={}
right={}
for l in product([0,1],repeat=n//2):
    res=0
    for i in range(n//2):
        res+=l[i]*a[i]
    if res in left:
        left[res]+=1
    else:
        left[res]=1

for r in product([0,1],repeat=n-n//2):
    res=0
    for i in range(n-n//2):
        res+=r[i]*a[-1-i]
    if res in right:
        right[res]+=1
    else:
        right[res]=1

#print(left)
#print(right)
ans=0
for l in left:
    if s-l in right:
        ans+=left[l]*right[s-l]
print(ans)