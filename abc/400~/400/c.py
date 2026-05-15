from math import sqrt
n=int(input())

a=0
while 2**a<=n:
    a+=1
a-=1
ans=0

for i in range(1,a+1):
    b2=n//(2**i)
    b=int(sqrt(b2))
    for j in range(-1000,1000):
        if (b+j)**2<b2<(b+j+1)**2:
            b=b+j
            break

    if b%2==0:
        ans+=b//2
    else:
        ans+=b//2+1
print(ans)
