#解説AC
n,m=map(int,input().split())
a=list(map(int,input().split()))

ruiseki=[0]
for i in range(n):
    ruiseki.append(ruiseki[-1]+a[i])

now=0
for i in range(m):
    now+=(i+1)*a[i]

ans=now
for i in range(n-m):
    now+=-(ruiseki[i+m]-ruiseki[i])+m*a[i+m]
    #print(now)
    ans=max(now,ans)
print(ans)
