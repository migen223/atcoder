s=input()
l=[]
for a in range(len(s)):
    if s[a]=="a":
        l.append(a+1)
if len(l)==0:
    print(-1)
else:
    print(max(l))