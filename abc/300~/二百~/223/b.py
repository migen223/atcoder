
s=list(input())

ans=["".join(s)]
def swap(s):
    ans=[]
    for i in range(1,len(s)):
        ans.append(s[i])
    ans.append(s[0])
    return "".join(ans)


for i in range(len(s)-1):
    s=swap(s)
    ans.append(s)
ans.sort()
print(ans[0])
print(ans[-1])


