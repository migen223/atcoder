s=list(input())
ans=0
if s[0]=="o":
    ans+=1
if s[-1]=="i":
    ans+=1
if len(s)==1:
    print(1)
else:
    if s[0]==s[1]=="i":
        ans+=1
    if s[-1]==s[-2]=="o":
        ans+=1
    for i in range(1,len(s)-1):
        if s[i]==s[i-1]=="o":
            ans+=1
        elif s[i]==s[i+1]=="i":
            ans+=1
print(ans)
