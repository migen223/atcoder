s=input()
ans=""
l=["a","i","u","e","o"]
for i in range(len(s)):
    if s[i] not in l:
        ans+=s[i]
print(ans)