
s="atcoder"

ans=""
l,r=map(int,input().split())
for i in range(len(s)):
    if l-1<=i<=r-1:
        ans+=s[i]
print(ans)