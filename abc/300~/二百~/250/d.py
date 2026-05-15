from bisect import bisect_right
def get_prime(n):
    sieve = [True] * (n + 1) 
    i = 2
    while i * i <= n: 
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
        i += 1
    return [i for i in range(2, n + 1) if sieve[i]]  
n=int(input())

ps=get_prime(10**6+1)


ans=0
for i in range(1,len(ps)):
    q=ps[i]
    p=n/(q**3)
    ind=bisect_right(ps,p,hi=i)
    ans+=ind

print(ans)





