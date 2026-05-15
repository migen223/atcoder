
k=int(input())
mod=998244353

ans=0
for a in range(2,k-3):
    for b in range(2,k-1-a):
        c=k-a-b
        #print(a,b,c)
        ans+=(k-max(a,b,c))*(a-1)*(b-1)*(c-1)
        ans%=mod
    
print(ans)