n=int(input())
t=(input())
a=(input())
f=0
for i in range(n):
    if t[i]==a[i]=="o":
        f+=1
if f>0:
    print("Yes")
else:
    print("No")