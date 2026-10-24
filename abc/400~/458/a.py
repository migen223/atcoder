

s=list(input())
n=int(input())

for i in range(n):
    s.pop()

ans =[]
for i in range(n,len(s)):
    ans.append(s[i])
print("".join(ans))