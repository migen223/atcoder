import sys
s=input()
done=set()
"""
f=0
for i in range(len(s)):
    if f==0 and s[i]=="(":
        f=1
    elif f==1 and s[i]!="(" and s[i]!=")":
        if s[i] in done:
            print("No")
            sys.exit()
        else:
            done.add(s[i])
    elif f==1 and s[i]==")":
        f=0
        done=set()
        
for i in range(len(s)):

    if s[i]!="(" and s[i]!=")":
        if s[i] in done:
            print("No")
            sys.exit()
        else:
            done.add(s[i])
    elif s[i]==")":
        f=0
        done=set()
"""
words=[]
next=set()
words.append(next)
for i in range(len(s)):
    if s[i]=="(":
        n=words[-1]|set()
        words.append(n)
    elif s[i]==")":
        words.pop()
    else:
        if s[i] in words[-1]:
            print("No")
            sys.exit()
        else:
            words[-1].add(s[i])
   # print(words)

print("Yes")