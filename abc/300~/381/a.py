import sys
n=int(input())
s=list(input())
if n%2==0:
    print("No")
elif n==1:
    if s[0]=="/":
        print("Yes")
    else:
        print("No")
else:
    for i in range(n):
        if 0<=i<=(n+1)/2-2:
            if s[i]!="1":
                print("No")
                sys.exit()
        elif i==(n+1)/2-1:
            if s[i]!="/":
                print("No")
                sys.exit()
        else:
            if s[i]!="2":
                print("No")
                sys.exit()
    print("Yes")
