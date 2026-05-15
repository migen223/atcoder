
p=int(input())

coin=[1]
for i in range(2,11):
    coin.append(coin[-1]*i)

for i in range(10):
    if coin[i]<=p:
        ind=i

ans=0
for i in range(ind,-1,-1):
    while p-coin[i]>=0:
        p-=coin[i]
        ans+=1
print(ans)
    

