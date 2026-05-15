from collections import Counter
n=int(input())
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
    res=[]
    c=Counter(a)
    for i in c:
        if c[i]%2==1:
            res.append(i)
    if len(res)==0:
        return (1)
    res.sort()
    return tuple(res)

dic={}
zero=0
for i in range(n):
    if a[i]!=0:
        pf=prime_factorize(a[i])
        #print(pf)
        if pf in dic:
            dic[pf]+=1
        else:
            dic[pf]=1
    else:
        zero+=1
#print(dic)
ans=0
for i in range(zero):
    ans+=(n-i-1)

for i in dic :
    if dic[i]>=2:
        ans+=(dic[i]*(dic[i]-1))//2
print(ans)

