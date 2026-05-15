import sys
s=input()
t=input()
if len(s)<=len(t):
    for i in range(len(s)):
        if s[i]!=t[i]:
            print("No")
            sys.exit()
    print("Yes")
else:
    print("No")