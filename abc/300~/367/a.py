a,b,c=map(int,input().split())
time=[0]*24
if b<c:
    if b<a<c:
        print("No")
    else:
        print("Yes")
else:
    if b<a or c>a:
        print("No")
    else:
        print("Yes")
