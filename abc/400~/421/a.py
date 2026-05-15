n=int(input())
a=[]
for _ in range(n):
    p=input()
    a.append(p)
x,y=input().split()
if a[int(x)-1]==y:
    print("Yes")
else:
    print("No")
