import sys
s=list(input())
t=list(input())

if s==t:
    print("Yes")
    sys.exit()
else:
    for i in range(len(s)-1):
        s[i],s[i+1]=s[i+1],s[i]
        if s==t:
            print("Yes")
            sys.exit()
        s[i],s[i+1]=s[i+1],s[i]
print("No")