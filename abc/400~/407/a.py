a,b=map(int,input().split())
s=a//b
if abs(s-a/b)>abs(s+1-a/b):
    print(s+1)
else:
    print(s)
