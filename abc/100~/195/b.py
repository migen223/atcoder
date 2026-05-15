a,b,w=map(int,input().split())

w*=1000

mi=10**12
ma=0
f=0

for i in range(1,10**6+2):
    if a*i<=w<=b*i:
        mi=min(mi,i)
        ma=max(ma,i)
        f+=1
if f>=1:
    print(mi,ma)
else:
    print("UNSATISFIABLE")
