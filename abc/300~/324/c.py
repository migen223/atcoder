
n,t=input().split()
n=int(n)
ans=[]
for i in range(n):
    s=input()
    if len(s)==len(t):
        diff=0
        for j in range(len(s)):
            if s[j]!=t[j]:
                diff+=1
        if diff<=1:
            ans.append(i+1) 
    elif len(s)+1==len(t):
        offset=0
        f=0
        now=0
        for j in range(len(t)):
            if now!=len(s):
                if s[now]==t[j]:
                    now+=1
                else:
                    f+=1
        if f<=1:
            ans.append(i+1)
    elif len(s)-1==len(t):
        offset=0
        f=0
        now=0
        for j in range(len(s)):
            if now!=len(t):
                if s[j]==t[now]:
                    now+=1
                else:
                    f+=1
        if f<=1:
            ans.append(i+1)
print(len(ans))
print(*ans)
 
            



