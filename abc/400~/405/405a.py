r,x=map(int,input().split())
#1->1600<=2999 2->2100<=2399

if x==1:
    if 1600<=r<=2999:
        print("Yes")
    else:
        print("No")
else:
    if 1200<=r<=2399:
        print("Yes")
    else:
        print("No")