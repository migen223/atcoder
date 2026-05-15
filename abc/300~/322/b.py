import sys
n,m=map(int,input().split())
s=input()
t=input()
f1=0
f2=0
for i in range(n):
    if t[i]==s[i]:
        f1+=1
    if t[-1-i]==s[-1-i]:
        f2+=1
#print(f1,f2)
if f1==f2==n:
    print(0)

elif f1==n and f2!=n:
    print(1)
elif f1!=n and f2==n:
    print(2)
else:
    print(3)


