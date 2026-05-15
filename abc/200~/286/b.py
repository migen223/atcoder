
n=int(input())
s=list(input())
s.reverse()
ans=""
while s:
    if len(s)>=2:
        if s[-1]=="n" and s[-2]=="a":
            ans+="nya"
            s.pop()
            s.pop()
        else:
            ans+=s.pop()
    else:
        ans+=s.pop()
print(ans)

