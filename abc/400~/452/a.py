
m,d=map(int,input().split())
if m==1:
    if d==7:
        print("Yes")
    else:
        print("No")
elif m%2==1 and m<11:
    if m==d:
        print("Yes")
    else:
        print("No")
else:
    print("No")