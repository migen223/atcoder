import sys
s=input()
if s[0].isupper():
    for i in range(1,len(s)):
        if s[i].isupper():
            print("No")
            sys.exit()
    print("Yes")
else:
    print("No")