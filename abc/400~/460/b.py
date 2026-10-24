
t=int(input())

for _ in range(t):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    leng=(x2-x1)**2+(y2-y1)**2
    if leng<abs(r1-r2)**2:
        print("No")
    elif (leng==abs(r1-r2)**2):
        print("Yes")
    elif abs(r1-r2)**2<leng<(r1+r2)**2:
        print("Yes")
    elif leng==(r1+r2)**2:
        print("Yes")
    else:
        print("No")