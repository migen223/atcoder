s=input()
se=set()
for i in range(10):
    se.add(str(i))

ans=[]
for i in range(len(s)):
    if s[i] in se:
        ans.append(s[i])
print("".join(ans))