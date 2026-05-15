s=input()
ans=""
ind=0
for i in range(len(s)):
    if s[-1-i]==".":
        ind=i
        break
for i in range(len(s)-ind,len(s)):
    ans+=s[i]
print(ans)
