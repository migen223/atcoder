from math import gcd
x,y=map(int,input().split())

g=gcd(x,y)
if (x//g==16 and y//g==9):
    print("Yes")
else:
    print("No")