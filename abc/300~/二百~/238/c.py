
n=int(input())
p=998244353

keta=len(str(n))
ans=0

for i in range(1,keta):
    num=10**i-10**(i-1)
    ans+=(((num)*(num+1))//2)%p


num=(n-10**(keta-1)+1)
ans+=(((num)*(num+1))//2)%p

print(ans%p)


