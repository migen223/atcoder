r,g,b=map(int,input().split())
c=input()
if c=="Blue":
    b=10000
elif c=="Red":
    r=1000000
else:
    g=10000000
print(min(r,g,b))