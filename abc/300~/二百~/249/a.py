
a,b,c,d,e,f,x=map(int,input().split())

x2=x
t=0
t+=(x//(a+c)*a*b)
x-=(x//(a+c))*(a+c)

if 0<=x<=a:
    t+=b*x
else:
    t+=a*b

ao=0
ao+=(x2//(d+f)*d*e)
x2-=(x2//(d+f))*(d+f)
if 0<=x2<=d:
    ao+=e*x2
else:
    ao+=e*d


if ao>t:
    print("Aoki")
elif ao<t:
    print("Takahashi")
else:
    print("Draw")