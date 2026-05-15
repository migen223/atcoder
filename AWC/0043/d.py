
n=int(input())
a=list(map(int,input().split()))
a.sort()
r=[0]
for i in a:
    r.append(r[-1]+i)

ans=0
for i in range(n):
    ans+=(r[-1]-r[i+1])-a[i]*(n-i-1)
print(ans)