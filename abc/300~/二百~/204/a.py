x,y=map(int,input().split())
k=[0,1,2]
if x==y:
    print(x)
else:
    k.remove(x)
    k.remove(y)
    print(k[0])