import sys
s=input()
t=input()
if s==t:
    print(0)
elif len(s)>len(t):
    for i in range(len(t)):
        if s[i]!=t[i]:
            print(i+1)
            sys.exit()
    print(len(t)+1)
else:
    for i in range(len(s)):
        if s[i]!=t[i]:
            print(i+1)
            sys.exit()
    print(len(s)+1)
    

    