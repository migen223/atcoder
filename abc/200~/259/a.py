
n,m,x,t,d=map(int,input().split())

for i in range(n,m-1,-1):
    if x<=i<=n:
        continue
    else:
        t-=d

print(t)
