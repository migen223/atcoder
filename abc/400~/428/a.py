

s,a,b,x=map(int,input().split())
ans=(x//(a+b))*a*s
x-=(x//(a+b))*(a+b)
#print(x)
if 0<=x<=a:
    print(ans+x*s)
else:
    print(ans+a*s)


