s=list(input())
if len(s)<=3:
    if s==["A","B","C"]:
        print("")
    else:
        print("".join(s))
else:
    ans=[s[0],s[1]]
    for i in range(2,len(s)):
        if len(ans)>=2:
            if ans[-2]=="A" and ans[-1]=="B" and s[i]=="C":
                ans.pop()
                ans.pop()
            else:
                ans.append(s[i])
        else:
            ans.append(s[i])
    print("".join(ans))

