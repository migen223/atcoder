import sys
def check(x0,y0,x1,y1):
    if x0*y1-y0*x1>0:
        return True 
    else:
        return False
def origin(x0,y0,x1,y1,x2,y2):
    ans=[x0-x2,y0-y2,x1-x2,y1-y2]
    return ans

ax,ay=map(int,input().split())
bx,by=map(int,input().split())
cx,cy=map(int,input().split())
dx,dy=map(int,input().split())


adc=origin(ax,ay,cx,cy,dx,dy)
dcb=origin(dx,dy,bx,by,cx,cy)
cba=origin(cx,cy,ax,ay,bx,by)
bad=origin(bx,by,dx,dy,ax,ay)

if  not check(adc[0],adc[1],adc[2],adc[3]):
    print("No")
    sys.exit()
if  not check(dcb[0],dcb[1],dcb[2],dcb[3]):
    print("No")
    sys.exit()
if  not check(cba[0],cba[1],cba[2],cba[3]):
    print("No")
    sys.exit()
if  not check(bad[0],bad[1],bad[2],bad[3]):
    print("No")
    sys.exit()
print("Yes")