from math import sqrt,pow
n=int(input())
r=int(sqrt(n))
soinn=[]
for i in range(2,r+1):
    while n%i==0:
        soinn.append(i)
        n=n//i
if n!=1:
    soinn.append(n)
k=len(soinn)
x=0
while True:
    if 2**x>=k:
        print(x)
        break
    elif k==1:
        print(0) 
        break
    x+=1
