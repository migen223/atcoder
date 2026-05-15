n,k=map(int,input().split())
i=input()
a=list(map(int,i.split()))
i=input()
b=list(map(int,i.split()))
dif=[]
for i in range(n):
    d=abs(a[i]-b[i])
    dif.append(d)
s=sum(dif)
if s>k:
    print("No")
else:
    if (k-s)%2==0:
        print("Yes")
    else:
        print("No")