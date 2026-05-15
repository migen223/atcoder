from math import gcd
t=int(input())

for _ in range(t):
    n,d,k=map(int,input().split())
    if gcd(n,d)==1:
        print((d*(k-1))%n)
    else:
        g=gcd(n,d)
        ofs=(k-1)//(n//g)
        #print("ofs",ofs,n,d,k)
        print(((k-1)*d+ofs)%n)
