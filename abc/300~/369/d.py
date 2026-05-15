n=int(input())
a=list(map(int,input().split()))
dpe=[0]*(n+1)
dpo=[0]*(n+1)
dpo[0]=-10000000000000000000
for i in range(1,n+1):
    dpo[i]=max(dpo[i-1],dpe[i-1]+a[i-1])
    dpe[i]=max(dpe[i-1],dpo[i-1]+2*a[i-1])

print(max(dpe[n],dpo[n]))