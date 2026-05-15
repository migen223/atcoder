from math import sqrt
d=int(input())
ans=10**12
for x in range(10**6+1):
    y=[int(sqrt(abs(d-x*x))),int(sqrt(abs(d-x*x)))+1]
    an=min(abs(x*x+y[0]*y[0]-d),abs(x*x+y[1]*y[1]-d))
    ans=min(an,ans)
print(ans)
