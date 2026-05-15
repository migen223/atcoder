import sys
n=int(input())
s=input()

ma=-1
f=0
count=0
"""
for i in range(n):
    if f==0 and s[i]=="-":
        f=1
    elif f==1 and s[i]=="o":
        count+=1
    elif f==1 and s[i]=="-":
        if count!=0:
            ma=max(ma,count)
            count=0
"""
for i in range(n):
    if s[i]=="-":
        ma=max(ma,count)
        count=0
    else:
        count+=1
ma=max(ma,count)

if "-" in s and "o" in s:
    print(ma)
else:
    print(-1)