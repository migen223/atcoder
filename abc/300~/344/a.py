s=input()
ans=""
f=0
for i in range(len(s)):
    if s[i]=="|":
        f+=1
        continue
    if f==0 or f==2:
        ans+=s[i]
print(ans)