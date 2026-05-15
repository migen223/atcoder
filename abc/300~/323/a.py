import sys
s=input()
for i in range(16):
    if i%2==1:
        if s[i]!="0":
            print("No")
            sys.exit()
print("Yes")