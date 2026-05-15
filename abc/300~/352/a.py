import sys
n,x,y,z=map(int,input().split())
if x<=y:
    for i in range(x,y+1):
        if i==z:
            print("Yes")
            sys.exit()
    print("No")
else:
    for i in range(y,x+1):
        if i==z:
            print("Yes")
            sys.exit()
    print("No")