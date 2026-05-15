import sys
s=input()
t=input().lower()
first=0
second=0
if t[2]=="x":
    for i in range(len(s)-1):
        if t[0]==s[i]:
            first=i
            break
        if i==len(s)-2:
            print("No")
            sys.exit()
    for j in range(first+1,len(s)):
        if t[1]==s[j]:
            second=j
            break
        if j==len(s)-1:
            print("No")
            sys.exit()
    print("Yes")
else:
    for i in range(len(s)-2):
        if t[0]==s[i]:
            first=i
            break
        if i==len(s)-3:
            print("No")
            sys.exit()
    for j in range(first+1,len(s)-1):
        if t[1]==s[j]:
            second=j
            break
        if j==len(s)-2:
            print("No")
            sys.exit()
    for k in range(second+1,len(s)):
        if t[2]==s[k]:
            break
        if len(s)-1==k:
            print("No")
            sys.exit()
    print("Yes")