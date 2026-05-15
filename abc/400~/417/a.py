n,a,b=map(int,input().split())
s=input()
ans=""
for i in range(n):
    if a<=i<n-b:
        ans+=s[i]

print(ans)
