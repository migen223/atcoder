s=input()
ans=0
for i in range(len(s)):
    if s[i]=="i" or s[i]=="j":
        ans+=1
print(ans)