import sys
x0,y0=map(int,input().split())
x1,y1=map(int,input().split())
x2,y2=map(int,input().split())

if ((x0-x1)**2+(y0-y1)**2+(x2-x1)**2+(y2-y1)**2)==(x0-x2)**2+(y0-y2)**2:
    print("Yes")
    sys.exit()
if ((x0-x1)**2+(y0-y1)**2+(x2-x0)**2+(y2-y0)**2)==(x1-x2)**2+(y1-y2)**2:
    print("Yes")
    sys.exit()
if ((x0-x2)**2+(y0-y2)**2+(x2-x1)**2+(y2-y1)**2)==(x0-x1)**2+(y0-y1)**2:
    print("Yes")
    sys.exit()
print("No")