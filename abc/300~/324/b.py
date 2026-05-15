import sys
n=int(input())
y=0
if n==1:
    print("Yes")
elif n%3!=0 and n%2!=0:
    print("No")
else:
    while n%3==0:
        n=n//3
    while n%2==0:
        n=n//2
    if n==1:
        print("Yes")
    else:
        print("No")