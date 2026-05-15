s=list(input())
ans=0
if len(s)<3:
    print(0)
else:
    for i in range(len(s)-2):
        for j in range(i+1,len(s)-1):
            for k in range(i+2,len(s)):
                if j-i==k-j and s[i]=="A" and s[j]=="B" and s[k]=="C":
                    ans+=1
    print(ans)
