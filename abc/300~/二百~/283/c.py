
s=list(input())
s.reverse()
ans=0
while s:
    if len(s)>=2:
        if s[-1]==s[-2]=="0":
            ans+=1
            s.pop()
            s.pop()
        else:
            ans+=1
            s.pop()
    else:
        ans+=1
        s.pop()
print(ans)
