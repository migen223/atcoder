

n,k,x=map(int,input().split())
a=list(map(int,input().split()))

over=0

ans=sum(a)

for i in range(n):
    over+=a[i]//x
    a[i]-=(a[i]//x)*x 
a.sort(reverse=True)
ruiseki=[a[0]]
for i in range(1,n):
    ruiseki.append(ruiseki[-1]+a[i])
if k>over:
    k-=over
    if k<n:
        ans-=over*x
        ans-=ruiseki[k-1]
    else:
        ans=0
elif k<=over:
    ans-=k*x



print(ans)