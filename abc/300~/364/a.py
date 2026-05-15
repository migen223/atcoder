import sys
n=int(input())
s=[]
for i in range(n):
    s.append(input())
for i in range(n-1):
    if  s[i]==s[i+1]=="sweet":
        if i==n-2:
            print("Yes")
            sys.exit()
        else:
            print("No")
            sys.exit()
print("Yes")
