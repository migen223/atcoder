
x,y,z=map(int,input().split())
s=input()
n=len(s)
dpoff=[10**32]*(n)
dpon=[10**32]*(n)

if s[0]=="A":
    dpoff[0]=y
    dpon[0]=z+x
else:
    dpoff[0]=x
    dpon[0]=z+y

for i in range(n-1):
    if s[i+1]=="A":
        dpoff[i+1]=min(dpon[i]+z+y,dpoff[i]+y)
        dpon[i+1]=min(dpoff[i]+z+x,dpon[i]+x)
    else:
        dpoff[i+1]=min(dpon[i]+z+x,dpoff[i]+x)
        dpon[i+1]=min(dpoff[i]+z+y,dpon[i]+y)
print(min(dpon[-1],dpoff[-1]))
