a,b=map(int,input().split())
ans=0
if a==b:
    print(1)
else:
    if abs(b-a)%2==0:
        print(3)
    else:
        print(2)