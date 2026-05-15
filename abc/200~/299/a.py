import sys
n=int(input())
s=input()

f=0
for i in range(n):
    if f==0 and s[i]=="|":
        f+=1
    elif f==1 and s[i]=="|":
        f+=1
    elif f==1 and s[i]=="*":
        print("in")
        sys.exit()
print("out")
