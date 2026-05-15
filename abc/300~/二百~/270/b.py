
x,y,z=map(int,input().split())
if x<0:
    if x<y<0:
        if y<z<0:
            print(-x)
        elif z<y:
            print(-1)
        else:
            print(-x+2*z)
    else:
        print(-x)
else:
    if 0<y<x:
        if 0<z<y:
            print(x)
        elif z>y:
            print(-1)
        else:
            print(x-2*z)
    else:
        print(x)
