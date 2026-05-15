import sys
n=int(input())
s=input()
for i in range(n-1):
    if s[i]==s[i+1]:
        print("No")
        sys.exit()
print("Yes")