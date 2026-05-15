from collections import Counter
import sys
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
    return Counter(a)

ans=0
min2=10**6
min3=10**6
k=a[0]
while k%2==0 or k%3==0:
    if k%2==0:
        k//=2
    else:
        k//=3
    #print(k)

for i in range(n):
    if a[i]!=1:
        c=prime_factorize(a[i])
        #print(c)
        now=1
        for j in c:
            
            if j==2:
                min2=min(min2,c[j])
            elif j==3:
                min3=min(min3,c[j])
            else:
                now*=j**c[j]
        if k!=now:
            print(-1)
            sys.exit()
        if 2 not in c:
            min2=0
        if 3 not in c:
            min3=0
    else:
        min2=0
        min3=0
two=0
three=0
for i in range(n):
    if a[i]!=1:
        c=prime_factorize(a[i])
        for j in c:
            if j==2:
                two+=c[j]-min2
            if j==3:
                three+=c[j]-min3

#print(min2,min3)
print(two+three)