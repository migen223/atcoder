
n,m=map(int,input().split())
a=list(map(int,input().split()))

def prime_factorize(n):#素因数分解 返り値はリスト Counterに渡すと良い感じになる
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

se=set()
for i in range(n):
    l=prime_factorize(a[i])
    for j in range(len(l)):
        se.add(l[j])

ans=[]
for i in range(1,m+1):
    f=0
    for j in se:
        if i%j==0:
            f+=1
            break
    if f==0:
        ans.append(i)

print(len(ans))
for i in range(len(ans)):
    print(ans[i])


