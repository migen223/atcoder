from bisect import bisect_left
def eratosthenes(n):
    is_prime = ([False, True] * (n//2+1))[0: n+1]
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, n+1, 2):
        if not(is_prime[i]):
            continue
        if i*i > n:
            break
        for k in range(i*i, n+1, i):
            is_prime[k] = False
    return is_prime

q=int(input())

pl=eratosthenes(10**5+1)
l=[]
for i in range(10**5+1):
    if pl[i]:
        l.append(i)

ansl=[]
for p in l:
    #print((p+1)//2)
    if pl[(p+1)//2]:
        ansl.append(p)
#print(ansl)


for i in range(q):
    ans=0
    L,R=map(int,input().split())
    ans+=bisect_left(ansl,R+1)-bisect_left(ansl,L)
    print(ans)
