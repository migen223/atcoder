s=input()
now=0
ans=[]
for i in range(1,len(s)):
    if s[i]=="|":
        ans.append(now)
        now=0
    elif s[i]=="-":
        now+=1
print(*ans)