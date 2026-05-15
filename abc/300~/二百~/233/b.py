
ans=[]
l,r=map(int,input().split())

s=list(input())


words=s[l-1:r]

for i in range(l-1):
    ans.append(s[i])
for i in range(r-l+1):
    ans.append(words[-1-i])
for i in range(r,len(s)):
    ans.append(s[i])
print("".join(ans))

