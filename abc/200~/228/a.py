
s,t,x=map(int,input().split())

if s>t:
    if s<=x<24 or 0<=x<t:
        print("Yes")
    else:
        print("No")
else:
    if s<=x<t:
        print("Yes")
    else:
        print("No")