s=input()
ans=""
for i in range(len(s)):
    if i%2==0:
        ans+=s[i+1]
    else:
        ans+=s[i-1]
print(ans)