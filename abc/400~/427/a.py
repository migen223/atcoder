
s=input()
ans=""
for i in  range(len(s)):
    if i!=(len(s)+1)//2-1:
        ans+=s[i]
print(ans)