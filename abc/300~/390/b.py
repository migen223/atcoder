from fractions import Fraction
n=int(input())
a=list(map(int,input().split()))
d=Fraction(a[1],a[0])
check=1
for i in range(1,n-1):
    if a[i+1]==a[i]*d:
        check+=1
if check==n-1:
    print("Yes")
else:
    print("No")