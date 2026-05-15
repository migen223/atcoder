import sys
n,t=map(int,input().split())
c=list(map(int,input().split()))
r=list(map(int,input().split()))

ma=[-1,-1]
for i in range(n):
    if c[i]==t:
        if ma[0]<r[i]:
            ma[0]=r[i]
            ma[1]=i+1
    #print(ma)

if ma[0]!=-1:
    print(ma[1])
    sys.exit()

t=c[0]
ma=[r[0],1]
for i in range(n):
    if c[i]==t:
        if ma[0]<r[i]:
            ma[0]=r[i]
            ma[1]=i+1
print(ma[1])