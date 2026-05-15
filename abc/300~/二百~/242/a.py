a,b,c,x=map(int,input().split())

if x<=a:
    print(1)
elif b<x:
    print(0)
else:
    print(c/(b-(a)))

