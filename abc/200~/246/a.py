import sys

x1,y1=map(int,input().split())
x2,y2=map(int,input().split())
x3,y3=map(int,input().split())

xs=[x1,x2,x3]
ys=[y1,y2,y3]
points=[[x1,y1],[x2,y2],[x3,y3]]

xma=max(xs)
xmi=min(xs)
yma=max(ys)
ymi=min(ys)

if [xma,yma] not in points:
    print(xma,yma)
    sys.exit()
elif [xma,ymi] not in points:
    print(xma,ymi)
    sys.exit()
elif [xmi,yma] not in points:
    print(xmi,yma)
    sys.exit()
elif [xmi,ymi] not in points:
    print(xmi,ymi)
    sys.exit()
