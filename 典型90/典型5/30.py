def eratosthenes(n):
    is_prime = ([False, True] * (n//2+1))[0: n+1]
    is_prime[1] = False
    for i in range(3, n+1, 2):
        if not(is_prime[i]):
            continue
        if i*i > n:
            break
        for k in range(i*i, n+1, i):
            is_prime[k] = False
    return is_prime

n,k=map(int,input().split())

plb=eratosthenes(n)
pl=[2]
for i in range(3,n):
    if plb[i]:
        pl.append(i)
#print(pl)

ansl=[0]*(n+1)
for p in pl:
    now=p
    while 1<=now<=n:
        ansl[now]+=1
        now+=p
#print(ansl)
ans=0
for i in range(1,n+1):
    if ansl[i]>=k:
        ans+=1

print(ans)
