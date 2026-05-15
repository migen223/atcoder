
n=int(input())
def eratosthenes2(n):
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

pl=eratosthenes2(1000000)
p=[]
pa=[]
pb=[]
for i in range(10001):
    if pl[i]:
        pb.append(i)
for i in range(1001):
    if pl[i]:
        pa.append(i)
for i in range(1000001):
    if pl[i]:
        p.append(i)
        
while pa[-1]**2*pa[-2]*pa[-3]**2>10**12:
    pa.pop()
while pb[-1]**2*pb[-2]>10**12:
    pb.pop()


while 6*p[-1]>10**12:
    p.pop()


ans=0

for i in range(len(pa)):
    for j in range(i+1,len(pb)):
        if pa[i]**2*pb[j]>n:
            break
        for k in range(j+1,len(p)):
            if pa[i]**2*pb[j]*p[k]**2>n:
                break
            else:
                ans+=1
print(ans)
        
