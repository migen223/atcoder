a,b,c,d=map(int,input().split())
if a>c:
    print("Yes")
elif a==c:
    if b>=d:
        print("Yes")
    else:
        print("No")
else:
    print("No")