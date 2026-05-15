import sys
n,m=map(int,input().split())

xn=[]
for i in range(m):
    l=list(map(int,input().split()))
    k=l[0]
    x=set(l[1:])
    xn.append(x)
for i in range(1,n):
    for j in range(i+1,n+1):
        count=0
        for k in range(m):
            if i in xn[k] and j in xn[k]:
                count+=1
                break
        if count==0:
            print("No")
            sys.exit()
print("Yes")
