from fractions import Fraction
import sys
x1,y1,x2,y2=map(int,input().split())

if y1!=y2:
    m=-Fraction(x1-x2,y1-y2)
    mx=Fraction(x1+x2,2)
    my=Fraction(y1+y2,2)
    c=my-mx*m


    def f(x):
        return m*x+c

    deno=m.denominator

    xint=(x1+x2)//2

    for i in range(-5,6):
        x=xint+i
        d1=(x1-x)**2+(y1-f(x))**2
        d2=(x2-x)**2+(y2-f(x))**2
        #print(x,f(x))
        #print(d1,d2)
        if d1==d2==5:
            print("Yes")
            sys.exit()
    print("No")
else:
    if (x1+x2)%2==0:
        x=(x1+x2)//2
        for i in range(-5,6):
            y=y1+i
            if (x1-x)**2+(y1-y)**2==(x2-x)**2+(y2-y)**2==5:
                print("Yes")
                sys.exit()
    print("No")




