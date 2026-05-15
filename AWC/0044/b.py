
n,q=map(int,input().split())
a=list(map(int,input().split()))
rl=[0]
for i in range(n):
    rl.append(rl[-1]+a[i])

for i in range(q):
    l,r=map(int,input().split())
    print(rl[r]-rl[l-1])
