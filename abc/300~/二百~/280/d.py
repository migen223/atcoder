from collections import Counter
k=int(input())
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

c=Counter(prime_factorize(k))
ans=0

for prime in c:
    count=0
    num=prime
    while count<c[prime]:
        #print(num,count)
        num2=num
        while num2%prime==0:
            num2=num2//prime
            count+=1
        #print(count,"ibgrbius")
        if count>=c[prime]:
            break
        num+=prime
    #print(num)
    ans=max(ans,num)
print(ans)

