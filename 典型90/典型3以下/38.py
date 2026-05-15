from math import lcm
a,b=map(int,input().split())
if lcm(a,b)>10**18:
    print("Large")
else:
    print(lcm(a,b))
