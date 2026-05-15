x,y=map(int,input().split())
if x<y:
    if y-x>2:
        print("No")
    else:
        print("Yes")
elif x>y:
    if x-y>3:
        print("No")
    else:
        print("Yes")
else:
    print("Yes")