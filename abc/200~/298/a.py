import sys
n=int(input())

s=input()

f=0
for i in range(n):
    if s[i]=="o":
        f+=1
    elif s[i]=="x":
        print("No")
        sys.exit()
if f!=0:
    print("Yes") 
else:
    print("No")

