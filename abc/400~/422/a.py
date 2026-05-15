s=list(input())
ans=""
if s[2]=="8":
    next=int(s[0])+1
    ans+=str(next)
    ans+="-1"
else:
    ans+=s[0]+s[1]
    next=int(s[2])+1
    ans+=str(next)
print(ans)