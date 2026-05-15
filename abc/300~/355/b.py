import sys
n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
acounter=[0]*201
for i in range(n):
    acounter[a[i]]+=1
c=[]
for i in a:
    c.append(i)
for i in b:
    c.append(i)
c.sort()
for i in range(n+m-1):
    if c[i]==c[i+1]:
        if acounter[c[i]]>=2:
            print("Yes")
            sys.exit()
    else:
        if c[i] in a and c[i+1] in a:
            print("Yes")
            sys.exit()


print("No")