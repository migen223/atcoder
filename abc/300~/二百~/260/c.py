

n,x,y=map(int,input().split())

ans=0
b=[0]*11
r=[0]*11
b[1]=1
for i in range(2,11):
    b[i]=r[i-1]+y*(b[i-1])
    r[i]=r[i-1]+x*b[i]
print(r[n])



