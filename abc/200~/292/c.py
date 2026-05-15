from collections import Counter
def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

def calc(dic):
    ans=1
    for i in dic:
        ans*=dic[i]+1
    return ans

n=int(input())
ans=0
for i in range(1,n//2+1):
    if n-i==i:
        c1=Counter(prime_factorize(i))
        ans+=calc(c1)**2
    else:
        c1=Counter(prime_factorize(i))
        c2=Counter(prime_factorize(n-i))
        ans+=2*calc(c1)*calc(c2)
print(ans)



