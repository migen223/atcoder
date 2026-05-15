a,b=map(int,input().split())

if a==3 or a==6 or a==9:
    print("No")
elif b-a==1:
    print("Yes")
else:
    print("No")