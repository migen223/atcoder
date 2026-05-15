n,l,r=map(int,input().split())
s=input()
f=0
for i in range(l-1,r):
    if s[i]!="o":
        f=1
if f==0:
    print("Yes")
else:
    print("No")