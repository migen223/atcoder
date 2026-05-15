from math import sqrt,pow
a,b=map(int,input().split())
x=int(((a/(2*b))**(2/3)))
if x>0:
    ans=10**18
    for i in range(10):
        ans=min(ans,a/sqrt(x+i+1)+(x+i)*b)
    for i in range(10):
        if x-i>0:
            ans=min(ans,a/sqrt(x-i+1)+(x-i)*b)
    print(f"{ans:.20f}")
else:
    print(a)