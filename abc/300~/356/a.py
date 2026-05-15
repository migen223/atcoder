n,l,r=map(int,input().split())
a=[i for i in range(1,n+1)]
ans=[]
for i in range(l-1):
    ans.append(a[i])

for i in range(r,l-1,-1):
    ans.append(i)
for i in range(n-r):
    ans.append(a[r+i])

print(*ans)
