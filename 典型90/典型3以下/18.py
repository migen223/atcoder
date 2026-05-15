from math import cos,sin,pi,sqrt,acos,degrees
t=int(input())
l,x,y=map(int,input().split())
q=int(input())
for i in range(q):
    e=int(input())
    y1=-(l/2)*cos(2*pi*e/t-pi/2)
    z1=(l/2)*sin(2*pi*e/t-pi/2)+l/2
    ab=sqrt(x*x+(y1-y)**2+z1*z1)
    ac=sqrt(x*x+(y1-y)**2)
    rad=acos(ac/ab)
    ans=degrees(rad)
    print(ans)
