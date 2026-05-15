n=int(input())
x=[]
y=[]
for i in range(n):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)
if sum(x)==sum(y):
    print("Draw")
elif sum(x)>sum(y):
    print("Takahashi")
else:
    print("Aoki")